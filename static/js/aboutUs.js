const button = document.querySelector('.hover-button');

button.addEventListener('mouseover', () => {
  button.textContent = 'Hovering!';
});

button.addEventListener('mouseout', () => {
  button.textContent = 'Hover Me';
});
