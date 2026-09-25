#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepara o vídeo da primeira dobra (hero) a partir do material original.

Uso:   python3 tools/prep_video.py
Lê:    assets/video/_source/hero-studio.mp4   (vídeo original, do celular)
Grava: assets/video/hero.mp4      versão grande (desktop)
       assets/video/hero-sm.mp4   versão leve (celular)
       assets/img/hero-poster.jpg primeiro quadro, para aparecer antes de carregar

O que o script faz, na ordem:
  1. amplia o vídeo com Lanczos (o original é pequeno, 576x1024)
  2. aplica o mesmo acabamento das fotos (curva S, calor nos meios-tons,
     vinheta discreta e nitidez) — é o que dá o ar de campanha
  3. monta um laço "vai e volta": o vídeo roda para frente e depois de volta,
     então o loop não tem corte seco
  4. exporta H.264 sem áudio, com moov no início (começa a tocar na hora)

Para trocar o vídeo: ponha o arquivo novo em assets/video/_source/ com o mesmo
nome e rode o script outra vez.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "video" / "_source" / "hero-studio.mp4"
OUT = ROOT / "assets" / "video"
IMG = ROOT / "assets" / "img"

FFMPEG = Path.home() / ".local" / "bin" / "ffmpeg"
if not FFMPEG.exists():
    FFMPEG = Path("ffmpeg")

# O mesmo acabamento fotográfico das imagens, escrito em filtros de vídeo:
# curva S suave -> calor nos meios-tons -> vinheta -> nitidez de saída.
GRADE = (
    "curves=all='0/0 0.25/0.22 0.5/0.5 0.75/0.79 1/1'"
    ",colorbalance=rm=0.030:bm=-0.026:rs=0.010:bs=-0.008"
    ",eq=saturation=1.06:contrast=1.03"
    ",vignette=angle=PI/5.2:mode=forward"
    ",unsharp=5:5:0.62:5:5:0.0"
)

# (arquivo de saída, largura, altura, crf)
TARGETS = [
    ("hero.mp4",    1080, 1920, 23),   # desktop
    ("hero-sm.mp4",  620, 1102, 27),   # celular
]


def run(args):
    r = subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error",
                        "-y", *args])
    if r.returncode != 0:
        raise SystemExit(f"ffmpeg falhou: {' '.join(str(a) for a in args)}")


def main():
    if not SRC.exists():
        raise SystemExit(f"Vídeo original não encontrado: {SRC}")

    OUT.mkdir(parents=True, exist_ok=True)

    for name, w, h, crf in TARGETS:
        # sobe a resolução, aplica o acabamento, duplica em "vai e volta"
        chain = (
            f"[0:v]scale={w}:{h}:flags=lanczos,{GRADE},"
            f"format=yuv420p,split[fwd][rev];"
            f"[rev]reverse,trim=start_frame=1[rv];"
            f"[fwd][rv]concat=n=2:v=1:a=0[out]"
        )
        run(["-i", SRC,
             "-filter_complex", chain, "-map", "[out]",
             "-an",
             "-c:v", "libx264", "-profile:v", "high", "-level", "4.0",
             "-preset", "slow", "-crf", str(crf),
             "-pix_fmt", "yuv420p",
             "-movflags", "+faststart",
             OUT / name])
        kb = (OUT / name).stat().st_size / 1024
        print(f"  ✓ {name:14s} {w}×{h}  {kb:,.0f} KB")

    # poster: primeiro quadro já com o acabamento, para o navegador mostrar
    # enquanto o vídeo carrega (e no lugar dele quando o visitante pediu
    # "menos animação" no sistema)
    run(["-i", SRC, "-vf",
         f"scale=1080:1920:flags=lanczos,{GRADE}",
         "-frames:v", "1", "-q:v", "3", IMG / "hero-poster.jpg"])
    kb = (IMG / "hero-poster.jpg").stat().st_size / 1024
    print(f"  ✓ hero-poster.jpg  1080×1920  {kb:,.0f} KB")


if __name__ == "__main__":
    main()
