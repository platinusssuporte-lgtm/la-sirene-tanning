# -*- coding: utf-8 -*-
"""
LA SIRENE TANNING — arquivo único de conteúdo.

TUDO que a proprietária pode querer trocar está neste arquivo:
textos, preços, fotos, depoimentos, FAQ, horários, links.

Depois de editar, rode:      python3 tools/build.py
Isso regenera as três páginas.  NÃO edite os index.html na mão.


OS TRÊS IDIOMAS
---------------
O site sai em espanhol (a raiz), português (/pt) e inglês (/en), porque o
público da La Sirene em Tampa é principalmente latino.

Todo texto que o visitante lê está escrito nos três idiomas de uma vez:

    "title": {
        "es": "El Arte del Bronceado Perfecto.",
        "pt": "A Arte do Bronzeado Perfeito.",
        "en": "The Art of the Perfect Glow.",
    }

Para trocar uma frase, troque nos três. Se esquecer de um, o build PARA e
diz exatamente onde — é de propósito, para nenhuma página ir ao ar com um
pedaço no idioma errado.

O que NÃO leva idioma: nomes de arquivo de foto, links, números, telefone,
e as chaves que começam com "image" ou "id".

Onde estiver escrito  "A DEFINIR"  é informação que ainda não temos e que a
proprietária precisa preencher.
"""

# ---------------------------------------------------------------------------
# 1. MARCA E CONTATO
# ---------------------------------------------------------------------------

BRAND = {
    "name": "La Sirene",
    "name_full": "La Sirene Tanning",
    "tagline": "Brazilian Tanning",
    "city": "Tampa",
    "state": "Florida",
    "state_short": "FL",
}

CONTACT = {
    # Coloque o número no formato internacional, só dígitos, para o WhatsApp.
    # Ex.: 1 + DDD + número  ->  "18135550199"
    # Este número é +1 (813) 679-7327 — é ele que acende o ícone do WhatsApp
    # em todos os botões de agendamento.
    "whatsapp": "18136797327",
    "whatsapp_message": {
        "es": "¡Hola! Me gustaría reservar una cita en La Sirene Tanning.",
        "pt": "Olá! Gostaria de agendar um horário na La Sirene Tanning.",
        "en": "Hi! I'd like to book an appointment at La Sirene Tanning.",
    },
    "phone_display": "",                 # A DEFINIR — ex.: "(813) 555-0199"
    "phone_href": "",                    # A DEFINIR — ex.: "+18135550199"
    "sms_href": "",                      # A DEFINIR — ex.: "+18135550199"
    "email": "",                         # A DEFINIR
    "instagram_handle": "@lasirene_tampa",
    "instagram_url": "https://www.instagram.com/lasirene_tampa",
    # Link do sistema de agendamento (GlossGenius, Square, Booksy, Vagaro...).
    # Enquanto estiver vazio, todos os botões BOOK caem no Instagram.
    "booking_url": "",                   # A DEFINIR
}

LOCATION = {
    "address_line1": "",                 # A DEFINIR — rua e número
    "address_line2": "Tampa, Florida",
    "maps_url": "https://www.google.com/maps/search/?api=1&query=La+Sirene+Tanning+Tampa+FL",
    # Cole aqui o src do iframe do Google Maps quando tiver o endereço exato.
    "maps_embed": "",                    # A DEFINIR
    "note": {
        "es": "Solo con cita previa.",
        "pt": "Somente com horário marcado.",
        "en": "By appointment only.",
    },
    "hours": [
        # (dia, horário) — A DEFINIR, estes são exemplos neutros
        (
            {"es": "Lunes — Viernes", "pt": "Segunda — Sexta", "en": "Monday — Friday"},
            {"es": "Con cita previa", "pt": "Com horário marcado", "en": "By appointment"},
        ),
        (
            {"es": "Sábado", "pt": "Sábado", "en": "Saturday"},
            {"es": "Con cita previa", "pt": "Com horário marcado", "en": "By appointment"},
        ),
        (
            {"es": "Domingo", "pt": "Domingo", "en": "Sunday"},
            {"es": "Cerrado", "pt": "Fechado", "en": "Closed"},
        ),
    ],
}

SEO = {
    # Rótulos que o visitante não lê — quem lê é o leitor de tela.
    "language_label": {"es": "Idioma", "pt": "Idioma", "en": "Language"},
    "nav_label": {
        "es": "Navegación principal",
        "pt": "Navegação principal",
        "en": "Main navigation",
    },
    "menu_label": {"es": "Abrir el menú", "pt": "Abrir o menu", "en": "Open menu"},

    "title": {
        "es": "La Sirene Tanning | Bronceado brasileño y Baño de Luna en Tampa, FL",
        "pt": "La Sirene Tanning | Bronzeamento brasileiro e Banho de Lua em Tampa, FL",
        "en": "La Sirene Tanning | Brazilian Tan, Banho de Lua & Boutique in Tampa, FL",
    },
    "description": {
        "es": (
            "Estudio de bronceado brasileño de lujo en Tampa, Florida. Bronceado "
            "brasileño con cinta o con bikini de tela, Baño de Luna, exfoliación "
            "profesional e hidratación, además de moda de playa, productos para el "
            "cuerpo y accesorios. Reserva tu cita en La Sirene Tanning."
        ),
        "pt": (
            "Estúdio de bronzeamento brasileiro de luxo em Tampa, Florida. "
            "Bronzeamento brasileiro com fita ou com biquíni de tecido, Banho de "
            "Lua, esfoliação profissional e hidratação, além de moda praia, produtos "
            "para o corpo e acessórios. Agende seu horário na La Sirene Tanning."
        ),
        "en": (
            "Luxury Brazilian tanning studio in Tampa, Florida. Custom Brazilian tan "
            "with tape or a fabric bikini, Banho de Lua, professional exfoliation "
            "and hydration, plus beachwear, body products and accessories. Book your "
            "appointment at La Sirene Tanning."
        ),
    },
    "keywords": {
        "es": (
            "bronceado brasileño Tampa, bronceado Tampa FL, bronceado con cinta Tampa, "
            "exfoliación Tampa, marquitas bronceado Tampa, baño de luna Tampa, "
            "bronceado de lujo Tampa, salón de bronceado Tampa"
        ),
        "pt": (
            "bronzeamento brasileiro Tampa, bronzeamento Tampa FL, bronzeamento com "
            "fita Tampa, esfoliação Tampa, marquinha Tampa, banho de lua Tampa, "
            "bronzeamento de luxo Tampa, estúdio de bronzeamento Tampa"
        ),
        "en": (
            "Brazilian Tan Tampa, Brazilian Tanning Tampa FL, Tape Tan Tampa, "
            "Exfoliation Tampa, Brazilian Tan near Tampa, Body Glow Tampa, "
            "Moon Bath Tampa, Luxury Tanning Tampa, Tanning Salon Tampa"
        ),
    },
    # Enquanto o site não estiver aprovado para publicação, deixe True.
    # True = pede ao Google para NÃO indexar o site.
    "noindex": True,
    # Endereço oficial do site. É o que faz o Google entender que a raiz, o
    # /pt e o /en são a mesma página em três idiomas (as tags hreflang só
    # saem quando este campo está preenchido).
    # TROCAR pelo domínio próprio quando ele existir.
    "canonical": "https://la-sirene-tanning.vercel.app",
}

# ---------------------------------------------------------------------------
# 2. TEXTOS CURTOS DA INTERFACE
# ---------------------------------------------------------------------------
#
# Frases soltas que aparecem nos botões e nos espaços ainda sem conteúdo.

UI = {
    "price_on_booking": {
        "es": "Precio disponible al reservar",
        "pt": "Preço disponível na reserva",
        "en": "Price available upon booking",
    },
    "learn_more": {"es": "Saber más", "pt": "Saiba mais", "en": "Learn More"},
    "photo_slot": {"es": "Fotografía", "pt": "Fotografia", "en": "Photography"},
    "guidance_slot": {
        "es": "Tu orientación aquí",
        "pt": "Sua orientação aqui",
        "en": "Your guidance here",
    },
    "testimonial_slot": {
        "es": "Testimonio de clienta",
        "pt": "Depoimento de cliente",
        "en": "Client testimonial",
    },
    "name_slot": {"es": "Nombre", "pt": "Nome", "en": "Client name"},
    "service_slot": {"es": "Servicio", "pt": "Serviço", "en": "Service"},
    "address_slot": {"es": "Dirección", "pt": "Endereço", "en": "Street address"},
    "map_title": {"es": "Mapa", "pt": "Mapa", "en": "Map"},
    "services_eyebrow": {
        "es": "Nuestros servicios", "pt": "Nossos serviços", "en": "Our Services",
    },
    "services_title": {
        "es": "El Menú La Sirene", "pt": "O Menu La Sirene", "en": "The La Sirene Menu",
    },
    "services_subtitle": {
        "es": "Cada servicio se construye alrededor del resultado que quieres.",
        "pt": "Cada serviço é construído em torno do resultado que você quer.",
        "en": "Each service is built around the result you want.",
    },
    "instagram_more": {
        "es": "Ver más en Instagram", "pt": "Ver mais no Instagram",
        "en": "See more on Instagram",
    },
    "rights": {
        "es": "Todos los derechos reservados.",
        "pt": "Todos os direitos reservados.",
        "en": "All rights reserved.",
    },
    "stars_of_five": {"es": "de 5", "pt": "de 5", "en": "out of 5"},
    "scroll_hint": {
        "es": "Ir al contenido", "pt": "Ir para o conteúdo", "en": "Scroll to content",
    },
    "footer_label": {"es": "Pie de página", "pt": "Rodapé", "en": "Footer"},
}

