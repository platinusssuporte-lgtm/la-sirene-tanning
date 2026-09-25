#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador do site da LA SIRENE TANNING.

Uso:   python3 tools/build.py
Lê:    content/site.py
Grava: index.html      (espanhol — é o idioma principal)
       pt/index.html   (português)
       en/index.html   (inglês)

Não edite os index.html na mão — eles são reescritos a cada build.

COMO OS TRÊS IDIOMAS FUNCIONAM
------------------------------
No content/site.py, todo texto que o visitante lê está escrito assim:

    "title": {"es": "El Arte...", "pt": "A Arte...", "en": "The Art..."}

O build roda três vezes, uma por idioma, e em cada volta troca esses
blocos pelo texto daquele idioma. O resto do arquivo — nomes de foto,
links, números — passa igual.

Se você escrever um texto em espanhol e esquecer do português, o build
PARA e diz onde. É de propósito: melhor quebrar aqui do que publicar uma
página com um pedaço no idioma errado.
"""

import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from content import site as fonte  # noqa: E402

e = html.escape

# Ordem importa: o primeiro é o idioma da raiz do site.
IDIOMAS = ("es", "pt", "en")

# Como cada idioma se chama no atributo lang= e no hreflang, para o Google
# entender que são versões da mesma página.
CODIGO_LANG = {"es": "es", "pt": "pt-BR", "en": "en-US"}

# O nome de cada idioma no próprio idioma, para o seletor da navbar.
NOME_IDIOMA = {"es": "ES", "pt": "PT", "en": "EN"}

# nome por extenso, no próprio idioma — vai no title do link da bandeira
NOME_COMPLETO = {"es": "Español", "pt": "Português", "en": "English"}

# Os blocos de conteúdo que o build lê do site.py.
BLOCOS = [
    "AFTERCARE", "BRAND", "BRAZILIAN", "COMBOS", "CONCEPT", "CONTACT",
    "CTA", "FAQ", "FINAL_CTA", "FINDER", "FOOTER", "GALLERY", "HERO",
    "HOW", "LOCATION", "LOCATION_SECTION", "MOON_CLASSIC", "MOON_PREMIUM",
    "NAV", "PREP", "SEO", "SERVICES", "SHOP", "SPRAY", "TESTIMONIALS", "UI", "UV",
]

IDIOMA = IDIOMAS[0]


def traduzir(valor, idioma, onde="conteúdo"):
    """
    Devolve o conteúdo com os blocos de tradução já resolvidos no idioma
    pedido. Um bloco de tradução é um dicionário com exatamente as chaves
    es, pt e en; qualquer outro dicionário é percorrido por dentro.
    """
    if isinstance(valor, dict):
        chaves = set(valor)
        idiomas = set(IDIOMAS)
        if chaves == idiomas:
            return valor[idioma]
        if chaves & idiomas:
            faltando = ", ".join(sorted(idiomas - chaves))
            raise SystemExit(
                f"\n  ✗ Tradução incompleta em {onde}: falta {faltando}.\n"
                f"    Texto: {list(valor.values())[0]!r:.70}\n"
                f"    Todo texto no content/site.py precisa dos três "
                f"idiomas (es, pt, en).\n"
            )
        return {k: traduzir(v, idioma, f"{onde} → {k}") for k, v in valor.items()}
    if isinstance(valor, list):
        return [traduzir(v, idioma, f"{onde}[{i}]") for i, v in enumerate(valor)]
    if isinstance(valor, tuple):
        return tuple(traduzir(v, idioma, onde) for v in valor)
    return valor


def carregar_idioma(idioma):
    """Põe o conteúdo daquele idioma no lugar dos nomes que o build usa."""
    g = globals()
    g["IDIOMA"] = idioma
    for nome in BLOCOS:
        g[nome] = traduzir(getattr(fonte, nome), idioma, nome)
    # o link do WhatsApp leva a mensagem no idioma da página — por isso é
    # recalculado aqui, e não só uma vez no carregamento do script
    if "booking_href" in g:
        g["BOOK"] = booking_href()


def versionar_assets(html_pagina):
    """
    Carimba cada /assets/... com ?v=<impressão digital do arquivo>.
    O vercel.json manda o navegador guardar os assets por 1 ano sem
    perguntar de novo; sem o carimbo, trocar uma foto mantendo o nome
    (ex.: concept.jpg) deixa quem já visitou vendo a foto ANTIGA.
    """
    import hashlib
    import re

    def carimbo(m):
        caminho = m.group(0)
        arquivo = ROOT / caminho.lstrip("/")
        if not arquivo.is_file():
            return caminho
        v = hashlib.md5(arquivo.read_bytes()).hexdigest()[:8]
        return f"{caminho}?v={v}"

    return re.sub(r"/assets/[\w./-]+\.\w+(?![\w?])", carimbo, html_pagina)


def url_idioma(idioma):
    """
    Endereço da página naquele idioma. Absoluto de propósito: assim o link
    é o mesmo em qualquer página, e a raiz (/) é sempre o espanhol.
    """
    return "/" if idioma == IDIOMAS[0] else f"/{idioma}/"


carregar_idioma(IDIOMA)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def booking_href():
    """Para onde vão os botões de agendamento, na ordem de preferência."""
    if CONTACT.get("booking_url"):
        return CONTACT["booking_url"]
    if CONTACT.get("whatsapp"):
        msg = CONTACT.get("whatsapp_message", "")
        from urllib.parse import quote
        return f"https://wa.me/{CONTACT['whatsapp']}?text={quote(msg)}"
    return CONTACT.get("instagram_url", "#contact")


BOOK = booking_href()
BOOK_ATTRS = 'target="_blank" rel="noopener"' if BOOK.startswith("http") else ""


def price_label(value):
    """Preço definido, ou a frase padrão."""
    return e(value) if value else e(UI["price_on_booking"])


def price_html(value, cls="price"):
    if value:
        return f'<p class="{cls}">{e(value)}</p>'
    return f'<p class="{cls} price--tbd">{e(UI["price_on_booking"])}</p>'


def img_slot(image, brief, ratio="3/4", cls="", caption=None,
             sizes="(max-width:820px) 100vw, 40vw", eager=False):
    """
    Renderiza uma foto real (se houver) ou um slot desenhado com a legenda
    do que deve entrar ali. Trocar foto = preencher o campo no content/site.py.

    Quando existe a versão -sm (gerada por tools/prep_images.py), monta o
    srcset para o celular baixar o arquivo leve.
    """
    classes = f"media {cls}".strip()
    if image:
        src = f"/assets/img/{e(image)}"
        alt = e(caption or brief or "")
        small = ROOT / "assets" / "img" / image.replace(".jpg", "-sm.jpg")
        srcset = ""
        if small.exists():
            from PIL import Image as _I
            with _I.open(small) as _s:
                sw = _s.width
            with _I.open(ROOT / "assets" / "img" / image) as _b:
                bw = _b.width
            if bw > sw:
                srcset = (f' srcset="/assets/img/{e(small.name)} {sw}w, '
                          f'{src} {bw}w" sizes="{e(sizes)}"')
        load = ('fetchpriority="high"' if eager
                else 'loading="lazy" decoding="async"')
        return (
            f'<figure class="{classes}" style="--ratio:{ratio}">'
            f'<img src="{src}"{srcset} alt="{alt}" {load}>'
            f"</figure>"
        )
    label = e(brief or caption or UI["photo_slot"])
    return (
        f'<figure class="{classes} media--slot" style="--ratio:{ratio}">'
        f'<span class="media__mark" aria-hidden="true"></span>'
        f'<figcaption class="media__brief">{label}</figcaption>'
        f"</figure>"
    )


def section_head(eyebrow, title, subtitle=None, align="center", tag="h2"):
    sub = f'<p class="sec__sub">{subtitle}</p>' if subtitle else ""
    eb = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
    return (
        f'<header class="sec__head sec__head--{align}" data-reveal>'
        f"{eb}"
        f'<{tag} class="sec__title">{title}</{tag}>'
        f"{sub}"
        f"</header>"
    )


# ---------------------------------------------------------------------------
# ícones desenhados à mão (SVG dentro da própria página)
#
# Ficam embutidos no HTML de propósito: não custam nenhum download a mais,
# aparecem no primeiro quadro e acompanham a cor do texto onde estão.
# ---------------------------------------------------------------------------

BANDEIRAS = {
    # Espanha
    "es": ('<rect width="20" height="14" fill="#C60B1E"/>'
           '<rect y="3.5" width="20" height="7" fill="#FFC400"/>'),
    # Brasil
    "pt": ('<rect width="20" height="14" fill="#009B3A"/>'
           '<path d="M10 1.7 18.3 7 10 12.3 1.7 7Z" fill="#FEDF00"/>'
           '<circle cx="10" cy="7" r="2.9" fill="#002776"/>'),
    # Estados Unidos
    "en": ('<rect width="20" height="14" fill="#FFFFFF"/>'
           '<g fill="#B22234"><rect width="20" height="2"/>'
           '<rect y="4" width="20" height="2"/>'
           '<rect y="8" width="20" height="2"/>'
           '<rect y="12" width="20" height="2"/></g>'
           '<rect width="9" height="8" fill="#3C3B6E"/>'),
}


def bandeira(idioma):
    """Bandeirinha do idioma — só desenho, quem lê a página ouve só o nome."""
    return ('<svg class="flag" viewBox="0 0 20 14" width="20" height="14" '
            'aria-hidden="true" focusable="false">'
            + BANDEIRAS[idioma] + "</svg>")


# contorno oficial do balão do WhatsApp, em 24×24
ZAP_PATH = (
    "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67."
    "15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255"
    "-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13"
    "-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-."
    "371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a"
    "12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04"
    " 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709."
    "306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 "
    "2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-"
    "5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-"
    "3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-"
    "9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 "
    "5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5."
    "495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-"
    "1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-"
    "11.893a11.821 11.821 0 0 0-3.48-8.413Z"
)


def icone_zap(classe="zap"):
    """Logo do WhatsApp. Herda a cor do texto do botão onde está."""
    return (f'<svg class="{classe}" viewBox="0 0 24 24" width="18" height="18" '
            f'aria-hidden="true" focusable="false"><path fill="currentColor" '
            f'd="{ZAP_PATH}"/></svg>')


def e_whatsapp(href):
    """Esse link abre uma conversa no WhatsApp?"""
    return "wa.me" in href or "api.whatsapp.com" in href


def btn(label, href, kind="primary", attrs=""):
    # todo botão que leva para o WhatsApp leva também o desenho do WhatsApp:
    # o visitante já sabe, antes de clicar, onde a conversa vai acontecer.
    icone = icone_zap("btn__zap") if e_whatsapp(href) else ""
    return (f'<a class="btn btn--{kind}" href="{href}" {attrs}>'
            f'{icone}<span>{e(label)}</span></a>')


def book_btn(label=None, kind="primary"):
    return btn(label or CTA["primary"], BOOK, kind, BOOK_ATTRS)


def rule():
    return '<span class="rule" aria-hidden="true"></span>'


# ---------------------------------------------------------------------------
# secções
# ---------------------------------------------------------------------------

def head():
    robots = (
        '<meta name="robots" content="noindex, nofollow">'
        if SEO.get("noindex") else
        '<meta name="robots" content="index, follow">'
    )
    # Cada idioma tem o seu próprio endereço. O canonical aponta para o
    # endereço daquela página, e os hreflang dizem ao Google que as três são
    # a mesma página em idiomas diferentes — sem isso ele trataria como
    # conteúdo repetido.
    base = (SEO.get("canonical") or "").rstrip("/")
    canonical = ""
    alternates = ""
    if base:
        sufixo = "" if IDIOMA == IDIOMAS[0] else f"/{IDIOMA}"
        canonical = f'<link rel="canonical" href="{e(base + sufixo + "/")}">'
        linhas = [
            f'<link rel="alternate" hreflang="{CODIGO_LANG[i]}" '
            f'href="{e(base + ("" if i == IDIOMAS[0] else "/" + i) + "/")}">'
            for i in IDIOMAS
        ]
        linhas.append(f'<link rel="alternate" hreflang="x-default" '
                      f'href="{e(base + "/")}">')
        alternates = "\n".join(linhas)
    ld = local_business_jsonld()
    return f"""<!DOCTYPE html>
