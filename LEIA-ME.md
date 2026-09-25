# La Sirene Tanning — site

Site institucional da **La Sirene Tanning** (Tampa, Florida).
HTML/CSS/JS puro, sem npm, sem framework.

O site sai em **três idiomas**, porque o público da La Sirene em Tampa é
principalmente latino:

| Idioma | Endereço |
|---|---|
| Espanhol (principal) | `/` — a raiz do site |
| Português | `/pt` |
| Inglês | `/en` |

Quem abre o link cai no **espanhol**. No topo, cada idioma tem a sua
**bandeira** — 🇪🇸 Espanha, 🇧🇷 Brasil, 🇺🇸 Estados Unidos — e é só clicar
para trocar. No computador aparece só a bandeira (o menu é longo e não
cabem as letras); no celular aparece bandeira **e** as letras ES · PT · EN.
A bandeira do idioma em que você já está fica acesa, com um fio dourado
embaixo.

---

## Como ver o site

No Terminal, dentro desta pasta:

```
python3 tools/serve.py
```

Ele abre sozinho em `http://localhost:6040`. Para parar, `Ctrl+C`.

---

## Como mudar QUALQUER texto, preço ou foto

Você só precisa mexer em **um arquivo**: `content/site.py`.

Pense nele como o "painel de controle" do site. Tudo que a dona pode
querer trocar está lá dentro, separado por seções e com comentários
em português.

Depois de editar, rode:

```
python3 tools/build.py
```

Isso reescreve as três páginas: `index.html`, `pt/index.html` e
`en/index.html`.

> ⚠️ **Nunca edite os `index.html` na mão.** Eles são gerados e sua
> edição some no próximo build.

### Como o texto fica nos três idiomas

Todo texto que a visitante lê está escrito três vezes, lado a lado:

```python
"title": {
    "es": "El Arte del Bronceado Perfecto.",
    "pt": "A Arte do Bronzeado Perfeito.",
    "en": "The Art of the Perfect Glow.",
},
```

Para trocar uma frase, troque nos três. **Se esquecer de um, o build
para e diz exatamente onde** — é de propósito, para nenhuma página ir ao
ar com um pedaço no idioma errado:

```
✗ Tradução incompleta em CTA → primary_short: falta pt.
```

O que **não** leva idioma: nome de arquivo de foto, link, telefone,
número e as chaves que começam com `image` ou `id`.

### Exemplo — colocar um preço

Abra `content/site.py`, procure o serviço em `SERVICES` e escreva o
valor como texto:

```python
"price": "",     →     "price": "$210",
```

Preço é número, então **não** leva os três idiomas. Enquanto estiver
vazio, o site mostra "Precio disponible al reservar" (e a versão
equivalente em cada idioma).

Salve, rode `python3 tools/build.py`. Pronto.

### Exemplo — mudar uma foto

1. Coloque o arquivo novo em `assets/img/` (ex.: `hero.jpg`).
2. Em `content/site.py`, escreva o nome do arquivo no campo `"image"`.
3. Rode `python3 tools/build.py`.

Se quiser que o corte seja feito automaticamente, ponha a foto original
em `assets/img/_source/`, ajuste a linha correspondente em
`tools/prep_images.py` e rode `python3 tools/prep_images.py`.

### Exemplo — trocar as fotos da primeira dobra

A primeira dobra hoje são **duas fotos** que se alternam sozinhas, em
fusão suave, em laço. (Antes era um vídeo; ele continua guardado.)

1. Ponha as fotos novas em `assets/img/_source/`.
2. Em `tools/prep_images.py`, troque o nome do arquivo nas linhas
   `hero-a.jpg` e `hero-b.jpg`.
3. Rode `python3 tools/prep_images.py` e depois `python3 tools/build.py`.

Quer **três** fotos em vez de duas? Em `content/site.py` → `HERO`, a
lista aceita quantas você quiser:

```python
"images": ["hero-a.jpg", "hero-b.jpg", "hero-c.jpg"],
```

Se a foto ficar mal enquadrada (cortando a cabeça ou sobrando chão),
ajuste no mesmo `HERO`:

```python
"focus": "26%",          # desktop — 0% é o topo da foto, 100% o pé
"focus_mobile": "22%",   # celular
```

Para **voltar ao vídeo**, deixe `HERO["images"]` como lista vazia (`[]`)
e escreva de volta `"video": "hero.mp4"`. Os arquivos do vídeo continuam
em `assets/video/`, e o `tools/prep_video.py` continua funcionando.