# ---------------------------------------------------------------------------
# 3. NAVEGAÇÃO
# ---------------------------------------------------------------------------

NAV = [
    # "Início" saiu em 25/09/26 para caber a Boutique — o logo já leva ao topo.
    ({"es": "Servicios", "pt": "Serviços", "en": "Services"}, "#services"),
    ({"es": "Boutique", "pt": "Boutique", "en": "Boutique"}, "#boutique"),
    ({"es": "Cómo funciona", "pt": "Como funciona", "en": "How It Works"}, "#how-it-works"),
    ({"es": "Cuidados", "pt": "Cuidados", "en": "Aftercare"}, "#aftercare"),
    ({"es": "Preguntas", "pt": "Dúvidas", "en": "FAQ"}, "#faq"),
    # Galeria saiu do site em 25/09/26 — o link "#gallery" saiu junto.
    ({"es": "Contacto", "pt": "Contato", "en": "Contact"}, "#contact"),
]

CTA = {
    "primary": {
        "es": "Reserva tu cita",
        "pt": "Agende seu horário",
        "en": "Book Your Appointment",
    },
    "primary_short": {"es": "Reservar", "pt": "Agendar", "en": "Book Now"},
    "secondary": {
        "es": "Ver nuestros servicios",
        "pt": "Ver nossos serviços",
        "en": "Explore Our Services",
    },
}

# ---------------------------------------------------------------------------
# 4. HERO
# ---------------------------------------------------------------------------

HERO = {
    "eyebrow": {"es": "Tampa, Florida", "pt": "Tampa, Florida", "en": "Tampa, Florida"},
    "title": {
        "es": "El Arte del<br>Bronceado Perfecto.",
        "pt": "A Arte do<br>Bronzeado Perfeito.",
        "en": "The Art of<br>the Perfect Glow.",
    },
    "services_line": [
        {"es": "Bronceado Brasileño", "pt": "Bronzeamento Brasileiro", "en": "Brazilian Tan"},
        {"es": "Baño de Luna", "pt": "Banho de Lua", "en": "Banho de Lua"},
        {"es": "Exfoliación", "pt": "Esfoliação", "en": "Exfoliation"},
        {"es": "Hidratación", "pt": "Hidratação", "en": "Hydration"},
    ],
    "quote": {
        "es": (
            "Un bronceado pensado para ti — creado para realzar tu belleza natural "
            "y dejar tu piel con ese brillo irresistible."
        ),
        "pt": (
            "Um bronzeado pensado para você — criado para realçar sua beleza natural "
            "e deixar a pele com aquele brilho irresistível."
        ),
        "en": (
            "A tan designed around you — created to enhance your natural beauty "
            "and leave your skin with that irresistible glow."
        ),
    },
    # AS DUAS FOTOS da primeira dobra (entraram no lugar do vídeo em 22/09/26).
    # Elas se alternam sozinhas, em fusão suave, em laço. Para voltar ao vídeo
    # basta esvaziar esta lista e preencher "video" de novo.
    # Ordem = ordem de exibição. Arquivos gerados por tools/prep_images.py.
    "images": ["hero-a.jpg"],   # desde 25/09/26 = foto da tesoura e da fita (model3)

    # VÍDEO da primeira dobra. Só é usado quando "images" está VAZIA.
    # Quando preenchido, o hero toca o vídeo (sem som, em laço) e usa "poster"
    # como primeiro quadro — que é o que aparece no celular economizando dados
    # e para quem pediu "menos animação" no sistema.
    # Os arquivos são gerados por tools/prep_video.py.
    "video": "",
    "video_small": "hero-sm.mp4",
    "poster": "hero-poster.jpg",
    # Enquadramento do vídeo/foto dentro da coluna: 0% = topo, 100% = pé.
    # Nas fotos novas o rosto está na parte de cima, por isso um valor baixo.
    "focus": "26%",
    "focus_mobile": "22%",

    # Foto de fundo da primeira dobra. Coloque o arquivo em assets/img/
    # e escreva aqui só o nome, ex.: "hero.jpg". Vazio = slot desenhado.
    # Usada quando "video" está vazio.
    "image": "hero.jpg",
    "image_brief": {
        "es": "Retrato editorial — piel dorada, luz cálida",
        "pt": "Retrato editorial — pele dourada, luz quente",
        "en": "Editorial portrait — golden skin, warm light",
    },
}

# ---------------------------------------------------------------------------
# 5. CONCEITO
# ---------------------------------------------------------------------------

CONCEPT = {
    "eyebrow": {
        "es": "El concepto La Sirene",
        "pt": "O conceito La Sirene",
        "en": "The La Sirene Concept",
    },
    "title": {
        "es": "Más Que un Bronceado.<br>Es una Experiencia.",
        "pt": "Mais Que um Bronzeado.<br>É uma Experiência.",
        "en": "More Than a Tan.<br>It's an Experience.",
    },
    "body": [
        {
            "es": (
                "En La Sirene Tanning, cada cita está pensada para crear mucho más "
                "que un bronceado bonito. Creamos una experiencia personalizada en "
                "la que cada detalle — desde preparar la piel hasta diseñar el "
                "bronceado — se cuida para favorecer el cuerpo y entregar el "
                "resultado que cada clienta busca."
            ),
            "pt": (
                "Na La Sirene Tanning, cada horário é pensado para criar muito mais "
                "do que um bronzeado bonito. Criamos uma experiência personalizada "
                "em que cada detalhe — do preparo da pele ao desenho do bronzeado — "
                "é cuidado para favorecer o corpo e entregar o resultado que cada "
                "cliente procura."
            ),
            "en": (
                "At La Sirene Tanning, every appointment is designed to create more "
                "than a beautiful tan. We create a personalized experience where "
                "every detail — from preparing the skin to designing the tan itself "
                "— is considered to flatter the body and deliver the result each "
                "client is looking for."
            ),
        },
        # Os dois parágrafos abaixo são o texto da própria dona (25/09/26).
        {
            "es": (
                "Nuestra máquina de bronceado es operada bajo la supervisión de una "
                "profesional, que acompaña todo el procedimiento. Moldeamos el "
                "bikini de tiras para todo tipo de cuerpo, y también puede hacerse "
                "con un bikini de nuestra propia tela, para un efecto más natural. "
                "El bronceado es gradual: se intensifica en cada sesión hasta "
                "llegar al color ideal para ti."
            ),
            "pt": (
                "Nossa máquina de bronzeamento é operada sob a supervisão de uma "
                "profissional, que acompanha todo o procedimento. Moldamos o "
                "biquíni de alças para todos os tipos de corpo, e ele também pode "
                "ser feito com um biquíni do nosso próprio tecido, para um efeito "
                "mais natural. O bronzeado é gradual: vai se intensificando a cada "
                "sessão, até chegar à cor ideal para você."
            ),
            "en": (
                "Our tanning machine is operated under the supervision of a "
                "professional who stays with you through the whole procedure. We "
                "shape the strap bikini for every body type, and it can also be "
                "done with a bikini made from our own fabric for a more natural "
                "effect. The tan is gradual, deepening with every session until it "
                "reaches the ideal color for you."
            ),
        },
        {
            "es": (
                "Los resultados ya se ven desde la primera sesión. Puedes necesitar "
                "una o más sesiones, según qué tan bronceada quieras quedar."
            ),
            "pt": (
                "Os resultados já aparecem desde a primeira sessão. Você pode "
                "precisar de uma ou mais sessões, dependendo de quão bronzeada "
                "quer ficar."
            ),
            "en": (
                "You'll see results from the very first session. You may need one "
                "or more sessions, depending on how deep you'd like your tan."
            ),
        },
    ],
    "pillars": [
        {"es": "Personalizado", "pt": "Personalizado", "en": "Customized"},
        {"es": "Femenino", "pt": "Feminino", "en": "Feminine"},
        {"es": "Natural", "pt": "Natural", "en": "Natural"},
        {"es": "De lujo", "pt": "Luxuoso", "en": "Luxurious"},
    ],
    "image": "concept.jpg",
    "image_brief": {
        "es": "Editorial vertical — piel bronceada, brillo natural",
        "pt": "Editorial vertical — pele bronzeada, brilho natural",
        "en": "Vertical editorial — bronzed skin, natural glow",
    },
}

# ---------------------------------------------------------------------------
# 6. SERVIÇOS DE BRONZEAMENTO (catálogo)
# ---------------------------------------------------------------------------
#
# price: escreva o valor como texto, ex.: "$190".
#        Deixe "" para mostrar "Precio disponible al reservar".
#
# Os nomes dos serviços são o menu da casa e ficam iguais nos três idiomas
# quando já são nome próprio (Spray Tan, Banho de Lua). O que muda é a
# explicação.

