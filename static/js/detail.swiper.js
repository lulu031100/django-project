var mySwiper = new Swiper ('.swiper-container', {
  effect: 'cube',
  loop: true,
  cubeEffect: {
    slideShadows: false,
     shadowOffset: 20,
     shadowScale: 0.94,
  },
   navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});