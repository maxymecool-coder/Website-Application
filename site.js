// Light and dark: the switch in the top band. The choice is saved as "theme", the same key the Notes pages use,
// so picking one here carries over to the vault. With no choice saved, the page follows the device setting.
(() => {
  const root = document.documentElement;
  const button = document.querySelector('.theme');
  if (!button) return;
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  const current = () => root.dataset.theme || (media.matches ? 'dark' : 'light');
  const sync = () => {
    const dark = current() === 'dark';
    button.setAttribute('aria-pressed', String(dark));
    button.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
  };
  button.addEventListener('click', () => {
    const next = current() === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) { /* private mode: the switch still works for this visit */ }
    sync();
  });
  media.addEventListener('change', sync);
  sync();
})();

// Friends: click one and it hops, throwing out notes and sparkles (Miku) or hearts (Cinnamoroll).
(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const bits = {
    miku: [['note', '♪'], ['spark', '✦'], ['note', '♫'], ['spark', '✧']],
    cinnamoroll: [['heart', '♥'], ['spark', '✦'], ['note', '♪'], ['heart', '♡']],
  };

  document.addEventListener('click', (e) => {
    const friend = e.target.closest('.mascot:not(.is-empty), .perch[data-character]');
    if (!friend) return;
    const kinds = bits[friend.dataset.character] || bits.miku;
    const box = friend.getBoundingClientRect();
    const cx = box.left + box.width / 2;
    const cy = box.top + box.height * 0.35;

    for (let i = 0; i < 8; i++) {
      const [kind, glyph] = kinds[i % kinds.length];
      const bit = document.createElement('i');
      bit.className = `pop pop-${kind}`;
      bit.textContent = glyph;
      bit.setAttribute('aria-hidden', 'true');
      bit.style.left = `${cx}px`;
      bit.style.top = `${cy}px`;
      document.body.appendChild(bit);
      const angle = ((-90 + (i - 3.5) * 24 + (Math.random() * 14 - 7)) * Math.PI) / 180;
      const dist = 60 + Math.random() * 50;
      const dx = Math.cos(angle) * dist;
      const dy = Math.sin(angle) * dist;
      bit.animate([
        { transform: 'translate(0, 0) scale(.4)', opacity: 0 },
        { transform: `translate(${dx * 0.6}px, ${dy * 0.6}px) scale(1.1)`, opacity: 1, offset: 0.35 },
        { transform: `translate(${dx}px, ${dy + 30}px) scale(.8) rotate(${Math.random() * 60 - 30}deg)`, opacity: 0 },
      ], { duration: 900 + Math.random() * 300, easing: 'cubic-bezier(.2, .7, .3, 1)' }).onfinish = () => bit.remove();
    }

    friend.classList.remove('is-hop');
    void friend.offsetWidth;
    friend.classList.add('is-hop');
  });
})();