### Se a imagem vier com texto escrito nela

Imagens geradas por IA costumam chegar com legendas desenhadas na
própria foto, e o site tem três idiomas — texto dentro da imagem não
tem como traduzir.

Quando o texto está na borda, dá para cortar fora: ajuste o ponto focal
daquela linha em `tools/prep_images.py` (foi o caso da foto do jato, que
tinha "BRONZEAMENTO A JATO" na coluna da direita).

Quando o texto atravessa o assunto, não há corte que resolva. **Peça a
imagem sem nenhum texto.**

Se deixar o campo `"image"` **vazio**, o site mostra um espaço reservado
elegante (sereia dourada + legenda do que vai ali). Isso é proposital:
nunca fica um buraco feio.

---

## O que ainda falta preencher

O build avisa a cada execução. Hoje falta:

| O quê | Onde em `content/site.py` |
|---|---|
| Link do sistema de agendamento | `CONTACT["booking_url"]` |
| WhatsApp | `CONTACT["whatsapp"]` — **é o que liga o ícone do WhatsApp nos botões** |
| Telefone / SMS / e-mail | `CONTACT` |
| Endereço da rua | `LOCATION["address_line1"]` |
| Mapa do Google | `LOCATION["maps_embed"]` |
| Horários reais | `LOCATION["hours"]` |
| Depoimentos reais | `TESTIMONIALS` |
| Preços dos bronzeamentos e combos | `SERVICES`, `COMBOS` |
| Domínio próprio | `SEO["canonical"]` |
| Orientações de preparo e aftercare | `SPRAY`, `PREP`, `AFTERCARE` |

**Enquanto `booking_url` e `whatsapp` estiverem vazios, todos os botões
de agendamento levam para o Instagram.** Isso é de propósito — nenhum
botão fica quebrado.

No site, os campos que a profissional ainda vai preencher aparecem em
itálico cinza com um tracinho pontilhado embaixo ("Tu orientación aquí").

---

## Preços

**Nenhum serviço tem preço no site ainda.** Todos mostram "Precio
disponible al reservar" porque não havia valor nenhum no material
enviado — não inventei nada.

Para colocar: `SERVICES` (cada serviço) e `COMBOS`, no campo `"price"`.

> Os preços de extensão de cílios que existiam aqui foram **removidos em
> 21/09/2026**, junto com a seção inteira: a La Sirene não faz cílios.

---

## Antes de publicar — 3 coisas obrigatórias

1. **Autorização das fotos.**
   As fotos de resultado são de clientes reais e identificáveis. Peça
   autorização por escrito de cada pessoa antes de colocar no ar.

2. **Desligar o `noindex`.**
   Em `content/site.py`, `SEO["noindex"]` está `True` — o Google é
   instruído a **não** indexar. Troque para `False` só quando o site
   estiver aprovado, e rode o build de novo.

3. **Conferir o `.vercelignore`.**
   A pasta `assets/img/_source/` tem as fotos **originais, sem corte**.
   O `.vercelignore` impede que elas subam. Não remova essa linha.

---

## Animações e acabamento

O site tem uma camada de movimento própria. Se em algum momento você
quiser diminuir ou tirar, tudo está no fim do `assets/css/style.css`,
no bloco **CAMADA PREMIUM**.

**O que acontece:**

- **Abertura** — a sereia dourada aparece e a tela sobe. Só na primeira
  vez de cada sessão; se a cliente navegar entre seções, não repete.
- **Títulos em 3D** — cada palavra gira para cima, uma depois da outra.
  Quem faz a divisão é o `main.js`; no HTML o texto continua inteiro,
  então dá para selecionar, copiar e o Google lê normalmente.
- **Cortina nas fotos** — a foto é revelada de baixo para cima enquanto
  dá um leve zoom-out.
- **Fios dourados** — as linhas se desenham da esquerda para a direita.
- **Cards** — inclinam de leve acompanhando o mouse, e o texto flutua um
  pouco à frente. No celular isso é desligado (atrapalharia o scroll).
- **Grão de filme** — uma textura muito sutil sobre a página e dentro das
  fotos. É o que tira o aspecto de "imagem de tela" e dá cara de
  fotografia impressa.

**Ajustes rápidos:**

| Quero... | Onde |
|---|---|
| Títulos entrando mais devagar/rápido | `.split .wi` → `transition` |
| Cascata entre palavras mais lenta | `.split .wi` → `54ms` |
| Menos inclinação nos cards | `main.js` → `TILT_MAX` (hoje 5 graus) |
| Menos grão | `.grain` e `.media::before` → `opacity` |
| Tirar a abertura | apagar o bloco `.intro` do `tools/build.py` |

