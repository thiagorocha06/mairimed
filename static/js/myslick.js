$(document).ready(function(){
    $('.anuncio-slider').slick({
      dots: true,
      arrows: false,
      autoplay: true,
      autoplaySpeed: 3000,
      pauseOnHover: true,
    });
    });

$(document).ready(function(){
    $('.divs-slider').slick({
        dots: true,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 4,
        // autoplay: true,
        // autoplaySpeed: 2000,
        // centerMode: true,
        responsive: [
        {
          breakpoint: 1224,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
    });
    });
