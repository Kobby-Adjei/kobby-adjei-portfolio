// Section rail. A tick per section down the right edge, the current one marked.
// Hover the rail to read the titles, click a tick to jump.
(function () {
  const sections = [...document.querySelectorAll('section')].filter((s) => s.querySelector('h2'));
  if (sections.length < 3) return;

  const slug = (t) =>
    t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);

  const rail = document.createElement('nav');
  rail.className = 'rail';
  rail.setAttribute('aria-label', 'Jump to a section');

  const buttons = sections.map((sec) => {
    const h = sec.querySelector('h2');
    const title = h.textContent.trim();
    if (!sec.id) sec.id = slug(title);

    const b = document.createElement('button');
    b.type = 'button';
    b.innerHTML = `<span class="lbl">${title}</span><span class="tick"></span>`;
    b.setAttribute('aria-label', `Jump to ${title}`);
    b.addEventListener('click', () => {
      sec.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
      history.replaceState(null, '', '#' + sec.id);
    });
    rail.appendChild(b);
    return b;
  });

  document.body.appendChild(rail);

  // Mark whichever section is nearest the top of the viewport.
  function mark() {
    let best = 0;
    let bestDist = Infinity;
    sections.forEach((sec, i) => {
      const d = Math.abs(sec.getBoundingClientRect().top - 90);
      if (d < bestDist) { bestDist = d; best = i; }
    });
    buttons.forEach((b, i) => b.classList.toggle('on', i === best));
  }

  let ticking = false;
  addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { mark(); ticking = false; });
  }, { passive: true });
  addEventListener('resize', mark, { passive: true });
  mark();
})();
