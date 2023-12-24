// Function to handle the scroll effect
function handleScroll(images, multipliers) {
  const scrollPosition = window.scrollY;

  images.forEach((img, index) => {
    if (img) { // Check if the image element exists
      const movement = scrollPosition * multipliers[index] % 798;
      img.style.transform = `translateY(${movement}px)`;
    }
  });
}

// Function to initialize the scroll effect
function initScroll() {
  const leftImages = [
    document.getElementById('scrollImage'),
    document.getElementById('scrollImage2'),
    document.getElementById('scrollImage3')
  ];

  const rightImages = [
    document.getElementById('scrollImage4'),
    document.getElementById('scrollImage5'),
    document.getElementById('scrollImage6')
  ];

  const multipliers = [-0.8, 1.2, 0.4, 0.7, -1.4, 0.5]; // Adjust the multipliers as needed

  window.addEventListener('scroll', () => {
    handleScroll(leftImages, multipliers.slice(0, 3));
    handleScroll(rightImages, multipliers.slice(3, 6));
  });
}

// Initialize the scroll effect when the window is fully loaded
window.onload = initScroll;


function Message2() {
  pyodide.runPython('cipher_machine.run()');
}