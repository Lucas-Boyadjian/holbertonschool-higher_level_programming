document.getElementById('toggle_header').addEventListener('click', function () {
  const the_header = document.querySelector('header');

  if (the_header.className === 'red') {
    the_header.className = 'green';
  } else {
    the_header.className = 'red';
  }
});
