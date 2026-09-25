/* LA SIRENE TANNING — interações
   Leve de propósito: o site tem que parecer luxuoso, não tecnológico. */

(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- abertura: só na primeira visita da sessão ------------------------ */
  var seen = false;
  try { seen = sessionStorage.getItem("ls-seen") === "1"; } catch (e) {}
  if (seen || reduced) {
    document.documentElement.classList.add("seen");
  } else {
    try { sessionStorage.setItem("ls-seen", "1"); } catch (e) {}
  }

  /* ---- ano no rodapé ---------------------------------------------------- */
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- navbar: fundo sólido ao rolar ------------------------------------ */
  var nav = document.getElementById("nav");
  var fab = document.querySelector(".fab");

  function onScroll() {
    var y = window.scrollY;
    if (nav) nav.classList.toggle("is-solid", y > 40);
    if (fab) fab.classList.toggle("is-on", y > window.innerHeight * 0.75);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---- menu mobile ------------------------------------------------------ */
  var toggle = document.getElementById("navToggle");
  var menu = document.getElementById("mobileMenu");

  function setMenu(open) {
    if (!menu || !toggle) return;
    menu.classList.toggle("is-open", open);
    menu.setAttribute("aria-hidden", String(!open));
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.style.overflow = open ? "hidden" : "";
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      setMenu(!menu.classList.contains("is-open"));
    });
  }
  if (menu) {
    menu.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) setMenu(false);
    });
  }
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") setMenu(false);
  });

  /* ---- reveal ao entrar na tela ----------------------------------------- */
  var targets = document.querySelectorAll("[data-reveal]");

  if (reduced || !("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(targets, function (el) {
      el.classList.add("is-in");
    });
  } else {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          // escalona irmãos para o conteúdo aparecer em cascata
          var sibs = el.parentElement
            ? el.parentElement.querySelectorAll(":scope > [data-reveal]")
            : [el];
          var i = Array.prototype.indexOf.call(sibs, el);
          if (!el.classList.contains("rv-flat")) {
            el.style.transitionDelay = Math.min(i, 6) * 90 + "ms";
          }
          el.classList.add("is-in");
          io.unobserve(el);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
    );
    Array.prototype.forEach.call(targets, function (el) {
      io.observe(el);
    });
  }

  /* ---- FAQ accordion ---------------------------------------------------- */
  var items = document.querySelectorAll(".faq__item");
  Array.prototype.forEach.call(items, function (item) {
    var btn = item.querySelector(".faq__q");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var open = item.classList.contains("is-open");
      // uma resposta aberta por vez
      Array.prototype.forEach.call(items, function (other) {
        other.classList.remove("is-open");
        var b = other.querySelector(".faq__q");
        if (b) b.setAttribute("aria-expanded", "false");
      });
      if (!open) {
        item.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---- link ativo na navbar --------------------------------------------- */
  var navLinks = document.querySelectorAll(".nav__links a[href^='#']");
  var sections = [];
  Array.prototype.forEach.call(navLinks, function (a) {
    var el = document.querySelector(a.getAttribute("href"));
    if (el) sections.push({ link: a, el: el });
  });

  if (sections.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          navLinks.forEach
            ? navLinks.forEach(clear)
            : Array.prototype.forEach.call(navLinks, clear);
          function clear(a) {
            a.classList.remove("is-active");
          }
          var hit = sections.filter(function (s) {
            return s.el === entry.target;
          })[0];
          if (hit) hit.link.classList.add("is-active");
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach(function (s) {
      spy.observe(s.el);
    });
  }


  /* ======================================================================
     Revelação 3D das tipografias
     Cada palavra vira um bloco próprio que gira para cima, com atraso
     em cascata. O texto continua sendo texto: dá para selecionar e o
     leitor de tela lê normalmente.
     ====================================================================== */

  var SPLIT_TARGETS = [
    ".hero__brand", ".hero__title", ".sec__title", ".concept__title",
    ".deep__title", ".premium__title", ".cta__title", ".loc__title",
    ".prep__when", ".vs__name"
  ].join(",");

  function splitWords(el) {
    if (el.dataset.split) return;
    el.dataset.split = "1";
    var i = 0;

    function walk(node) {
      var kids = Array.prototype.slice.call(node.childNodes);
      kids.forEach(function (n) {
        if (n.nodeType === 3) {
          var text = n.textContent;
          if (!text.trim()) return;
          var frag = document.createDocumentFragment();
          text.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) {
              frag.appendChild(document.createTextNode(part));
              return;
            }
            var outer = document.createElement("span");
            outer.className = "w";
            var inner = document.createElement("span");
            inner.className = "wi";
            inner.textContent = part;
            inner.style.setProperty("--i", i++);
            outer.appendChild(inner);
            frag.appendChild(outer);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== "BR") {
          walk(n);
        }
      });
    }

    walk(el);
    el.classList.add("split");

    // o bloco pai só aparece; quem se move são as palavras
    var holder = el.closest("[data-reveal]");
    if (holder) holder.classList.add("rv-flat");
  }

  if (!reduced) {
    Array.prototype.forEach.call(
      document.querySelectorAll(SPLIT_TARGETS),
      splitWords
    );
  }

  /* ---- hero: entra no carregamento, não no scroll ----------------------- */
  var heroText = document.querySelector(".hero__text");
  if (heroText) {
    var wait = reduced || seen ? 120 : 1150;
    setTimeout(function () {
      heroText.classList.add("is-in");
    }, wait);
  }

  /* ======================================================================
     Inclinação 3D dos cards
     Acompanha o cursor de leve. Só no mouse — em toque não faz sentido
     e atrapalharia o scroll.
     ====================================================================== */

  var canTilt =
    !reduced && window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  if (canTilt) {
    var TILT_MAX = 5; // graus — passar disso vira efeito de videogame
    Array.prototype.forEach.call(
      document.querySelectorAll(".card, .sig, .combo, .t__card"),
      function (card) {
        var raf = null;

        card.addEventListener("pointermove", function (ev) {
          if (raf) return;
          raf = requestAnimationFrame(function () {
            raf = null;
            var r = card.getBoundingClientRect();
            var px = (ev.clientX - r.left) / r.width - 0.5;
            var py = (ev.clientY - r.top) / r.height - 0.5;
            card.classList.add("tilt");
            card.classList.remove("tilt-reset");
            card.style.setProperty("--ry", (px * TILT_MAX).toFixed(2) + "deg");
            card.style.setProperty("--rx", (-py * TILT_MAX).toFixed(2) + "deg");
            card.style.setProperty("--ty", "-8px");
          });
        });

        card.addEventListener("pointerleave", function () {
          if (raf) { cancelAnimationFrame(raf); raf = null; }
          card.classList.add("tilt-reset");
          card.style.setProperty("--rx", "0deg");
          card.style.setProperty("--ry", "0deg");
          card.style.setProperty("--ty", "0px");
        });
      }
    );
  }

  /* ---- parallax muito leve no hero -------------------------------------- */
  var heroImg = document.querySelector(".hero__figure img");
  if (heroImg && !reduced) {
    var ticking = false;
    window.addEventListener(
      "scroll",
      function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
          var y = window.scrollY;
          if (y < window.innerHeight) {
            heroImg.style.transform = "translate3d(0," + y * 0.14 + "px,0)";
          }
          ticking = false;
        });
      },
      { passive: true }
    );
  }
})();