# 25/09/26: a lista segue EXATAMENTE os serviços que a dona mandou. Saíram o
# Bronzeamento a Jato (ela não faz) e o UV como serviço separado (o bronzeado
# é todo na máquina, com fita ou com biquíni de tecido). "target" = para onde
# o card leva; sem ele, vai para "#id".
SERVICES = [
    {
        "id": "tape-tan",
        "index": "01",
        "target": "#brazilian-tan",
        "name": {
            "es": 'Bronceado Brasileño<br>con Cinta',
            "pt": 'Bronzeamento Brasileiro<br>com Fita',
            "en": 'Brazilian Tan<br>with Tape',
        },
        "name_plain": {
            "es": 'Bronceado Brasileño con Cinta',
            "pt": 'Bronzeamento Brasileiro com Fita',
            "en": 'Brazilian Tan with Tape',
        },
        "subtitle": {
            "es": 'Tu marca, diseñada a medida.',
            "pt": 'Sua marquinha, desenhada sob medida.',
            "en": 'Your tan lines, custom designed.',
        },
        "price": "",
        "short": {
            "es": 'Moldeamos las tiras con cinta para tu cuerpo — grosor, forma y posición exactamente como quieras.',
            "pt": 'Moldamos as alças com fita para o seu corpo — espessura, formato e posição do jeito que você quiser.',
            "en": 'We shape the straps with tape for your body — width, shape and placement exactly the way you want.',
        },
        "image": "svc-tape.jpg",
        "image_brief": {
            "es": 'Tijera y cinta — el diseño de la marca',
            "pt": 'Tesoura e fita — o desenho da marquinha',
            "en": 'Scissors and tape — designing the tan lines',
        },
    },
    {
        "id": "fabric-tan",
        "index": "02",
        "target": "#brazilian-tan",
        "name": {
            "es": 'Bronceado Brasileño<br>con Bikini de Tela',
            "pt": 'Bronzeamento Brasileiro<br>com Biquíni de Tecido',
            "en": 'Brazilian Tan<br>with Fabric Bikini',
        },
        "name_plain": {
            "es": 'Bronceado Brasileño con Bikini de Tela',
            "pt": 'Bronzeamento Brasileiro com Biquíni de Tecido',
            "en": 'Brazilian Tan with Fabric Bikini',
        },
        "subtitle": {
            "es": 'Un acabado más natural.',
            "pt": 'Um acabamento mais natural.',
            "en": 'A more natural finish.',
        },
        "price": "",
        "short": {
            "es": 'Hecho con un bikini de nuestra propia tela, para bordes más suaves y un efecto natural.',
            "pt": 'Feito com um biquíni do nosso próprio tecido, para bordas mais suaves e um efeito natural.',
            "en": 'Done with a bikini made from our own fabric, for softer edges and a natural effect.',
        },
        "image": "svc-fabric.jpg",
        "image_brief": {
            "es": 'Marca brasileña — piel dorada',
            "pt": 'Marquinha brasileira — pele dourada',
            "en": 'Brazilian tan lines — golden skin',
        },
    },
    {
        "id": "banho-de-lua-classic",
        "index": "03",
        "name": {
            "es": 'Baño<br>de Luna',
            "pt": 'Banho<br>de Lua',
            "en": 'Banho<br>de Lua',
        },
        "name_plain": {
            "es": 'Baño de Luna',
            "pt": 'Banho de Lua',
            "en": 'Banho de Lua',
        },
        "subtitle": {
            "es": 'El ritual corporal clásico.',
            "pt": 'O ritual corporal clássico.',
            "en": 'The classic body ritual.',
        },
        "price": "",
        "short": {
            "es": 'Un ritual corporal creado para aclarar el vello, limpiar la piel y retirar células muertas — dejando la piel uniforme, limpia y lista para el bronceado.',
            "pt": 'Um ritual corporal criado para clarear os pelos, limpar a pele e remover células mortas — deixando a pele uniforme, limpa e pronta para o bronzeado.',
            "en": 'A body ritual created to lighten body hair, cleanse the skin and remove dead cells — leaving skin even, clean and ready for a tan.',
        },
        "image": "svc-moon-classic.jpg",
        "image_brief": {
            "es": 'El ritual — producto trabajado sobre la piel',
            "pt": 'O ritual — produto trabalhado na pele',
            "en": 'Banho de Lua ritual — product worked into the skin',
        },
    },
    {
        "id": "banho-de-lua-premium",
        "index": "04",
        "name": {
            "es": 'Baño de Luna<br>Premium',
            "pt": 'Banho de Lua<br>Premium',
            "en": 'Banho de Lua<br>Premium',
        },
        "name_plain": {
            "es": 'Baño de Luna Premium',
            "pt": 'Banho de Lua Premium',
            "en": 'Banho de Lua Premium',
        },
        "subtitle": {
            "es": 'El ritual completo de luminosidad.',
            "pt": 'O ritual completo de luminosidade.',
            "en": 'A complete body glow ritual.',
        },
        "price": "",
        "short": {
            "es": 'Una experiencia completa de cuidado corporal que une aclarado del vello, renovación de la piel, hidratación y luminosidad.',
            "pt": 'Uma experiência completa de cuidado corporal que une clareamento dos pelos, renovação da pele, hidratação e luminosidade.',
            "en": 'A complete body care experience combining hair lightening, skin renewal, hydration and luminosity.',
        },
        "image": "svc-moon-premium.jpg",
        "image_brief": {
            "es": 'Ritual premium — hidratación y luminosidad',
            "pt": 'Ritual premium — hidratação e luminosidade',
            "en": 'Premium ritual — hydration and luminosity',
        },
        "featured": True,
    },
    {
        "id": "exfoliation",
        "index": "05",
        "target": "#combos",
        "name": {
            "es": 'Exfoliación<br>Profesional',
            "pt": 'Esfoliação<br>Profissional',
            "en": 'Professional<br>Exfoliation',
        },
        "name_plain": {
            "es": 'Exfoliación Profesional',
            "pt": 'Esfoliação Profissional',
            "en": 'Professional Exfoliation',
        },
        "subtitle": {
            "es": 'Piel renovada y lista.',
            "pt": 'Pele renovada e pronta.',
            "en": 'Renewed, ready skin.',
        },
        "price": "",
        "short": {
            "es": 'Retira las células muertas y deja la piel suave y uniforme — la mejor base para un bronceado parejo.',
            "pt": 'Remove as células mortas e deixa a pele macia e uniforme — a melhor base para um bronzeado por igual.',
            "en": 'Removes dead cells and leaves skin soft and even — the best base for an even tan.',
        },
        "image": "svc-exfol.jpg",
        "image_brief": {
            "es": 'Exfoliante natural sobre la piel',
            "pt": 'Esfoliante natural na pele',
            "en": 'Natural scrub on the skin',
        },
    },
    {
        "id": "hydration",
        "index": "06",
        "target": "#aftercare",
        "name": {
            "es": 'Hidratación',
            "pt": 'Hidratação',
            "en": 'Hydration',
        },
        "name_plain": {
            "es": 'Hidratación',
            "pt": 'Hidratação',
            "en": 'Hydration',
        },
        "subtitle": {
            "es": 'Suavidad y brillo.',
            "pt": 'Maciez e brilho.',
            "en": 'Softness and glow.',
        },
        "price": "",
        "short": {
            "es": 'Hidratación profunda para una piel suave y luminosa, que ayuda a mantener tu bronceado bonito por más tiempo.',
            "pt": 'Hidratação profunda para uma pele macia e luminosa, que ajuda a manter o seu bronzeado bonito por mais tempo.',
            "en": 'Deep hydration for soft, luminous skin that helps keep your tan beautiful for longer.',
        },
        "image": "svc-hydra.jpg",
        "image_brief": {
            "es": 'Hidratación — crema trabajada sobre la piel',
            "pt": 'Hidratação — creme trabalhado na pele',
            "en": 'Hydration — cream worked into the skin',
        },
    },
]

# ---------------------------------------------------------------------------
# 7. BRONZEAMENTO BRASILEIRO — seção detalhada
# ---------------------------------------------------------------------------

