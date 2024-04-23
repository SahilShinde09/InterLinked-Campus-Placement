const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const slides = document.querySelector('.slides');
const slideWidth = slides.clientWidth / 3; // divide by number of slides
let slideIndex = 0;

nextBtn.addEventListener('click', () => {
  if (slideIndex < 2) { // check if not the last slide
    slideIndex++;
    slides.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
  }
});

prevBtn.addEventListener('click', () => {
  if (slideIndex > 0) { // check if not the first slide
    slideIndex--;
    slides.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
  }
});
