const image = document.getElementById('scrollImage');
let imagePosition = 0;
function handleScroll() {
  const container = document.documentElement;
  imagePosition = container.scrollTop;
  image.style.transform = `translateY(-${imagePosition}px)`;
}
window.addEventListener('scroll', handleScroll);

const image2 = document.getElementById('scrollImage2');
let imagePosition2 = 0;
function handleScroll2() {
  const container2 = document.documentElement;
  imagePosition2 = container2.scrollTop;
  image2.style.transform = `translateY(${imagePosition2}px)`;
}
window.addEventListener('scroll', handleScroll2);

const image3 = document.getElementById('scrollImage3');
let imagePosition3 = 0;
function handleScroll3() {
  const container3 = document.documentElement;
  imagePosition3 = 0.5 * container3.scrollTop;
  image3.style.transform = `translateY(-${imagePosition3}px)`;
}
window.addEventListener('scroll', handleScroll3);