BRAZILIAN = {
    "eyebrow": {"es": "Servicios 01 · 02", "pt": "Serviços 01 · 02", "en": "Services 01 · 02"},
    "title": {
        "es": "La Sirene<br>Bronceado Brasileño",
        "pt": "La Sirene<br>Bronzeamento Brasileiro",
        "en": "La Sirene<br>Brazilian Tan",
    },
    "subtitle": {
        "es": "El brillo brasileño de la casa.",
        "pt": "O brilho brasileiro da casa.",
        "en": "The signature Brazilian glow.",
    },
    "body": {
        "es": (
            "El Bronceado Brasileño es una experiencia personalizada en la que "
            "diseñamos tus marcas según el bikini que quieras. Con la cinta podemos "
            "crear líneas hechas a medida, que favorecen el cuerpo y dan un "
            "resultado que es solo tuyo."
        ),
        "pt": (
            "O Bronzeamento Brasileiro é uma experiência personalizada em que "
            "desenhamos sua marquinha conforme o biquíni que você quer. Com a fita "
            "dá para criar linhas sob medida, que favorecem o corpo e entregam um "
            "resultado que é só seu."
        ),
        "en": (
            "The Brazilian Tan is a personalized tanning experience where we design "
            "your tan according to the bikini style you want. Applying tape lets us "
            "create custom lines that flatter the body and produce a result that is "
            "entirely your own."
        ),
    },
    "highlight": {
        "es": "Tu Bronceado. Tu Diseño.",
        "pt": "Seu Bronzeado. Seu Desenho.",
        "en": "Your Tan. Your Design.",
    },
    "choices_title": {"es": "Tú eliges", "pt": "Você escolhe", "en": "You choose"},
    "choices": [
        (
            {"es": "Grosor", "pt": "Espessura", "en": "Width"},
            {
                "es": "Qué tan finas o anchas quedan tus marcas.",
                "pt": "Quão finas ou largas ficam suas marquinhas.",
                "en": "How thin or wide your tan lines sit.",
            },
        ),
        (
            {"es": "Forma", "pt": "Formato", "en": "Shape"},
            {
                "es": "El corte y la curva del diseño.",
                "pt": "O corte e a curva do desenho.",
                "en": "The cut and curve of the design.",
            },
        ),
        (
            {"es": "Posición", "pt": "Posição", "en": "Placement"},
            {
                "es": "Exactamente dónde caen las líneas en tu cuerpo.",
                "pt": "Exatamente onde as linhas caem no seu corpo.",
                "en": "Exactly where the lines fall on your body.",
            },
        ),
        (
            {"es": "Modelo de bikini", "pt": "Modelo de biquíni", "en": "Bikini style"},
            {
                "es": "La silueta que quieres recrear.",
                "pt": "A silhueta que você quer recriar.",
                "en": "The silhouette you want to recreate.",
            },
        ),
    ],
    "compare_title": {
        "es": "Dos maneras de llevarlo",
        "pt": "Duas formas de usar",
        "en": "Two ways to wear it",
    },
    "compare": [
        {
            "name": {"es": "Con cinta", "pt": "Com fita", "en": "Tape Tan"},
            "lead": {
                "es": "Líneas totalmente personalizadas.",
                "pt": "Linhas totalmente personalizadas.",
                "en": "Fully customized lines.",
            },
            "desc": {
                "es": (
                    "La cinta se aplica para dibujar el diseño exacto que quieres, "
                    "así las líneas quedan justo donde las elijas."
                ),
                "pt": (
                    "A fita é aplicada para desenhar exatamente o que você quer, "
                    "então as linhas ficam no lugar exato que você escolher."
                ),
                "en": (
                    "Tape is applied to draw the exact design you want, so the "
                    "lines are placed precisely where you choose."
                ),
            },
            "points": [
                {
                    "es": "Grosor y forma a medida",
                    "pt": "Espessura e formato sob medida",
                    "en": "Custom width and shape",
                },
                {"es": "Posición precisa", "pt": "Posição precisa", "en": "Precise placement"},
                {
                    "es": "Líneas nítidas y definidas",
                    "pt": "Linhas nítidas e definidas",
                    "en": "Sharp, defined lines",
                },
            ],
            "image": "",   # 25/09/26: comparação só com texto
            "image_brief": {
                "es": "Diseño con cinta sobre la piel",
                "pt": "Desenho com fita na pele",
                "en": "Tape design applied on skin",
            },
        },
        {
            "name": {
                "es": "Con bikini de tela",
                "pt": "Com biquíni de tecido",
                "en": "Fabric Bikini Tan",
            },
            "lead": {
                "es": "Un acabado más suave y natural.",
                "pt": "Um acabamento mais suave e natural.",
                "en": "A softer, natural finish.",
            },
            "desc": {
                "es": (
                    "Para quien prefiere un resultado más natural, usando un bikini "
                    "de tela."
                ),
                "pt": (
                    "Para quem prefere um resultado mais natural, usando um biquíni "
                    "de tecido."
                ),
                "en": (
                    "For clients who prefer a more natural result using a fabric "
                    "bikini."
                ),
            },
            "points": [
                {"es": "Bordes más suaves", "pt": "Bordas mais suaves", "en": "Softer edges"},
                {
                    "es": "El formato del bikini que ya conoces",
                    "pt": "O formato do biquíni que você já conhece",
                    "en": "Familiar bikini shape",
                },
                {
                    "es": "Acabado de aspecto natural",
                    "pt": "Acabamento de aspecto natural",
                    "en": "Natural-looking finish",
                },
            ],
            "image": "",
            "image_brief": {
                "es": "Resultado con bikini de tela",
                "pt": "Resultado com biquíni de tecido",
                "en": "Fabric bikini tan result",
            },
        },
    ],
    # Veio da antiga seção UV em 25/09/26.
    # Dois caminhos de bronzeado: o gradual (o indicado para o dia a dia) e o
    # neon de primeira sessão (para ocasiões especiais). O texto do neon é
    # honesto sem assustar: diz que é mais intenso e pede mais da pele, por
    # isso fica reservado para datas pontuais. NÃO prometer "pele saudável"
    # nem dizer que não faz mal — só comparar os dois ritmos.
    "paths_title": {
        "es": "Dos caminos hacia tu bronceado",
        "pt": "Dois caminhos para o seu bronzeado",
        "en": "Two paths to your tan",
    },
    "paths_intro": {
        "es": "Te ayudamos a elegir el ritmo ideal para tu piel y tu momento.",
        "pt": "A gente te ajuda a escolher o ritmo ideal para a sua pele e o seu momento.",
        "en": "We'll help you choose the right pace for your skin and your moment.",
    },
    "paths": [
        {
            "tag": {"es": "Recomendado", "pt": "O mais indicado", "en": "Our recommendation"},
            "name": {"es": "Bronceado gradual", "pt": "Bronze gradual", "en": "Gradual tan"},
            "lead": {
                "es": "El color se construye sesión a sesión.",
                "pt": "A cor vai sendo construída sessão a sessão.",
                "en": "Color is built up session by session.",
            },
            "body": {
                "es": (
                    "Respeta el tiempo de tu piel: se broncea poco a poco, se mantiene "
                    "hidratada y cuidada, y el color queda más uniforme y dura más. "
                    "Es el camino que recomendamos para quien quiere lucir un bronceado "
                    "bonito todo el año."
                ),
                "pt": (
                    "Respeita o tempo da sua pele: ela vai se bronzeando aos poucos, "
                    "continua hidratada e bem cuidada, e a cor fica mais uniforme e "
                    "dura mais. É o caminho que a gente indica para quem quer um "
                    "bronzeado bonito o ano inteiro."
                ),
                "en": (
                    "It respects your skin's natural pace: it tans little by little, "
                    "stays hydrated and cared for, and the color comes out more even "
                    "and lasts longer. It's the path we recommend for a beautiful "
                    "glow all year round."
                ),
            },
        },
        {
            "tag": {"es": "Ocasiones especiales", "pt": "Datas especiais", "en": "Special occasions"},
            "name": {"es": "Bronceado neón", "pt": "Bronze neon", "en": "Neon tan"},
            "lead": {
                "es": "Color intenso desde la primera sesión.",
                "pt": "Cor intensa já na primeira sessão.",
                "en": "Intense color from the very first session.",
            },
            "body": {
                "es": (
                    "Pensado para eventos, viajes y fechas especiales, cuando quieres "
                    "llegar con el bronceado listo. Como es un proceso más intenso y "
                    "le pide más a tu piel, lo reservamos para esos momentos puntuales "
                    "— y en el día a día, el gradual es el mejor aliado."
                ),
                "pt": (
                    "Pensado para eventos, viagens e datas especiais, quando você quer "
                    "chegar com o bronzeado pronto. Por ser um processo mais intenso, "
                    "que exige mais da pele, a gente reserva para esses momentos "
                    "pontuais — e no dia a dia, o gradual é o seu melhor aliado."
                ),
                "en": (
                    "Designed for events, trips and special dates, when you want to "
                    "arrive with your tan ready. Because it's a more intense process "
                    "that asks more of your skin, we save it for those special "
                    "moments — for everyday, gradual is your best ally."
                ),
            },
        },
    ],
    # Espaço reservado para a profissional inserir as orientações dela.
    # O site NÃO faz afirmações sobre segurança ou tempo de exposição.
    "guidance_title": {
        "es": "Orientación de la sesión",
        "pt": "Orientação da sessão",
        "en": "Session guidance",
    },
    "guidance_body": {
        "es": (
            "Los detalles y la orientación de la sesión te los da personalmente "
            "nuestra profesional en tu consulta."
        ),
        "pt": (
            "Os detalhes e a orientação da sessão são passados pessoalmente pela "
            "nossa profissional na sua consulta."
        ),
        "en": (
            "Session details and guidance are provided personally by our "
            "professional during your consultation."
        ),
    },
}

# ---------------------------------------------------------------------------
# 8. BRONZEAMENTO A JATO
# ---------------------------------------------------------------------------

