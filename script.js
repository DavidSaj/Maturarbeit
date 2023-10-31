const image = document.getElementById('scrollImage');
let imagePosition = 0;

function handleScroll() {
  const container = document.documentElement;
 
  imagePosition = container.scrollTop;

  image.style.transform = `translateY(-${imagePosition}px)`;
}



window.addEventListener('scroll', handleScroll);
