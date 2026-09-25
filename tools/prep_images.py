#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepara as fotos do site a partir do material original.

Uso:   python3 tools/prep_images.py
Lê:    assets/img/_source/   (as fotos originais, sem tratamento)
Grava: assets/img/           (versões cortadas, redimensionadas e otimizadas)

Cada entrada de RECIPES diz: arquivo de saída, foto de origem, proporção,
e o ponto focal (fx, fy) — a fração da imagem que deve ficar no centro do
corte. zoom=1.0 aproveita o máximo da foto; valores maiores aproximam.

Para trocar uma foto: ponha o arquivo novo em assets/img/_source/ e ajuste
a linha correspondente aqui. Depois rode o script e o build.
"""

from pathlib import Path
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "img" / "_source"
OUT = ROOT / "assets" / "img"

# apelidos curtos para as fotos originais
A = {
    "editorial": "editorial-gold.jpeg",       # retrato editorial, pele dourada
    "studio1": "studio-result-1.jpeg",        # resultado no estúdio (parede do logo)
    "studio2": "studio-result-2.jpeg",        # resultado no estúdio
    "studio3": "studio-result-3.jpeg",        # detalhe de torso / marquinha
    "beach1": "beach-1.jpeg",
    "beach2": "beach-2.jpeg",
    "beach3": "beach-3.jpeg",
    "beach4": "beach-4.jpeg",
    "beach5": "beach-5.jpeg",
    "beach6": "beach-6.jpeg",
    "frame1": "studio-frame-1.jpg",           # quadro do vídeo do estúdio
    "frame2": "studio-frame-2.jpg",
    # fotos de cena (cabine de jato, banho de lua, cílios) — deitadas, 3/2
    "spray": "spray-session.png",
    "moon1": "moon-classic.png",
    "moon2": "moon-premium.png",
    # fundo do site inteiro: pôr do sol na praia com folhas de palmeira
    "sunset": "bg-sunset.png",
    # as duas fotos da primeira dobra (entram em fusão, uma na outra)
    "model1": "hero-model-1.png",
    "model2": "hero-model-2.png",
    # 25/09/26: a cliente de preto segurando a tesoura e a fita
    "model3": "hero-model-3.png",
}

# (saída, origem, largura/altura, fx, fy, zoom [, "plain"])
# O 7º item, quando presente, desliga o tratamento fotográfico: é o caso do
# fundo do site, que já vem pronto e não pode ganhar vinheta nem mais calor.
RECIPES = [
    # FUNDO DO SITE INTEIRO — pôr do sol. Fica atrás de todas as seções,
    # por baixo do véu de areia translúcido do CSS.
    ("bg-sunset.jpg",         A["sunset"],    (2, 3),   0.50, 0.50, 1.00, "plain"),

    # primeira dobra — as duas fotos que se alternam em fusão
    ("hero-a.jpg",            A["model3"],    (3, 4),   0.50, 0.40, 1.00),
    ("hero-b.jpg",            A["model2"],    (3, 4),   0.50, 0.50, 1.00),

    # (hero.jpg — retrato antigo de cliente — saiu em 25/09/26)

    # conceito ("Mais que um bronzeado") — desde 23/09/26 é a foto de óculos
    # que antes alternava na primeira dobra. A antiga (praia) era A["beach5"].
    ("concept.jpg",           A["model2"],    (3, 4.2), 0.50, 0.45, 1.00),

    # cards de serviço (4/5) — lista nova da dona, 25/09/26
    ("svc-tape.jpg",          A["model3"],    (4, 5),   0.50, 0.30, 1.00),
    ("svc-fabric.jpg",        A["model2"],    (4, 5),   0.50, 0.45, 1.00),
    ("svc-moon-classic.jpg",  A["moon1"],     (4, 5),   0.48, 0.50, 1.00),
    ("svc-moon-premium.jpg",  A["moon2"],     (4, 5),   0.55, 0.50, 1.00),
    # esfoliação e hidratação: recortes mais fechados das mesmas cenas de IA
    # do banho de lua, para os cards não ficarem iguais aos vizinhos
    ("svc-exfol.jpg",         A["moon1"],     (4, 5),   0.18, 0.78, 1.70),
    ("svc-hydra.jpg",         A["moon2"],     (4, 5),   0.66, 0.62, 1.60),

]

MAX_W = 1500          # largura máxima da versão grande
SMALL_W = 700         # versão leve, usada no celular
QUALITY = 90          # skin tone pede compressão generosa
QUALITY_SM = 82


def crop_to(im, ratio, fx, fy, zoom=1.0):
    """Corta na proporção pedida, centrado no ponto focal (fx, fy)."""
    w, h = im.size
    tw, th = ratio
    target = tw / th

    # maior caixa com a proporção certa que cabe na imagem
    if w / h > target:
        bh = h
        bw = h * target
    else:
        bw = w
        bh = w / target

    bw /= zoom
    bh /= zoom
    bw, bh = min(bw, w), min(bh, h)

    cx, cy = fx * w, fy * h
    left = max(0, min(w - bw, cx - bw / 2))
    top = max(0, min(h - bh, cy - bh / 2))
    return im.crop((int(left), int(top), int(left + bw), int(top + bh)))


def grade(im):
    """
    Acabamento fotográfico: curva S suave, calor nos meios-tons e um leve
    escurecimento nas bordas. É o que separa "foto de celular" de "foto de
    campanha" — dá profundidade sem deixar artificial.
    """
    a = np.asarray(im).astype(np.float32) / 255.0

    # curva S: fecha um pouco as sombras e segura as altas luzes
    s = a * a * (3.0 - 2.0 * a)
    a = a * 0.78 + s * 0.22

    # calor só nos meios-tons: preserva branco e preto neutros
    mid = 1.0 - np.abs(a - 0.5) * 2.0
    a[..., 0] = a[..., 0] + 0.014 * mid[..., 0]
    a[..., 2] = a[..., 2] - 0.012 * mid[..., 2]
    a = np.clip(a, 0.0, 1.0)

    # vinheta discreta: o olho vai para o centro
    h, w = a.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    a *= (1.0 - 0.10 * np.clip(r - 0.62, 0, None) ** 1.6)[..., None]

    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), "RGB")
    return ImageEnhance.Color(out).enhance(1.05)


def fundo(im):
    """
    Tratamento do FUNDO do site (o pôr do sol atrás de todas as seções).

    O fundo tem um trabalho difícil: precisa ser visto e, ao mesmo tempo,
    deixar o texto preto legível por cima. Então ele é clareado e tem o
    contraste aberto — as sombras das palmeiras sobem, o céu continua
    dourado. Um desfoque leve tira o detalhe que só faria sujeira atrás
    das palavras (e disfarça a ampliação em telas grandes).

    Quem quiser mais praia: baixe o 0.16 (menos clareamento).
    Quem quiser ler melhor: suba o 0.16.
    """
    a = np.asarray(im).astype(np.float32) / 255.0
    a = a * (1.0 - 0.16) + 0.16          # clareia para o texto respirar
    a = 0.5 + (a - 0.5) * 0.90           # fecha o contraste
    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    out = out.filter(ImageFilter.GaussianBlur(2.0))
    return ImageEnhance.Color(out).enhance(1.10)


def sharpen(im):
    """Nitidez de saída — aplicada depois do redimensionamento."""
    return im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=64,
                                             threshold=3))


def main():
    if not SRC.exists():
        raise SystemExit(f"Pasta não encontrada: {SRC}")

    OUT.mkdir(parents=True, exist_ok=True)
    done = 0
    for recipe in RECIPES:
        name, source, ratio, fx, fy, zoom = recipe[:6]
        plain = len(recipe) > 6 and recipe[6] == "plain"
        path = SRC / source
        if not path.exists():
            print(f"  ! faltando: {source}  (pulando {name})")
            continue
        im = Image.open(path).convert("RGB")
        im = crop_to(im, ratio, fx, fy, zoom)
        im = fundo(im) if plain else grade(im)

        if im.width > MAX_W:
            nh = round(im.height * MAX_W / im.width)
            im = im.resize((MAX_W, nh), Image.LANCZOS)
        big = im if plain else sharpen(im)
        # o fundo do site fica sob um véu translúcido: detalhe fino ali não
        # aparece, então comprime mais e economiza o download de todo mundo.
        q, qs = (76, 68) if plain else (QUALITY, QUALITY_SM)
        big.save(OUT / name, "JPEG", quality=q, optimize=True,
                 progressive=True, subsampling=0)

        # versão leve para o celular (srcset)
        sw = min(SMALL_W, big.width)
        sh = round(big.height * sw / big.width)
        small = im.resize((sw, sh), Image.LANCZOS)
        if not plain:
            small = sharpen(small)
        small.save(OUT / name.replace(".jpg", "-sm.jpg"), "JPEG",
                   quality=qs, optimize=True, progressive=True)

        done += 1
        print(f"  ✓ {name:24s} {big.width}×{big.height}  +  {sw}×{sh}")
    print(f"\n{done} imagens geradas em assets/img/")


if __name__ == "__main__":
    main()