Quem prefere menos movimento no sistema (acessibilidade) recebe o site
sem nenhuma animação, automaticamente.

**O fundo do site inteiro é a foto do pôr do sol na praia.** Ela fica
parada atrás de tudo (não rola junto), e cada seção é um **véu de areia
translúcido** por cima dela — é assim que a praia aparece sem deixar
nenhum texto ilegível. As seções ainda alternam entre dois tons de véu,
que é o que dá profundidade conforme você rola.

Para clarear ou escurecer o site inteiro, mexa só em duas linhas no
começo do `assets/css/style.css` — o último número de cada uma é a
opacidade do véu:

```css
--sand:rgba(232,223,210,.74);     /* seções principais */
--sand-2:rgba(220,208,190,.69);   /* seções alternadas */
```

- **Quer ver MAIS praia?** baixe os números (`.74` → `.66`).
- **Quer ler MELHOR?** suba os números (`.74` → `.84`).

Para trocar a foto do fundo: ponha o arquivo novo em
`assets/img/_source/`, aponte para ele na linha `bg-sunset.jpg` do
`tools/prep_images.py` e rode o script. Essa foto passa por um
tratamento próprio (clareada e levemente desfocada) justamente para
poder ficar atrás de texto.

Existe também um `--gold-ink` separado do `--gold`: o dourado claro
some sobre areia quando é texto pequeno, então os rótulos usam um
dourado mais fechado e os fios e bordas continuam com o claro.

**Tratamento do vídeo:** o `tools/prep_video.py` amplia o arquivo (o
original do celular é pequeno), aplica o mesmo acabamento das fotos e
monta um laço "vai e volta" — o vídeo roda para frente e depois de
volta, então o loop não tem corte seco. O celular baixa uma versão leve
(`hero-sm.mp4`, ~0,8 MB) e o desktop a grande (`hero.mp4`, ~3,4 MB);
nunca os dois. Quem pediu "menos animação" no sistema vê só o primeiro
quadro, parado.

**Tratamento das fotos:** o `tools/prep_images.py` aplica curva de
contraste, calor nos meios-tons, vinheta e nitidez, e gera duas versões
de cada foto — a grande e uma leve (`-sm.jpg`) que o celular baixa no
lugar. Se trocar uma foto, rode o script para ela receber o mesmo
tratamento.

---

## Estrutura da pasta

```
content/site.py        ← TODO o conteúdo, nos três idiomas (mexa aqui)
tools/build.py         ← gera as três páginas
tools/prep_images.py   ← corta e otimiza as fotos
tools/prep_video.py    ← trata o vídeo da primeira dobra
tools/serve.py         ← servidor local
assets/css/style.css   ← visual
assets/js/main.js      ← menu, FAQ, animações
assets/logo/           ← logo em preto, dourado e branco (PNG transparente)
assets/img/            ← fotos já cortadas e usadas no site
assets/img/_source/    ← fotos originais (não vão para o ar)
assets/video/          ← vídeo do hero, já tratado
assets/video/_source/  ← vídeo original (não vai para o ar)
index.html             ← GERADO (espanhol) — não edite
pt/index.html          ← GERADO (português) — não edite
en/index.html          ← GERADO (inglês) — não edite
```

---

## O que o site tem

Navbar fixa com troca de idioma (com bandeira) · hero em duas fotos que se
alternam, sobre o fundo de pôr do sol · conceito da marca ·
menu de 5 serviços · Brazilian Tan com comparação fita × biquíni de tecido ·
Spray Tan em 5 etapas · UV Tan com estilos de marquinha · Banho de Lua
Classic e Premium · combos · "qual bronze é para mim" · o que esperar do
atendimento · guia de preparação · aftercare (Do / Don't) · FAQ em
accordion · galeria editorial · depoimentos · localização · CTA final ·
rodapé · botão flutuante de agendar no celular. Todo botão que leva para o
WhatsApp mostra o desenho do WhatsApp — ele aparece sozinho assim que o
número estiver preenchido em `CONTACT["whatsapp"]`.

SEO local pronto: title, meta description, headings semânticos e dados
estruturados (`BeautySalon`) para Tampa/FL.

Sobre saúde e segurança o site **não afirma nada** — nem tempo de
exposição, nem duração do bronze, nem contraindicação. Tudo isso remete
à orientação pessoal da profissional, como pedido.