SPRAY = {
    "eyebrow": {"es": "Servicio 02", "pt": "Serviço 02", "en": "Service 02"},
    "title": {
        "es": "Bronceado en Spray",
        "pt": "Bronzeamento a Jato",
        "en": "Spray Tanning",
    },
    "subtitle": {
        "es": "Un dorado impecable.",
        "pt": "Um dourado impecável.",
        "en": "A flawless golden glow.",
    },
    "body": {
        "es": (
            "Un bronceado uniforme y sofisticado para quien quiere piel dorada sin "
            "exposición al sol."
        ),
        "pt": (
            "Um bronzeado uniforme e sofisticado para quem quer pele dourada sem "
            "exposição ao sol."
        ),
        "en": (
            "An even, sophisticated tan for those who want golden skin without "
            "sun exposure."
        ),
    },
    "steps": [
        (
            "01",
            {"es": "Preparación de la piel", "pt": "Preparo da pele", "en": "Skin Preparation"},
            {
                "es": "Preparamos la piel para que el color se asiente uniforme.",
                "pt": "Preparamos a pele para a cor assentar por igual.",
                "en": "We prepare the skin so the colour settles evenly.",
            },
        ),
        (
            "02",
            {"es": "Elección del tono", "pt": "Escolha do tom", "en": "Choosing Your Shade"},
            {
                "es": "Elegimos el tono juntas, según el resultado que quieras.",
                "pt": "Escolhemos o tom juntas, conforme o resultado que você quer.",
                "en": "We select the tone together, based on the result you want.",
            },
        ),
        (
            "03",
            {"es": "Aplicación", "pt": "Aplicação", "en": "Application"},
            {
                "es": "El bronceado se aplica con atención al contorno y al acabado.",
                "pt": "O bronzeado é aplicado com atenção ao contorno e ao acabamento.",
                "en": "The tan is applied with attention to contour and finish.",
            },
        ),
        (
            "04",
            {"es": "Revelado", "pt": "Revelação", "en": "Development"},
            {
                "es": "El color se revela sobre la piel.",
                "pt": "A cor se revela na pele.",
                "en": "The colour develops on the skin.",
            },
        ),
        (
            "05",
            {"es": "Cuidados", "pt": "Cuidados", "en": "Aftercare"},
            {
                "es": "Te explicamos cómo cuidar tu brillo.",
                "pt": "Explicamos como cuidar do seu brilho.",
                "en": "We walk you through how to care for your glow.",
            },
        ),
    ],
    "before_title": {
        "es": "Antes de tu cita",
        "pt": "Antes do seu horário",
        "en": "Before Your Appointment",
    },
    "before_intro": {
        "es": "Algunas cosas que ayudan a que tu bronceado quede lindo.",
        "pt": "Algumas coisas que ajudam seu bronzeado a ficar bonito.",
        "en": "A few things that help your tan turn out beautifully.",
    },
    # Orientações editáveis — a profissional preenche com as instruções dela.
    "before_items": [
        {
            "es": "Llega con la piel limpia, sin productos pesados.",
            "pt": "Chegue com a pele limpa, sem produtos pesados.",
            "en": "Arrive with clean skin, free of heavy products.",
        },
        {
            "es": "Ven con ropa holgada y cómoda.",
            "pt": "Venha com roupa larga e confortável.",
            "en": "Wear loose, comfortable clothing to your appointment.",
        },
        {
            "es": "Trae el bikini o la prenda que quieras usar en la sesión.",
            "pt": "Traga o biquíni ou a peça que quiser usar na sessão.",
            "en": "Bring the bikini or garment you'd like to wear during the session.",
        },
        "",  # espaço editável para a profissional
    ],
}

# ---------------------------------------------------------------------------
# 9. BRONZEAMENTO UV
# ---------------------------------------------------------------------------

UV = {
    "eyebrow": {"es": "Servicio 03", "pt": "Serviço 03", "en": "Service 03"},
    "title": {"es": "Bronceado UV", "pt": "Bronzeamento UV", "en": "UV Tan"},
    "subtitle": {
        "es": "Tu bronceado. A tu manera.",
        "pt": "Seu bronzeado. Do seu jeito.",
        "en": "Your tan. Your way.",
    },
    "body": {
        "es": (
            "Bronceado UV con la opción de diseñar tus propias marcas con cinta, "
            "según tu preferencia."
        ),
        "pt": (
            "Bronzeamento UV com a opção de desenhar sua própria marquinha com "
            "fita, conforme sua preferência."
        ),
        "en": (
            "UV tanning with the option of designing your own tan lines using tape, "
            "according to your preference."
        ),
    },
    "styles_title": {
        "es": "Estilos de marca",
        "pt": "Estilos de marquinha",
        "en": "Tan line styles",
    },
    "styles_intro": {
        "es": "Un punto de partida — el diseño final lo definimos juntas.",
        "pt": "Um ponto de partida — o desenho final a gente define junto.",
        "en": "A starting point — we'll shape the final design together.",
    },
    "styles": [
        (
            {"es": "Brasileña", "pt": "Brasileira", "en": "Brazilian"},
            {
                "es": "La marca brasileña alta, a marca da casa.",
                "pt": "A marquinha brasileira alta, a marca da casa.",
                "en": "The signature high-cut Brazilian line.",
            },
        ),
        (
            {"es": "Recta", "pt": "Reta", "en": "Straight"},
            {
                "es": "Una línea horizontal limpia y recta.",
                "pt": "Uma linha horizontal limpa e reta.",
                "en": "A clean, straight horizontal line.",
            },
        ),
        (
            {"es": "Fina", "pt": "Fina", "en": "Thin"},
            {
                "es": "Líneas delicadas, casi imperceptibles.",
                "pt": "Linhas delicadas, quase imperceptíveis.",
                "en": "Delicate, barely-there lines.",
            },
        ),
        (
            {"es": "Ancha", "pt": "Larga", "en": "Wide"},
            {
                "es": "Un diseño más amplio y marcado.",
                "pt": "Um desenho mais amplo e marcado.",
                "en": "A broader, more pronounced design.",
            },
        ),
        (
            {"es": "A medida", "pt": "Sob medida", "en": "Custom"},
            {
                "es": "Lo que quieras crear con nosotras.",
                "pt": "O que você quiser criar com a gente.",
                "en": "Anything you'd like to create with us.",
            },
        ),
    ],

}

# ---------------------------------------------------------------------------
# 10. BANHO DE LUA
# ---------------------------------------------------------------------------

MOON_CLASSIC = {
    "eyebrow": {"es": "Servicio 03", "pt": "Serviço 03", "en": "Service 03"},
    "title": {
        "es": "Baño<br>de Luna",
        "pt": "Banho<br>de Lua",
        "en": "Banho<br>de Lua",
    },
    "subtitle": {
        "es": "El ritual corporal clásico.",
        "pt": "O ritual corporal clássico.",
        "en": "The classic body ritual.",
    },
    "body": {
        "es": (
            "Un ritual corporal creado para aclarar el vello, limpiar la piel y "
            "retirar células muertas — dejando la piel más uniforme, limpia y "
            "preparada para recibir el bronceado."
        ),
        "pt": (
            "Um ritual corporal criado para clarear os pelos, limpar a pele e "
            "remover células mortas — deixando a pele mais uniforme, limpa e "
            "preparada para receber o bronzeado."
        ),
        "en": (
            "A body ritual created to lighten body hair, cleanse the skin and "
            "remove dead cells — leaving the skin more even, clean and prepared to "
            "receive a tan."
        ),
    },
    "timeline": [
        (
            "01",
            {"es": "Preparación", "pt": "Preparo", "en": "Preparation"},
            {
                "es": "Se limpia y se prepara la piel.",
                "pt": "A pele é limpa e preparada.",
                "en": "The skin is cleansed and prepared.",
            },
        ),
        (
            "02",
            {"es": "Aclarado del vello", "pt": "Clareamento dos pelos", "en": "Hair Lightening"},
            {
                "es": "Se aclara el vello del cuerpo.",
                "pt": "Os pelos do corpo são clareados.",
                "en": "Body hair is lightened.",
            },
        ),
        (
            "03",
            {"es": "Exfoliación", "pt": "Esfoliação", "en": "Exfoliation"},
            {
                "es": "Se retiran las células muertas.",
                "pt": "As células mortas são removidas.",
                "en": "Dead cells are removed.",
            },
        ),
        (
            "04",
            {"es": "Limpieza de la piel", "pt": "Limpeza da pele", "en": "Skin Cleansing"},
            {
                "es": "La piel se limpia a fondo.",
                "pt": "A pele é limpa a fundo.",
                "en": "The skin is thoroughly cleansed.",
            },
        ),
        (
            "05",
            {"es": "Acabado", "pt": "Finalização", "en": "Finishing"},
            {
                "es": "Cuidado final y últimos detalles.",
                "pt": "Cuidado final e últimos detalhes.",
                "en": "Final care and finishing touches.",
            },
        ),
    ],
}

MOON_PREMIUM = {
    "eyebrow": {"es": "Servicio 04", "pt": "Serviço 04", "en": "Service 04"},
    "title": {
        "es": "Baño de Luna<br>Premium",
        "pt": "Banho de Lua<br>Premium",
        "en": "Banho de Lua<br>Premium",
    },
    "subtitle": {
        "es": "El ritual completo de luminosidad.",
        "pt": "O ritual completo de luminosidade.",
        "en": "A complete body glow ritual.",
    },
    "body": {
        "es": (
            "Una experiencia completa de cuidado corporal que une aclarado del "
            "vello, renovación de la piel, hidratación y luminosidad."
        ),
        "pt": (
            "Uma experiência completa de cuidado corporal que une clareamento dos "
            "pelos, renovação da pele, hidratação e luminosidade."
        ),
        "en": (
            "A complete body care experience combining hair lightening, skin "
            "renewal, hydration and luminosity."
        ),
    },
    "pillars": [
        (
            {"es": "Renovar", "pt": "Renovar", "en": "Renew"},
            {
                "es": "Renovación y alisado de la piel.",
                "pt": "Renovação e alisamento da pele.",
                "en": "Skin renewal and resurfacing.",
            },
        ),
        (
            {"es": "Hidratar", "pt": "Hidratar", "en": "Hydrate"},
            {
                "es": "Hidratación profunda y duradera.",
                "pt": "Hidratação profunda e duradoura.",
                "en": "Deep, lasting hydration.",
            },
        ),
        (
            {"es": "Brillar", "pt": "Brilhar", "en": "Glow"},
            {
                "es": "Luminosidad desde el primer toque.",
                "pt": "Luminosidade desde o primeiro toque.",
                "en": "Luminosity from the first touch.",
            },
        ),
        (
            {"es": "Suavidad", "pt": "Suavidade", "en": "Softness"},
            {
                "es": "Un acabado más suave y liso.",
                "pt": "Um acabamento mais suave e liso.",
                "en": "A softer, smoother finish.",
            },
        ),
    ],
    "closing": {
        "es": (
            "Ideal para quien no quiere solo preparar la piel, sino convertir todo "
            "el ritual en una experiencia de cuidado y luminosidad."
        ),
        "pt": (
            "Ideal para quem não quer só preparar a pele, mas transformar todo o "
            "ritual em uma experiência de cuidado e luminosidade."
        ),
        "en": (
            "Ideal for anyone who wants not just to prepare the skin, but to turn "
            "the whole ritual into an experience of care and luminosity."
        ),
    },
}

