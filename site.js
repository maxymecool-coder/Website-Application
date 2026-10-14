// Mascots: click one and it hops, throwing out notes and sparkles (Miku) or hearts and clouds (Cinnamoroll).
(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const bits = {
    miku: ['note', 'spark', 'note', 'star', 'spark-blue'],
    cinnamoroll: ['heart', 'cloud', 'spark', 'heart', 'spark-blue'],
  };

  document.addEventListener('click', (e) => {
    const mascot = e.target.closest('.mascot:not(.is-empty)');
    if (!mascot) return;
    const kinds = bits[mascot.dataset.character] || bits.miku;
    const box = mascot.getBoundingClientRect();
    const cx = box.left + box.width / 2;
    const cy = box.top + box.height * 0.4;

    for (let i = 0; i < 8; i++) {
      const bit = document.createElement('i');
      bit.className = `pop pop-${kinds[i % kinds.length]}`;
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

    mascot.classList.remove('is-hop');
    void mascot.offsetWidth;
    mascot.classList.add('is-hop');
  });
})();
