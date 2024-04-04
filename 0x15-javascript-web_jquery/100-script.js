document.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('header');
  for (const item of items) {
    item.style.color = '#FF0000';
  }
});