# ---------------------------------------------------------------------------
# 11. COMBOS
# ---------------------------------------------------------------------------

COMBOS = {
    "eyebrow": {"es": "Combinaciones", "pt": "Combinações", "en": "Combinations"},
    "title": {
        "es": "La Combinación Perfecta",
        "pt": "A Combinação Perfeita",
        "en": "The Perfect Combination",
    },
    "subtitle": {
        "es": "Preparar, renovar y terminar — en una sola visita.",
        "pt": "Preparar, renovar e finalizar — em uma só visita.",
        "en": "Prepare, renew and finish — in one visit.",
    },
    "items": [
        {
            "name": {
                "es": "Baño de Luna + Bronceado",
                "pt": "Banho de Lua + Bronzeado",
                "en": "Moon Bath + Tan",
            },
            "price": "",
            "desc": {
                "es": (
                    "Prepara tu piel, renueva su textura y termina con un bronceado "
                    "personalizado."
                ),
                "pt": (
                    "Prepare sua pele, renove a textura e finalize com um bronzeado "
                    "personalizado."
                ),
                "en": (
                    "Prepare your skin, renew its texture and finish with a "
                    "personalized tan."
                ),
            },
        },
        {
            "name": {
                "es": "Exfoliación + Bronceado",
                "pt": "Esfoliação + Bronzeado",
                "en": "Exfoliation + Tan",
            },
            "price": "",
            "desc": {
                "es": (
                    "Una preparación completa para dejar la piel uniforme y lista "
                    "para recibir el bronceado."
                ),
                "pt": (
                    "Um preparo completo para deixar a pele uniforme e pronta para "
                    "receber o bronzeado."
                ),
                "en": (
                    "A complete preparation to leave the skin even and ready to "
                    "receive a tan."
                ),
            },
        },
    ],
}

# ---------------------------------------------------------------------------
# BOUTIQUE — o que a dona vende no estúdio (25/09/26)
# ---------------------------------------------------------------------------
# Sem preço e sem foto por enquanto: cada card leva ao WhatsApp. Quando houver
# fotos dos produtos, dá para acrescentar "image" em cada item.

SHOP = {
    "eyebrow": {"es": "Boutique", "pt": "Boutique", "en": "Boutique"},
    "title": {
        "es": "Llévate el Brillo<br>a Casa",
        "pt": "Leve o Brilho<br>para Casa",
        "en": "Take the Glow<br>Home",
    },
    "subtitle": {
        "es": "En el estudio también encuentras todo para completar tu look de verano.",
        "pt": "No estúdio você também encontra tudo para completar o seu look de verão.",
        "en": "At the studio you'll also find everything to complete your summer look.",
    },
    "items": [
        {
            "icon": "bikini",
            "name": {"es": "Moda de Playa", "pt": "Moda Praia", "en": "Beachwear"},
            "desc": {
                "es": "Bikinis y piezas de playa elegidas para lucir tu bronceado.",
                "pt": "Biquínis e peças de praia escolhidas para valorizar o seu bronzeado.",
                "en": "Bikinis and beach pieces picked to show off your tan.",
            },
        },
        {
            "icon": "frasco",
            "name": {
                "es": "Productos para el Cuerpo",
                "pt": "Produtos para o Corpo",
                "en": "Body Products",
            },
            "desc": {
                "es": "Cuidados para mantener la piel hidratada y el bronceado bonito por más tiempo.",
                "pt": "Cuidados para manter a pele hidratada e o bronzeado bonito por mais tempo.",
                "en": "Care products to keep your skin hydrated and your tan beautiful for longer.",
            },
        },
        {
            "icon": "joia",
            "name": {"es": "Accesorios", "pt": "Acessórios", "en": "Accessories"},
            "desc": {
                "es": "Los detalles que completan tu look, del estudio a la playa.",
                "pt": "Os detalhes que completam o seu look, do estúdio à praia.",
                "en": "The finishing touches for your look, from the studio to the beach.",
            },
        },
    ],
    "cta": {"es": "Consultar", "pt": "Consultar", "en": "Ask us"},
    "note": {
        "es": "Disponibles en el estudio. Pregúntanos por modelos, tallas y novedades.",
        "pt": "Disponíveis no estúdio. Pergunte pelos modelos, tamanhos e novidades.",
        "en": "Available at the studio. Ask us about styles, sizes and what's new.",
    },
}

# ---------------------------------------------------------------------------
# 12. "QUAL BRONZE É PARA MIM?"
# ---------------------------------------------------------------------------

FINDER = {
    "eyebrow": {"es": "Encuentra tu brillo", "pt": "Encontre seu brilho", "en": "Find Your Glow"},
    "title": {
        "es": "¿No Sabes Cuál Elegir?",
        "pt": "Não Sabe Qual Escolher?",
        "en": "Not Sure Which Tan to Choose?",
    },
    "subtitle": {
        "es": "Vamos a encontrar tu brillo perfecto.",
        "pt": "Vamos encontrar seu brilho perfeito.",
        "en": "Let's find your perfect glow.",
    },
    "options": [
        {
            "want": {
                "es": "Quiero marcas personalizadas",
                "pt": "Quero uma marquinha personalizada",
                "en": "I want custom tan lines",
            },
            "answer": {
                "es": "Bronceado Brasileño",
                "pt": "Bronzeamento Brasileiro",
                "en": "Brazilian Tan",
            },
            "target": "#brazilian-tan",
        },
        {
            "want": {
                "es": "Quiero la piel suave e hidratada",
                "pt": "Quero a pele macia e hidratada",
                "en": "I want soft, hydrated skin",
            },
            "answer": {
                "es": "Hidratación",
                "pt": "Hidratação",
                "en": "Hydration",
            },
            "target": "#services",
        },
        {
            "want": {
                "es": "Quiero diseñar mis propias marcas",
                "pt": "Quero criar minha própria marquinha",
                "en": "I want to design my own tan lines",
            },
            "answer": {
                "es": "Bronceado Brasileño con Cinta",
                "pt": "Bronzeamento Brasileiro com Fita",
                "en": "Brazilian Tan with Tape",
            },
            "target": "#brazilian-tan",
        },
        {
            "want": {
                "es": "Quiero algo más natural",
                "pt": "Quero algo mais natural",
                "en": "I want something more natural",
            },
            "answer": {
                "es": "Bronceado con bikini de tela",
                "pt": "Bronzeamento com biquíni de tecido",
                "en": "Fabric Bikini Tan",
            },
            "target": "#brazilian-tan",
        },
        {
            "want": {
                "es": "Quiero preparar y cuidar la piel antes",
                "pt": "Quero preparar e cuidar da pele antes",
                "en": "I want to prepare and care for my skin first",
            },
            "answer": {
                "es": "Baño de Luna / Exfoliación + Bronceado",
                "pt": "Banho de Lua / Esfoliação + Bronzeado",
                "en": "Moon Bath / Exfoliation + Tan",
            },
            "target": "#combos",
        },
    ],
}

# ---------------------------------------------------------------------------
# 13. COMO FUNCIONA O ATENDIMENTO
# ---------------------------------------------------------------------------

HOW = {
    "eyebrow": {"es": "Tu cita", "pt": "Seu horário", "en": "Your Appointment"},
    "title": {"es": "Qué Esperar", "pt": "O Que Esperar", "en": "What to Expect"},
    "subtitle": {
        "es": "Cada cita es individual, sin prisa y acompañada de principio a fin.",
        "pt": "Cada atendimento é individual, sem pressa e acompanhado do início ao fim.",
        "en": "Every appointment is individual, unhurried and guided from start to finish.",
    },
    "steps": [
        (
            "01",
            {"es": "Consulta", "pt": "Consulta", "en": "Consultation"},
            {
                "es": "Conversamos sobre el resultado que buscas.",
                "pt": "Conversamos sobre o resultado que você busca.",
                "en": "We talk through the result you're looking for.",
            },
        ),
        (
            "02",
            {"es": "Preparación de la piel", "pt": "Preparo da pele", "en": "Skin Preparation"},
            {
                "es": "Preparamos tu piel para el procedimiento.",
                "pt": "Preparamos sua pele para o procedimento.",
                "en": "We prepare your skin for the procedure.",
            },
        ),
        (
            "03",
            {"es": "Diseño a medida", "pt": "Desenho sob medida", "en": "Custom Design"},
            {
                "es": "Definimos el diseño de tus marcas, cuando corresponde.",
                "pt": "Definimos o desenho da sua marquinha, quando for o caso.",
                "en": "We define your tan line design, where applicable.",
            },
        ),
        (
            "04",
            {"es": "Aplicación", "pt": "Aplicação", "en": "Tan Application"},
            {
                "es": "Realizamos el tratamiento que elegiste.",
                "pt": "Realizamos o tratamento que você escolheu.",
                "en": "We carry out the treatment you've chosen.",
            },
        ),
        (
            "05",
            {"es": "Detalles finales", "pt": "Detalhes finais", "en": "Final Touches"},
            {
                "es": "Revisamos el resultado juntas y te damos tu orientación.",
                "pt": "Conferimos o resultado juntas e passamos sua orientação.",
                "en": "We check the result together and share your guidance.",
            },
        ),
    ],
}