<html lang="{CODIGO_LANG[IDIOMA]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(SEO["title"])}</title>
<meta name="description" content="{e(SEO["description"])}">
<meta name="keywords" content="{e(SEO["keywords"])}">
{robots}
{canonical}
{alternates}
<meta property="og:type" content="website">
<meta property="og:title" content="{e(SEO["title"])}">
<meta property="og:description" content="{e(SEO["description"])}">
<meta property="og:locale" content="{CODIGO_LANG[IDIOMA].replace("-", "_")}">
<meta name="theme-color" content="#E8DFD2">
<link rel="icon" href="/assets/logo/lasirene-mark-black.png">
<link rel="apple-touch-icon" href="/assets/logo/lasirene-mark-black.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
<noscript><style>
[data-reveal]{{opacity:1!important;transform:none!important}}
[data-reveal] .media::after{{display:none!important}}
[data-reveal] .media img{{transform:none!important}}
.rule{{transform:scaleX(1)!important}}
.intro{{display:none!important}}
.hero__mark,.hero__eyebrow,.hero__services,.hero__quote,.hero__cta{{
opacity:1!important;transform:none!important}}
</style></noscript>
{ld}
</head>
<body id="top">
<div class="intro" aria-hidden="true">
  <div>
    <img src="/assets/logo/lasirene-mark-gold.png" alt="" class="intro__mark">
    <p class="intro__word">La Sirene</p>
  </div>