# ---------------------------------------------------------------------------
# 14. GUIA DE PREPARAÇÃO
# ---------------------------------------------------------------------------

PREP = {
    "eyebrow": {
        "es": "Guía de preparación",
        "pt": "Guia de preparação",
        "en": "Your Tan Prep Guide",
    },
    "title": {
        "es": "Cómo Prepararte<br>para tu Cita",
        "pt": "Como se Preparar<br>para o seu Horário",
        "en": "How to Prepare<br>for Your Appointment",
    },
    "subtitle": {
        "es": "Un poco de preparación hace una diferencia que se nota.",
        "pt": "Um pouco de preparo faz uma diferença que se vê.",
        "en": "A little preparation makes a noticeable difference.",
    },
    # Todos os textos abaixo são editáveis pela profissional.
    "items": [
        (
            {"es": "48h antes", "pt": "48h antes", "en": "48h Before"},
            {
                "es": "Prepara y exfolia la piel.",
                "pt": "Prepare e esfolie a pele.",
                "en": "Prepare and exfoliate the skin.",
            },
        ),
        (
            {"es": "24h antes", "pt": "24h antes", "en": "24h Before"},
            {
                "es": "Depilación, si la necesitas.",
                "pt": "Depilação, se precisar.",
                "en": "Hair removal, if needed.",
            },
        ),
        (
            {"es": "El día de la cita", "pt": "No dia do horário", "en": "Day of Appointment"},
            {
                "es": "Ven con la piel bien limpia y, si es posible, exfoliada.",
                "pt": "Venha com a pele bem limpa e, se possível, esfoliada.",
                "en": "Come with very clean skin — exfoliated, if possible.",
            },
        ),
        (
            {"es": "Qué ponerte", "pt": "O que vestir", "en": "What to Wear"},
            {
                "es": "Ropa cómoda, para volver a casa tranquila después de la sesión.",
                "pt": "Roupa confortável, para voltar para casa tranquila depois da sessão.",
                "en": "Comfortable clothes, so you can head home at ease after your session.",
            },
        ),
    ],
    "note": {
        "es": (
            "Tu profesional te dirá los tiempos y los productos exactos para tu "
            "piel durante la consulta."
        ),
        "pt": (
            "Sua profissional vai passar os tempos e os produtos exatos para a sua "
            "pele durante a consulta."
        ),
        "en": (
            "Your professional will share the exact timing and products for your "
            "skin during your consultation."
        ),
    },
}

# ---------------------------------------------------------------------------
# 15. CUIDADOS DEPOIS
# ---------------------------------------------------------------------------

AFTERCARE = {
    "eyebrow": {"es": "Cuidados", "pt": "Cuidados", "en": "Aftercare"},
    "title": {
        "es": "Mantén tu Brillo Bonito.",
        "pt": "Mantenha seu Brilho Bonito.",
        "en": "Keep Your Glow Beautiful.",
    },
    "subtitle": {
        "es": "Cómo cuidas tu piel después define el resultado.",
        "pt": "Como você cuida da pele depois define o resultado.",
        "en": "How you care for your skin afterwards shapes the result.",
    },
    "blocks": [
        {
            "title": {
                "es": "Antes de tu primera ducha",
                "pt": "Antes do primeiro banho",
                "en": "Before Your First Shower",
            },
            "items": [
                {
                    "es": "Sigue la orientación que te dio tu profesional.",
                    "pt": "Siga a orientação que sua profissional passou.",
                    "en": "Follow the guidance given to you by your professional.",
                },
                "",  # campo editável
            ],
        },
        {
            "title": {
                "es": "Los primeros días",
                "pt": "Os primeiros dias",
                "en": "The First Days",
            },
            "items": [
                {
                    "es": "Mantén la piel hidratada como te indicaron.",
                    "pt": "Mantenha a pele hidratada como foi orientado.",
                    "en": "Keep the skin hydrated as instructed.",
                },
                "",  # campo editável
            ],
        },
        {
            "title": {
                "es": "Cómo mantener tu brillo",
                "pt": "Como manter seu brilho",
                "en": "How to Maintain Your Glow",
            },
            "items": [
                {
                    "es": "Usa los productos recomendados para tu piel.",
                    "pt": "Use os produtos recomendados para a sua pele.",
                    "en": "Use the products recommended for your skin.",
                },
                "",  # campo editável
            ],
        },
    ],
    "do_title": {"es": "Sí", "pt": "Faça", "en": "Do"},
    "do": [
        {
            "es": "Sigue la orientación de tu profesional.",
            "pt": "Siga a orientação da sua profissional.",
            "en": "Follow the guidance provided by your professional.",
        },
        {
            "es": "Mantén la piel hidratada como te indicaron.",
            "pt": "Mantenha a pele hidratada como foi orientado.",
            "en": "Keep your skin hydrated as instructed.",
        },
        {
            "es": "Usa productos adecuados.",
            "pt": "Use produtos adequados.",
            "en": "Use suitable products.",
        },
        "",  # campo editável
    ],
    "dont_title": {"es": "No", "pt": "Evite", "en": "Don't"},
    "dont": [
        {
            "es": "Saltarte los cuidados que te indicaron.",
            "pt": "Pular os cuidados que foram passados para você.",
            "en": "Skip the aftercare steps you were given.",
        },
        {
            "es": "Usar productos que no te fueron recomendados.",
            "pt": "Usar produtos que não foram recomendados para você.",
            "en": "Use products that weren't recommended for you.",
        },
        "",  # campo editável
    ],
    "note": {
        "es": (
            "Los tiempos, los productos y los cuidados específicos te los damos "
            "personalmente después de tu cita."
        ),
        "pt": (
            "Os tempos, os produtos e os cuidados específicos são passados "
            "pessoalmente para você depois do atendimento."
        ),
        "en": (
            "Specific timings, products and care are given to you personally after "
            "your appointment."
        ),
    },
}

# ---------------------------------------------------------------------------
# 16. DÚVIDAS FREQUENTES
# ---------------------------------------------------------------------------

FAQ = {
    "eyebrow": {"es": "Preguntas", "pt": "Dúvidas", "en": "Questions"},
    "title": {
        "es": "Preguntas Frecuentes",
        "pt": "Perguntas Frequentes",
        "en": "Frequently Asked Questions",
    },
    "items": [
        (
            {
                "es": "¿Tengo que preparar la piel antes del bronceado?",
                "pt": "Preciso preparar a pele antes do bronzeado?",
                "en": "Do I need to prepare my skin before my tan?",
            },
            {
                "es": (
                    "Sí — la preparación hace una diferencia real en el resultado. "
                    "Arriba tienes nuestra guía general, y tu profesional te "
                    "confirmará los pasos exactos para tu piel en la consulta."
                ),
                "pt": (
                    "Sim — o preparo faz uma diferença real no resultado. Acima "
                    "está nosso guia geral, e sua profissional confirma os passos "
                    "exatos para a sua pele na consulta."
                ),
                "en": (
                    "Yes — preparation makes a real difference to the result. "
                    "You'll find our general prep guide above, and your "
                    "professional will confirm the exact steps for your skin "
                    "during your consultation."
                ),
            },
        ),
        (
            {
                "es": "¿Puedo elegir la forma de mis marcas?",
                "pt": "Posso escolher o formato da minha marquinha?",
                "en": "Can I choose the shape of my tan lines?",
            },
            {
                "es": (
                    "Claro que sí. Ese es el corazón del Bronceado Brasileño de La "
                    "Sirene. Tú eliges el grosor, la forma y la posición, y "
                    "diseñamos las líneas contigo antes de empezar."
                ),
                "pt": (
                    "Com certeza. Esse é o coração do Bronzeamento Brasileiro da La "
                    "Sirene. Você escolhe a espessura, o formato e a posição, e a "
                    "gente desenha as linhas com você antes de começar."
                ),
                "en": (
                    "Absolutely. That's the heart of the La Sirene Brazilian Tan. "
                    "You choose the width, shape and placement, and we design the "
                    "lines with you before we begin."
                ),
            },
        ),
        (
            {
                "es": "¿Puedo usar bikini de tela en vez de cinta?",
                "pt": "Posso usar biquíni de tecido em vez de fita?",
                "en": "Can I use a fabric bikini instead of tape?",
            },
            {
                "es": (
                    "Sí. Ofrecemos el Bronceado Brasileño con bikini de tela para "
                    "quien prefiere un acabado más suave y natural."
                ),
                "pt": (
                    "Sim. Oferecemos o Bronzeamento Brasileiro com biquíni de "
                    "tecido para quem prefere um acabamento mais suave e natural."
                ),
                "en": (
                    "Yes. We offer the Brazilian Tan with a fabric bikini for "
                    "clients who prefer a softer, more natural finish."
                ),
            },
        ),
        (
            {
                "es": "¿Cuántas sesiones necesito?",
                "pt": "Quantas sessões eu preciso?",
                "en": "How many sessions do I need?",
            },
            {
                "es": (
                    "Los resultados ya se ven desde la primera sesión. El bronceado "
                    "es gradual y se intensifica en cada sesión, así que puedes "
                    "necesitar una o más, según qué tan bronceada quieras quedar."
                ),
                "pt": (
                    "Os resultados já aparecem desde a primeira sessão. O bronzeado "
                    "é gradual e vai se intensificando a cada sessão, então você "
                    "pode precisar de uma ou mais, dependendo de quão bronzeada "
                    "quer ficar."
                ),
                "en": (
                    "You'll see results from the very first session. The tan is "
                    "gradual and deepens with each session, so you may need one or "
                    "more, depending on how deep you'd like your tan."
                ),
            },
        ),
        (
            {
                "es": "¿Cómo funciona el Baño de Luna?",
                "pt": "Como funciona o Banho de Lua?",
                "en": "How does the Banho de Lua work?",
            },
            {
                "es": (
                    "Es un ritual corporal que aclara el vello, limpia la piel y "
                    "retira células muertas, dejando la piel uniforme y preparada. "
                    "La versión Premium añade renovación, hidratación y luminosidad."
                ),
                "pt": (
                    "É um ritual corporal que clareia os pelos, limpa a pele e "
                    "remove células mortas, deixando a pele uniforme e preparada. A "
                    "versão Premium acrescenta renovação, hidratação e luminosidade."
                ),
                "en": (
                    "It's a body ritual that lightens body hair, cleanses the skin "
                    "and removes dead cells, leaving skin even and prepared. The "
                    "Premium version adds renewal, hydration and luminosity."
                ),
            },
        ),
        (
            {
                "es": "¿Puedo hacer el Baño de Luna junto con el bronceado?",
                "pt": "Posso fazer o Banho de Lua junto com o bronzeado?",
                "en": "Can I book a Banho de Lua together with a tan?",
            },
            {
                "es": (
                    "Sí — es nuestra combinación Baño de Luna + Bronceado. Primero "
                    "se prepara y se renueva la piel, y después se termina con un "
                    "bronceado personalizado."
                ),
                "pt": (
                    "Sim — é a nossa combinação Banho de Lua + Bronzeado. Primeiro a "
                    "pele é preparada e renovada, depois finalizamos com um "
                    "bronzeado personalizado."
                ),
                "en": (
                    "Yes — that's our Moon Bath + Tan combination. The skin is "
                    "prepared and renewed first, then finished with a personalized "
                    "tan."
                ),
            },
        ),
        (
            {
                "es": "¿Qué llevo a la cita?",
                "pt": "O que eu levo no dia?",
                "en": "What should I bring to my appointment?",
            },
            {
                "es": (
                    "Ropa holgada y cómoda y, si tienes preferencia, el bikini que "
                    "quieras usar. Todo lo demás lo tenemos en el estudio."
                ),
                "pt": (
                    "Roupa larga e confortável e, se tiver preferência, o biquíni "
                    "que quiser usar. O resto tem tudo no estúdio."
                ),
                "en": (
                    "Loose, comfortable clothing and, if you have a preference, the "
                    "bikini you'd like to wear. Everything else is provided in "
                    "studio."
                ),
            },
        ),
        (
            {
                "es": "¿Qué debo evitar después de la cita?",
                "pt": "O que devo evitar depois do atendimento?",
                "en": "What should I avoid after my appointment?",
            },
            {
                "es": (
                    "Tu profesional te da instrucciones de cuidado personalizadas al "
                    "final de la sesión — seguirlas es lo que mantiene el resultado "
                    "bonito."
                ),
                "pt": (
                    "Sua profissional passa as instruções de cuidado personalizadas "
                    "no fim da sessão — seguir isso é o que mantém o resultado "
                    "bonito."
                ),
                "en": (
                    "Your professional gives you personalized aftercare instructions "
                    "at the end of your session — following those is what keeps the "
                    "result looking its best."
                ),
            },
        ),
        (
            {
                "es": "¿Cuánto me va a durar?",
                "pt": "Quanto tempo dura?",
                "en": "How long will my result last?",
            },
            {
                "es": (
                    "Depende de tu piel y de los cuidados que sigas. Tu profesional "
                    "te explicará qué esperar en tu caso."
                ),
                "pt": (
                    "Depende da sua pele e dos cuidados que você seguir. Sua "
                    "profissional explica o que esperar no seu caso."
                ),
                "en": (
                    "This depends on your skin and on the aftercare you follow. Your "
                    "professional will talk you through what to expect for your skin."
                ),
            },
        ),
        (
            {
                "es": "¿Puedo elegir qué tan oscuro queda?",
                "pt": "Posso escolher o quão escuro fica?",
                "en": "Can I choose how deep my tan goes?",
            },
            {
                "es": (
                    "Sí. Hablamos de la intensidad que buscas en la consulta y "
                    "trabajamos hacia ella juntas."
                ),
                "pt": (
                    "Sim. Conversamos sobre a intensidade que você busca na consulta "
                    "e trabalhamos nisso juntas."
                ),
                "en": (
                    "Yes. We discuss the intensity you're looking for during your "
                    "consultation and work towards it together."
                ),
            },
        ),
    ],
}

# ---------------------------------------------------------------------------
# 17. GALERIA
# ---------------------------------------------------------------------------
#
# Para usar uma foto: coloque o arquivo em assets/img/ e escreva o nome em
# "image". Enquanto estiver vazio, aparece um slot desenhado com a legenda.
#
# ATENÇÃO: fotos de clientes só podem ir ao ar com autorização escrita delas.

GALLERY = {
    "eyebrow": {"es": "Galería", "pt": "Galeria", "en": "Gallery"},
    "title": {
        "es": "El Brillo La Sirene",
        "pt": "O Brilho La Sirene",
        "en": "The La Sirene Glow",
    },
    "subtitle": {
        "es": "Resultados, detalles y momentos del estudio.",
        "pt": "Resultados, detalhes e momentos do estúdio.",
        "en": "Results, details and moments from the studio.",
    },
    # 25/09/26: as fotos antigas de clientes saíram; ficaram só as duas
    # fotos novas. Com até 3 fotos a grade vira duas colunas centralizadas.
    "items": [
        {
            "image": "gal-1.jpg",
            "caption": {"es": "En el estudio", "pt": "No estúdio", "en": "In the studio"},
            "size": "tall",
        },
        {
            "image": "gal-2.jpg",
            "caption": {"es": "Detalle de la marca", "pt": "Detalhe da marquinha",
                        "en": "Tan line detail"},
            "size": "tall",
        },
    ],
}

# ---------------------------------------------------------------------------
# 18. DEPOIMENTOS
# ---------------------------------------------------------------------------
#
# A DEFINIR — substitua pelos depoimentos reais das clientes.
# O depoimento vai no idioma em que a cliente escreveu; repita o mesmo texto
# nos três campos se não quiser traduzir a fala dela.

TESTIMONIALS = {
    "eyebrow": {"es": "Clientas", "pt": "Clientes", "en": "Clients"},
    "title": {
        "es": "Salieron Brillando.",
        "pt": "Saíram Brilhando.",
        "en": "They Left Glowing.",
    },
    "items": [
        {"quote": "", "name": "", "detail": "", "stars": 5},   # A DEFINIR
        {"quote": "", "name": "", "detail": "", "stars": 5},   # A DEFINIR
        {"quote": "", "name": "", "detail": "", "stars": 5},   # A DEFINIR
    ],
}

# ---------------------------------------------------------------------------
# 19. CHAMADA FINAL, LOCALIZAÇÃO E RODAPÉ
# ---------------------------------------------------------------------------

FINAL_CTA = {
    "eyebrow": {"es": "Reservar", "pt": "Agendar", "en": "Book"},
    "title": {
        "es": "¿Lista para tu Brillo?",
        "pt": "Pronta para o seu Brilho?",
        "en": "Ready for Your Glow?",
    },
    "subtitle": {
        "es": "Tu próximo bronceado empieza aquí.",
        "pt": "Seu próximo bronzeado começa aqui.",
        "en": "Your next tan starts here.",
    },
    "contact_line": {
        "es": "¿Dudas? Escríbenos",
        "pt": "Dúvidas? Fale com a gente",
        "en": "Questions? Contact us",
    },
}

LOCATION_SECTION = {
    "eyebrow": {"es": "Visítanos", "pt": "Visite", "en": "Visit"},
    "title": {
        "es": "Tu Próximo Brillo<br>Está en Tampa.",
        "pt": "Seu Próximo Brilho<br>Está em Tampa.",
        "en": "Your Next Glow<br>Is in Tampa.",
    },
    "cta": {"es": "Cómo llegar", "pt": "Como chegar", "en": "Get Directions"},
}

FOOTER = {
    "note": {
        "es": "Estudio de bronceado brasileño de lujo en Tampa, Florida.",
        "pt": "Estúdio de bronzeamento brasileiro de luxo em Tampa, Florida.",
        "en": "Luxury Brazilian tanning studio in Tampa, Florida.",
    },
    "credit": "Platinuss Design",
    "credit_url": "",
}