</div>
<div class="grain" aria-hidden="true"></div>
"""


def local_business_jsonld():
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "BeautySalon",
        "name": BRAND["name_full"],
        "description": SEO["description"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": BRAND["city"],
            "addressRegion": BRAND["state_short"],
            "addressCountry": "US",
        },
        "areaServed": f'{BRAND["city"]}, {BRAND["state"]}',
        "sameAs": [CONTACT["instagram_url"]] if CONTACT.get("instagram_url") else [],
    }
    if LOCATION.get("address_line1"):
        data["address"]["streetAddress"] = LOCATION["address_line1"]
    if CONTACT.get("phone_href"):
        data["telephone"] = CONTACT["phone_href"]
    if SEO.get("canonical"):
        data["url"] = SEO["canonical"]
    offers = []
    for s in SERVICES:
        offers.append({"@type": "Offer", "itemOffered": {
            "@type": "Service", "name": s["name_plain"]}})
    data["makesOffer"] = offers
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False) + "</script>")


def seletor_idioma(classe="lang"):
    """
    Troca de idioma. Cada idioma é um endereço próprio, então são links de
    verdade — funcionam sem JavaScript e o Google segue os três.

    Cada um leva a sua bandeira: quem chega no idioma errado reconhece a
    bandeira sem precisar ler nada, que é o caminho mais curto até a página
    certa. A bandeira é só desenho — quem usa leitor de tela ouve o nome.
    """
    itens = []
    for i in IDIOMAS:
        atual = ' aria-current="true"' if i == IDIOMA else ""
        itens.append(
            f'<a href="{e(url_idioma(i))}" hreflang="{CODIGO_LANG[i]}"'
            f'{atual} lang="{CODIGO_LANG[i]}" title="{e(NOME_COMPLETO[i])}">'
            f'{bandeira(i)}<span>{e(NOME_IDIOMA[i])}</span></a>'
        )
    return (f'<div class="{classe}" role="group" '
            f'aria-label="{e(SEO["language_label"])}">' + "".join(itens) + "</div>")


def navbar():
    links = "".join(
        f'<li><a href="{e(href)}" data-nav>{e(label)}</a></li>'
        for label, href in NAV
    )
    return f"""
<header class="nav" id="nav">
  <div class="nav__inner">
    <a class="nav__brand" href="#top" aria-label="{e(BRAND['name_full'])} — home">
      <img src="/assets/logo/lasirene-mark-black.png" alt="" class="nav__mark">
      <span class="nav__word">La Sirene</span>
    </a>
    <nav class="nav__links" aria-label="{e(SEO["nav_label"])}">
      <ul>{links}</ul>
    </nav>
    <div class="nav__actions">
      {seletor_idioma("lang")}
      {book_btn(CTA["primary_short"], "nav")}
      <button class="nav__toggle" id="navToggle" aria-label="{e(SEO["menu_label"])}" aria-expanded="false" aria-controls="mobileMenu">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>

<div class="menu" id="mobileMenu" aria-hidden="true">
  <div class="menu__inner">
    <img src="/assets/logo/lasirene-mark-gold.png" alt="" class="menu__mark">
    <nav aria-label="{e(SEO["nav_label"])}"><ul>{links}</ul></nav>
    <div class="menu__foot">
      {seletor_idioma("lang lang--menu")}
      {book_btn(CTA["primary"], "primary")}
      <a class="menu__ig" href="{e(CONTACT['instagram_url'])}" target="_blank" rel="noopener">{e(CONTACT['instagram_handle'])}</a>
    </div>
  </div>
</div>
"""


def hero_fig_class():
    """Modificador da coluna da imagem: fotos em fusão, vídeo, slot ou foto."""
    if HERO.get("images"):
        return " hero__figure--slides"
    if HERO.get("video"):
        return " hero__figure--video"
    if HERO.get("image"):
        return ""
    return " hero__figure--slot"


def hero_fig_style():
    """Enquadramento das fotos/vídeo (o ponto da altura que fica no centro)."""
    if not (HERO.get("video") or HERO.get("images")):
        return ""
    parts = []
    if HERO.get("focus"):
        parts.append(f'--hero-focus:{e(HERO["focus"])}')
    if HERO.get("focus_mobile"):
        parts.append(f'--hero-focus-mobile:{e(HERO["focus_mobile"])}')
    return f' style="{";".join(parts)}"' if parts else ""


def _srcset_de(nome, sizes):
    """srcset/sizes de uma foto, quando existe a versão -sm gerada pelo prep."""
    from PIL import Image as _I
    pequena = ROOT / "assets" / "img" / nome.replace(".jpg", "-sm.jpg")
    if not pequena.exists():
        return ""
    with _I.open(pequena) as _s, _I.open(ROOT / "assets" / "img" / nome) as _b:
        if _b.width <= _s.width:
            return ""
        return (f' srcset="/assets/img/{e(pequena.name)} {_s.width}w, '
                f'/assets/img/{e(nome)} {_b.width}w" sizes="{e(sizes)}"')


def hero_slides():
    """
    Primeira dobra em FOTOS: elas se alternam em fusão suave, em laço.

    A primeira já vem visível e marcada como prioritária — é a imagem que o
    visitante vê antes de qualquer coisa. As seguintes entram em preguiçosa,
    então quem só olha o topo e vai embora baixa uma foto só.

    Quem pediu "menos animação" no sistema fica na primeira foto parada: o
    script sai antes de agendar a troca.
    """
    fotos = HERO["images"]
    sizes = "(max-width:980px) 100vw, 50vw"
    tags = []
    for i, nome in enumerate(fotos):
        primeira = i == 0
        tags.append(
            f'<img class="hero__slide{" is-on" if primeira else ""}" '
            f'src="/assets/img/{e(nome)}"{_srcset_de(nome, sizes)} alt="" '
            + ('fetchpriority="high" decoding="async"' if primeira
               else 'loading="lazy" decoding="async"')
            + ">"
        )
    return "".join(tags) + f"""
  <script>
  (function(){{
    var box=document.currentScript.parentNode;
    var fotos=box.querySelectorAll(".hero__slide");
    if(fotos.length<2)return;
    if(window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;
    var i=0;
    setInterval(function(){{
      fotos[i].classList.remove("is-on");
      i=(i+1)%fotos.length;
      fotos[i].classList.add("is-on");
    }},{HERO.get("slide_seconds", 5.5)}*1000);
  }})();
  </script>"""


def hero_video():
    """
    Vídeo da primeira dobra: sem som, em laço, sem controles.

    O elemento nasce SEM src: o trecho de script logo abaixo escolhe o arquivo
    (leve no celular, grande no desktop) antes de o navegador começar a baixar,
    então nunca baixa os dois. Quem pediu "menos animação" no sistema — e quem
    está sem JavaScript — fica no poster, que é o primeiro quadro do vídeo.
    """
    poster = HERO.get("poster") or ""
    big = HERO["video"]
    small = HERO.get("video_small") or big
    poster_attr = f' poster="/assets/img/{e(poster)}"' if poster else ""
    return f"""<video class="hero__video"{poster_attr}
         autoplay muted loop playsinline preload="auto"
         aria-hidden="true" tabindex="-1"></video>
  <script>
  (function(){{
    var v=document.currentScript.previousElementSibling;
    if(window.matchMedia("(prefers-reduced-motion: reduce)").matches)return;
    v.src=window.matchMedia("(min-width: 981px)").matches
      ? "/assets/video/{e(big)}" : "/assets/video/{e(small)}";
    var play=function(){{var p=v.play();if(p&&p.catch)p.catch(function(){{}});}};
    play();v.addEventListener("loadeddata",play,{{once:true}});
  }})();
  </script>"""


def hero():
    services = "".join(
        f'<li>{e(s)}</li>' for s in HERO["services_line"]
    )
    if HERO.get("images"):
        fig = hero_slides()
    elif HERO.get("video"):
        fig = hero_video()
    elif HERO.get("image"):
        from PIL import Image as _I
        _n = HERO["image"]
        _sm = ROOT / "assets" / "img" / _n.replace(".jpg", "-sm.jpg")
        _ss = ""
        if _sm.exists():
            with _I.open(_sm) as _s1, _I.open(ROOT / "assets" / "img" / _n) as _b1:
                if _b1.width > _s1.width:
                    _ss = (f' srcset="/assets/img/{e(_sm.name)} {_s1.width}w, '
                           f'/assets/img/{e(_n)} {_b1.width}w"'
                           f' sizes="(max-width:980px) 100vw, 50vw"')
        fig = (f'<img src="/assets/img/{e(_n)}"{_ss} alt="" '
               f'fetchpriority="high" decoding="async">')
    else:
        fig = ('<span class="hero__figmark" aria-hidden="true"></span>'
               f'<span class="hero__figbrief">{e(HERO["image_brief"])}</span>')
    return f"""
<section class="hero" aria-label="La Sirene Tanning">
  <div class="hero__text">
    <div class="hero__inner">
      <p class="hero__eyebrow"><span class="dot" aria-hidden="true"></span>{e(HERO['eyebrow'])}</p>
      <img src="/assets/logo/lasirene-mark-gold.png" alt="" class="hero__mark">
      <h1 class="hero__brand">La Sirene<span class="hero__brandsub">Tanning</span></h1>
      <p class="hero__title">{HERO['title']}</p>
      <ul class="hero__services">{services}</ul>
      <p class="hero__quote">{e(HERO['quote'])}</p>
      <div class="hero__cta">
        {book_btn(CTA["primary"], "primary")}
        {btn(CTA["secondary"], "#services", "ghost")}
      </div>
    </div>
    <a class="hero__scroll" href="#concept" aria-label="{e(UI['scroll_hint'])}"><span></span></a>
  </div>
  <div class="hero__figure{hero_fig_class()}"{hero_fig_style()}>{fig}</div>
</section>
"""


def concept():
    pillars = "".join(f"<li>{e(p)}</li>" for p in CONCEPT["pillars"])
    body = "".join(f"<p>{e(p)}</p>" for p in CONCEPT["body"])
    return f"""
<section class="concept" id="concept">
  <div class="wrap concept__grid">
    <div class="concept__text" data-reveal>
      <p class="eyebrow">{e(CONCEPT['eyebrow'])}</p>
      <h2 class="concept__title">{CONCEPT['title']}</h2>
      {rule()}
      <div class="concept__body">{body}</div>
      <ul class="pillars">{pillars}</ul>
    </div>
    <div class="concept__media" data-reveal>
      {img_slot(CONCEPT['image'], CONCEPT['image_brief'], ratio="3/4.2")}
    </div>
  </div>
</section>
"""


def services():
    cards = []
    for s in SERVICES:
        featured = " card--featured" if s.get("featured") else ""
        cards.append(f"""
      <article class="card{featured}" data-reveal>
        <a class="card__link" href="{e(s.get('target') or '#' + s['id'])}">
          {img_slot(s['image'], s['image_brief'], ratio="4/5", cls="card__media")}
          <div class="card__body">
            <p class="card__index">{e(s['index'])}</p>
            <h3 class="card__name">{s['name']}</h3>
            <p class="card__sub">{e(s['subtitle'])}</p>
            <p class="card__desc">{e(s['short'])}</p>
            <p class="card__price">{price_label(s['price'])}</p>
            <span class="card__more">{e(UI["learn_more"])}<i aria-hidden="true"></i></span>
          </div>
        </a>
      </article>""")
    return f"""
<section class="services" id="services">
  <div class="wrap">
    {section_head(UI["services_eyebrow"], e(UI["services_title"]),
                  e(UI["services_subtitle"]))}
    <div class="cards">{''.join(cards)}</div>
  </div>
</section>
"""


def brazilian():
    choices = "".join(
        f'<li><span class="choice__k">{e(k)}</span>'
        f'<span class="choice__v">{e(v)}</span></li>'
        for k, v in BRAZILIAN["choices"]
    )
    paths = "".join(
        f'<li class="path{" path--main" if i == 0 else ""}" data-reveal>'
        f'<p class="path__tag">{e(p["tag"])}</p>'
        f'<h4 class="path__n">{e(p["name"])}</h4>'
        f'<p class="path__lead">{e(p["lead"])}</p>'
        f'<p class="path__d">{e(p["body"])}</p></li>'
        for i, p in enumerate(BRAZILIAN["paths"])
    )
    compare = []
    for c in BRAZILIAN["compare"]:
        pts = "".join(f"<li>{e(p)}</li>" for p in c["points"])
        compare.append(f"""
        <article class="vs__item" data-reveal>
          {img_slot(c['image'], c['image_brief'], ratio="1/1", cls="vs__media")
           if c['image'] else ''}
          <h4 class="vs__name">{e(c['name'])}</h4>
          <p class="vs__lead">{e(c['lead'])}</p>
          <p class="vs__desc">{e(c['desc'])}</p>
          <ul class="vs__points">{pts}</ul>
        </article>""")
    return f"""
<section class="deep deep--brazilian" id="brazilian-tan">
  <div class="wrap">
    <div class="deep__head" data-reveal>
      <p class="eyebrow">{e(BRAZILIAN['eyebrow'])}</p>
      <h2 class="deep__title">{BRAZILIAN['title']}</h2>
      <p class="deep__sub">{e(BRAZILIAN['subtitle'])}</p>
      {rule()}
      <p class="deep__body">{e(BRAZILIAN['body'])}</p>
    </div>

    <div class="banner" data-reveal>
      <p class="banner__text">{e(BRAZILIAN['highlight'])}</p>
    </div>

    <div class="choices" data-reveal>
      <h3 class="choices__title">{e(BRAZILIAN['choices_title'])}</h3>
      <ul class="choices__list">{choices}</ul>
    </div>

    <div class="vs">
      <h3 class="vs__title" data-reveal>{e(BRAZILIAN['compare_title'])}</h3>
      <div class="vs__grid">
        {compare[0]}
        <span class="vs__sep" aria-hidden="true">vs.</span>
        {compare[1]}
      </div>
    </div>

    <div class="paths">
      <h3 class="styles__title" data-reveal>{e(BRAZILIAN['paths_title'])}</h3>
      <p class="styles__intro" data-reveal>{e(BRAZILIAN['paths_intro'])}</p>
      <ul class="paths__list">{paths}</ul>
    </div>
    <div class="note" data-reveal>
      <h4>{e(BRAZILIAN['guidance_title'])}</h4>
      <p>{e(BRAZILIAN['guidance_body'])}</p>
    </div>
  </div>
</section>
"""


def spray():
    steps = "".join(
        f'<li data-reveal><span class="step__n">{e(n)}</span>'
        f'<h4 class="step__t">{e(t)}</h4>'
        f'<p class="step__d">{e(d)}</p></li>'
        for n, t, d in SPRAY["steps"]
    )
    before = "".join(
        f"<li>{e(i)}</li>" if i else f'<li class="editable">{e(UI["guidance_slot"])}</li>'
        for i in SPRAY["before_items"]
    )
    return f"""
<section class="deep deep--spray" id="spray-tanning">
  <div class="wrap">
    <div class="deep__head deep__head--center" data-reveal>
      <p class="eyebrow">{e(SPRAY['eyebrow'])}</p>
      <h2 class="deep__title">{e(SPRAY['title'])}</h2>
      <p class="deep__sub">{e(SPRAY['subtitle'])}</p>
      {rule()}
      <p class="deep__body">{e(SPRAY['body'])}</p>
    </div>
    <ol class="steps steps--5">{steps}</ol>
    <div class="panel" data-reveal>
      <h3 class="panel__title">{e(SPRAY['before_title'])}</h3>
      <p class="panel__intro">{e(SPRAY['before_intro'])}</p>
      <ul class="panel__list">{before}</ul>
    </div>
  </div>
</section>
"""


def uv():
    styles = "".join(
        f'<li data-reveal><span class="style__mark" aria-hidden="true"></span>'
        f'<h4 class="style__n">{e(n)}</h4><p class="style__d">{e(d)}</p></li>'
        for n, d in UV["styles"]
    )
    # Fora da página desde 25/09/26 (o UV virou parte do Brasileiro; os
    # "dois caminhos" e a orientação da sessão foram para brazilian()).
    return f"""
<section class="deep deep--uv" id="uv-tan">
  <div class="wrap">
    <div class="deep__head deep__head--center" data-reveal>
      <p class="eyebrow">{e(UV['eyebrow'])}</p>
      <h2 class="deep__title">{e(UV['title'])}</h2>
      <p class="deep__sub">{e(UV['subtitle'])}</p>
      {rule()}
      <p class="deep__body">{e(UV['body'])}</p>
    </div>
    <div class="styles">
      <h3 class="styles__title" data-reveal>{e(UV['styles_title'])}</h3>
      <p class="styles__intro" data-reveal>{e(UV['styles_intro'])}</p>
      <ul class="styles__list">{styles}</ul>
    </div>
  </div>
</section>
"""


def moon():
    tl = "".join(
        f'<li data-reveal><span class="tl__n">{e(n)}</span>'
        f'<div><h4 class="tl__t">{e(t)}</h4><p class="tl__d">{e(d)}</p></div></li>'
        for n, t, d in MOON_CLASSIC["timeline"]
    )
    pil = "".join(
        f'<li data-reveal><h4>{e(n)}</h4><p>{e(d)}</p></li>'
        for n, d in MOON_PREMIUM["pillars"]
    )
    return f"""
<section class="deep deep--moon" id="banho-de-lua-classic">
  <div class="wrap">
    <div class="deep__head" data-reveal>
      <p class="eyebrow">{e(MOON_CLASSIC['eyebrow'])}</p>
      <h2 class="deep__title">{MOON_CLASSIC['title']}</h2>
      <p class="deep__sub">{e(MOON_CLASSIC['subtitle'])}</p>
      {rule()}
      <p class="deep__body">{e(MOON_CLASSIC['body'])}</p>
    </div>
    <ol class="tl">{tl}</ol>
  </div>
</section>

<section class="premium" id="banho-de-lua-premium">
  <div class="wrap">
    <div class="premium__head" data-reveal>
      <p class="eyebrow eyebrow--light">{e(MOON_PREMIUM['eyebrow'])}</p>
      <h2 class="premium__title">{MOON_PREMIUM['title']}</h2>
      <p class="premium__sub">{e(MOON_PREMIUM['subtitle'])}</p>
      <p class="premium__body">{e(MOON_PREMIUM['body'])}</p>
    </div>
    <ul class="premium__pillars">{pil}</ul>
    <p class="premium__closing" data-reveal>{e(MOON_PREMIUM['closing'])}</p>
    <div class="premium__cta" data-reveal>{book_btn(CTA['primary'], 'light')}</div>
  </div>
</section>
"""


def combos():
    items = "".join(f"""
      <article class="combo" data-reveal>
        <h3 class="combo__name">{e(c['name'])}</h3>
        {rule()}
        <p class="combo__desc">{e(c['desc'])}</p>
        {price_html(c['price'], 'combo__price')}
        {book_btn(CTA['primary_short'], 'ghost')}
      </article>""" for c in COMBOS["items"])
    return f"""
<section class="combos" id="combos">
  <div class="wrap">
    {section_head(COMBOS['eyebrow'], e(COMBOS['title']), e(COMBOS['subtitle']))}
    <div class="combos__grid">{items}</div>
  </div>
</section>
"""


# ícones de linha fina, desenhados à mão (sem download), para a Boutique
ICONES_SHOP = {
    "bikini": '<path d="M6 5l5 8a3 3 0 0 0 5 0 3 3 0 0 0 5 0l5-8M16 11v2M7 20h18l-6 7h-6z"/>',
    "frasco": '<path d="M13 4h6v4h-6zM11 8h10l1 4v14a2 2 0 0 1-2 2h-8a2 2 0 0 1-2-2V12zM10 16h12"/>',
    "joia": '<path d="M10 6h12l4 6-10 14L6 12zM6 12h20M13 6l3 6 3-6M16 12v14"/>',
}


def shop():
    items = "".join(f"""
      <article class="combo shop__item" data-reveal>
        <svg class="shop__icon" viewBox="0 0 32 32" aria-hidden="true" fill="none"
             stroke="currentColor" stroke-width="1.2" stroke-linecap="round"
             stroke-linejoin="round">{ICONES_SHOP[i['icon']]}</svg>
        <h3 class="combo__name">{e(i['name'])}</h3>
        {rule()}
        <p class="combo__desc">{e(i['desc'])}</p>
        {book_btn(SHOP['cta'], 'ghost')}
      </article>""" for i in SHOP["items"])
    return f"""
<section class="combos shop" id="boutique">
  <div class="wrap">
    {section_head(SHOP['eyebrow'], SHOP['title'], e(SHOP['subtitle']))}
    <div class="combos__grid shop__grid">{items}</div>
    <p class="shop__note" data-reveal>{e(SHOP['note'])}</p>
  </div>
</section>
"""


def finder():
    opts = "".join(f"""
      <a class="finder__card" href="{e(o['target'])}" data-reveal>
        <span class="finder__want">&ldquo;{e(o['want'])}&rdquo;</span>
        <span class="finder__arrow" aria-hidden="true"></span>
        <span class="finder__answer">{e(o['answer'])}</span>
      </a>""" for o in FINDER["options"])
    return f"""
<section class="finder" id="finder">
  <div class="wrap">
    {section_head(FINDER['eyebrow'], e(FINDER['title']), e(FINDER['subtitle']))}
    <div class="finder__grid">{opts}</div>
  </div>
</section>
"""


def how():
    steps = "".join(
        f'<li data-reveal><span class="hstep__n">{e(n)}</span>'
        f'<h3 class="hstep__t">{e(t)}</h3>'
        f'<p class="hstep__d">{e(d)}</p></li>'
        for n, t, d in HOW["steps"]
    )
    return f"""
<section class="how" id="how-it-works">
  <div class="wrap">
    {section_head(HOW['eyebrow'], e(HOW['title']), e(HOW['subtitle']))}
    <ol class="hsteps">{steps}</ol>
  </div>
</section>
"""


def prep():
    items = "".join(
        f'<li data-reveal><span class="prep__when">{e(w)}</span>'
        f'<span class="prep__line" aria-hidden="true"></span>'
        f'<p class="prep__what">{e(t)}</p></li>'
        for w, t in PREP["items"]
    )
    return f"""
<section class="prep" id="prep">
  <div class="wrap">
    {section_head(PREP['eyebrow'], PREP['title'], e(PREP['subtitle']))}
    <ol class="prep__list">{items}</ol>
    <p class="prep__note" data-reveal>{e(PREP['note'])}</p>
  </div>
</section>
"""


def aftercare():
    blocks = ""
    for b in AFTERCARE["blocks"]:
        li = "".join(
            f"<li>{e(i)}</li>" if i else f'<li class="editable">{e(UI["guidance_slot"])}</li>'
            for i in b["items"]
        )
        blocks += (f'<article class="ac__block" data-reveal>'
                   f'<h3 class="ac__title">{e(b["title"])}</h3>'
                   f'<ul class="ac__list">{li}</ul></article>')
    do = "".join(
        f"<li>{e(i)}</li>" if i else f'<li class="editable">{e(UI["guidance_slot"])}</li>'
        for i in AFTERCARE["do"]
    )
    dont = "".join(
        f"<li>{e(i)}</li>" if i else f'<li class="editable">{e(UI["guidance_slot"])}</li>'
        for i in AFTERCARE["dont"]
    )
    return f"""
<section class="ac" id="aftercare">
  <div class="wrap">
    {section_head(AFTERCARE['eyebrow'], e(AFTERCARE['title']), e(AFTERCARE['subtitle']))}
    <div class="ac__grid">{blocks}</div>
    <div class="ac__rules">
      <article class="ac__rule ac__rule--do" data-reveal>
        <h3>{e(AFTERCARE['do_title'])}</h3>
        <ul class="ticks">{do}</ul>
      </article>
      <article class="ac__rule ac__rule--dont" data-reveal>
        <h3>{e(AFTERCARE['dont_title'])}</h3>
        <ul class="crosses">{dont}</ul>
      </article>
    </div>
    <p class="ac__note" data-reveal>{e(AFTERCARE['note'])}</p>
  </div>
</section>
"""


def faq():
    items = "".join(f"""
      <div class="faq__item" data-reveal>
        <button class="faq__q" aria-expanded="false">
          <span>{e(q)}</span><i aria-hidden="true"></i>
        </button>
        <div class="faq__a"><p>{e(a)}</p></div>
      </div>""" for q, a in FAQ["items"])
    return f"""
<section class="faq" id="faq">
  <div class="wrap wrap--narrow">
    {section_head(FAQ['eyebrow'], e(FAQ['title']))}
    <div class="faq__list">{items}</div>
  </div>
</section>
"""


def gallery():
    # Fora da página desde 25/09/26 (pedido do Eduardo). Para voltar: pôr
    # gallery() de novo na lista de seções em pagina() e o link no NAV.
    items = "".join(
        f'<div class="g__item g__item--{e(i["size"])}" data-reveal>'
        + img_slot(i["image"], i["caption"], ratio="auto", cls="g__media",
                   caption=i["caption"])
        + "</div>"
        for i in GALLERY["items"]
    )
    duo = " g__grid--duo" if len(GALLERY["items"]) <= 3 else ""
    ig = ""
    if CONTACT.get("instagram_url"):
        ig = (f'<a class="g__ig" href="{e(CONTACT["instagram_url"])}" '
              f'target="_blank" rel="noopener">{e(UI["instagram_more"])} '
              f'<span>{e(CONTACT["instagram_handle"])}</span></a>')
    return f"""
<section class="g" id="gallery">
  <div class="wrap">
    {section_head(GALLERY['eyebrow'], e(GALLERY['title']), e(GALLERY['subtitle']))}
    <div class="g__grid{duo}">{items}</div>
    {ig}
  </div>
</section>
"""


def testimonials():
    real = [t for t in TESTIMONIALS["items"] if t["quote"]]
    if real:
        cards = "".join(f"""
      <article class="t__card" data-reveal>
        <div class="t__stars" aria-label="{t['stars']} {e(UI['stars_of_five'])}">{'★' * t['stars']}</div>
        <blockquote class="t__quote">{e(t['quote'])}</blockquote>
        <p class="t__name">{e(t['name'])}</p>
        <p class="t__detail">{e(t['detail'])}</p>
      </article>""" for t in real)
    else:
        cards = "".join(f"""
      <article class="t__card t__card--empty" data-reveal>
        <div class="t__stars" aria-hidden="true">★★★★★</div>
        <blockquote class="t__quote editable">{e(UI["testimonial_slot"])}</blockquote>
        <p class="t__name editable">{e(UI["name_slot"])}</p>
        <p class="t__detail editable">{e(UI["service_slot"])}</p>
      </article>""" for _ in range(3))
    return f"""
<section class="t" id="testimonials">
  <div class="wrap">
    {section_head(TESTIMONIALS['eyebrow'], e(TESTIMONIALS['title']))}
    <div class="t__grid">{cards}</div>
  </div>
</section>
"""


def location():
    addr1 = (f'<p class="loc__addr">{e(LOCATION["address_line1"])}</p>'
             if LOCATION.get("address_line1")
             else f'<p class="loc__addr editable">{e(UI["address_slot"])}</p>')
    hours = "".join(
        f'<li><span>{e(d)}</span><span>{e(h)}</span></li>'
        for d, h in LOCATION["hours"]
    )
    if LOCATION.get("maps_embed"):
        map_html = (f'<div class="loc__map"><iframe src="{e(LOCATION["maps_embed"])}" '
                    f'loading="lazy" title="{e(UI["map_title"])}" referrerpolicy="no-referrer-when-downgrade" '
                    f'allowfullscreen></iframe></div>')
    else:
        map_html = ('<div class="loc__map loc__map--slot">'
                    '<span class="loc__mapmark" aria-hidden="true"></span>'
                    '<span class="loc__mapbrief">Map</span></div>')
    return f"""
<section class="loc" id="location">
  <div class="wrap loc__grid">
    <div class="loc__text" data-reveal>
      <p class="eyebrow">{e(LOCATION_SECTION['eyebrow'])}</p>
      <h2 class="loc__title">{LOCATION_SECTION['title']}</h2>
      {rule()}
      <p class="loc__name">{e(BRAND['name_full'])}</p>
      {addr1}
      <p class="loc__addr">{e(LOCATION['address_line2'])}</p>
      <p class="loc__note">{e(LOCATION['note'])}</p>
      <ul class="loc__hours">{hours}</ul>
      {btn(LOCATION_SECTION['cta'], LOCATION['maps_url'], 'ghost',
           'target="_blank" rel="noopener"')}
    </div>
    <div data-reveal>{map_html}</div>
  </div>
</section>
"""


def final_cta():
    contact_bits = []
    if CONTACT.get("phone_display"):
        contact_bits.append(
            f'<a href="tel:{e(CONTACT["phone_href"])}">{e(CONTACT["phone_display"])}</a>')
    if CONTACT.get("email"):
        contact_bits.append(
            f'<a href="mailto:{e(CONTACT["email"])}">{e(CONTACT["email"])}</a>')
    if CONTACT.get("instagram_url"):
        contact_bits.append(
            f'<a href="{e(CONTACT["instagram_url"])}" target="_blank" rel="noopener">'
            f'{e(CONTACT["instagram_handle"])}</a>')
    links = ('<div class="cta__links">' + "".join(contact_bits) + "</div>"
             if contact_bits else "")
    return f"""
<section class="cta" id="contact">
  <div class="wrap">
    <img src="/assets/logo/lasirene-mark-gold.png" alt="" class="cta__mark" data-reveal>
    <p class="eyebrow" data-reveal>{e(FINAL_CTA['eyebrow'])}</p>
    <h2 class="cta__title" data-reveal>{e(FINAL_CTA['title'])}</h2>
    <p class="cta__sub" data-reveal>{e(FINAL_CTA['subtitle'])}</p>
    <div class="cta__btn" data-reveal>{book_btn(CTA['primary'], 'primary')}</div>
    <p class="cta__contact" data-reveal>{e(FINAL_CTA['contact_line'])}</p>
    {links}
  </div>
</section>
"""


def footer():
    links = "".join(
        f'<li><a href="{e(h)}">{e(l)}</a></li>' for l, h in NAV
    )
    credit = FOOTER["credit"]
    if FOOTER.get("credit_url"):
        credit = (f'<a href="{e(FOOTER["credit_url"])}" target="_blank" '
                  f'rel="noopener">{e(FOOTER["credit"])}</a>')
    else:
        credit = e(credit)
    return f"""
<footer class="foot">
  <div class="wrap foot__grid">
    <div class="foot__brand">
      <img src="/assets/logo/lasirene-full-black.png" alt="{e(BRAND['name_full'])}" class="foot__logo">
      <p class="foot__note">{e(FOOTER['note'])}</p>
    </div>
    <nav class="foot__nav" aria-label="{e(UI['footer_label'])}"><ul>{links}</ul></nav>
    <div class="foot__contact">
      <p>{e(BRAND['city'])}, {e(BRAND['state'])}</p>
      <a href="{e(CONTACT['instagram_url'])}" target="_blank" rel="noopener">{e(CONTACT['instagram_handle'])}</a>
    </div>
  </div>
  <div class="wrap foot__bottom">
    <p>&copy; <span id="yr"></span> {e(BRAND['name_full'])}. {e(UI['rights'])}</p>
    <p>{credit}</p>
  </div>
</footer>

<a class="fab" href="{BOOK}" {BOOK_ATTRS}>{icone_zap("fab__zap") if e_whatsapp(BOOK) else ""}<span>{e(CTA['primary_short'])}</span></a>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------

def pagina():
    """Monta o HTML da página no idioma que está carregado."""
    return "".join([
        head(), navbar(), hero(), concept(), services(),
        # spray() e uv() saíram em 25/09/26
        brazilian(), moon(), combos(), shop(), finder(), how(),
        prep(), aftercare(), faq(), testimonials(), location(),
        final_cta(), footer(),
    ])


def build():
    # O idioma principal fica na raiz; os outros em pastas próprias.
    for idioma in IDIOMAS:
        carregar_idioma(idioma)
        destino = (ROOT / "index.html" if idioma == IDIOMAS[0]
                   else ROOT / idioma / "index.html")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(versionar_assets(pagina()), encoding="utf-8")
        rel = destino.relative_to(ROOT)
        print(f"✓ {str(rel):16s} {NOME_IDIOMA[idioma]}  "
              f"{destino.stat().st_size:,} bytes")

    # os avisos saem uma vez, no idioma principal
    carregar_idioma(IDIOMAS[0])

    # avisos úteis
    missing = []
    if not CONTACT.get("booking_url"):
        missing.append("link de agendamento (CONTACT['booking_url'])")
    if not CONTACT.get("whatsapp"):
        missing.append("WhatsApp (CONTACT['whatsapp'])")
    if not LOCATION.get("address_line1"):
        missing.append("endereço (LOCATION['address_line1'])")
    if not any(t["quote"] for t in TESTIMONIALS["items"]):
        missing.append("depoimentos reais (TESTIMONIALS)")
    no_photo = sum(1 for s in SERVICES if not s["image"])
    no_photo += sum(1 for g in GALLERY["items"] if not g["image"])
    if not HERO.get("image"):
        no_photo += 1
    if no_photo:
        missing.append(f"{no_photo} fotos (slots ainda vazios)")
    if missing:
        print("\n  Ainda falta preencher em content/site.py:")
        for m in missing:
            print(f"   · {m}")
    if SEO.get("noindex"):
        print("\n  ⚠ noindex LIGADO — o Google não vai indexar. "
              "Desligue em SEO['noindex'] quando for publicar.")


if __name__ == "__main__":
    build()
