

      new WOW().init();

        $(window).scroll(function(){  var sticky = $('.header'),     
         scroll = $(window).scrollTop();  if (scroll >= 100) sticky.addClass('fixed');  
         else sticky.removeClass('fixed');
     });

        //top thing slider js//

         $('.Partner-slider').owlCarousel({

            loop:false,

            nav:false,

            autoplay:false,

            dots:true,

            margin:20,

            smartSpeed: 1000,

            responsive:{

                0:{

                    items:1

                },

                600:{

                    items:1

                },

                1000:{

                    items:5

                }

            },navText: ["<i class='fa fa-angle-left' aria-hidden='true'></i>","<i class='fa fa-angle-right' aria-hidden='true'></i>"]

        });

            $('.testimonial-slider').owlCarousel({

        loop:true,

        nav:true,

        autoplay:true,

        margin:10,

        smartSpeed: 1000,

        dots:true,

        responsive:{

            0:{

                items:1

            },

            600:{

                items:1

            },

            1000:{

                items:1

            }

        },navText: ["<i class='fa fa-angle-left' aria-hidden='true'></i>","<i class='fa fa-angle-right' aria-hidden='true'></i>"]

    });

            //about page slider//

               $('.Aboutlogo-slider').owlCarousel({

            loop:false,

            nav:false,

            autoplay:false,

            dots:true,

            margin:20,

            smartSpeed: 1000,

            responsive:{

                0:{

                    items:1

                },

                600:{

                    items:1

                },

                1000:{

                    items:8

                }

            },navText: ["<i class='fa fa-angle-left' aria-hidden='true'></i>","<i class='fa fa-angle-right' aria-hidden='true'></i>"]

        });
//about page slider//

               $('.corporate-slider').owlCarousel({

            loop:false,

            nav:false,

            autoplay:false,

            dots:true,

            margin:20,

            smartSpeed: 1000,

            responsive:{

                0:{

                    items:1

                },

                600:{

                    items:1

                },

                1000:{

                    items:2

                }

            },navText: ["<i class='fa fa-angle-left' aria-hidden='true'></i>","<i class='fa fa-angle-right' aria-hidden='true'></i>"]

        });
        
(function($){
    'use script';
/*---canvas menu activation---*/
    $('.canvas_open').on('click', function(){
        $('.offcanvas_menu_wrapper,.off_canvars_overlay').addClass('active')
    });
    
    $('.canvas_close,.off_canvars_overlay').on('click', function(){
        $('.offcanvas_menu_wrapper,.off_canvars_overlay').removeClass('active')
    });


    /*---Off Canvas Menu---*/
    var $offcanvasNav = $('.offcanvas_main_menu'),
        $offcanvasNavSubMenu = $offcanvasNav.find('.sub-menu');
    $offcanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i class="fa fa-angle-down"></i></span>');
    
    $offcanvasNavSubMenu.slideUp();
    
    $offcanvasNav.on('click', 'li a, li .menu-expand', function(e) {
        var $this = $(this);
        if ( ($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand')) ) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length){
                $this.siblings('ul').slideUp('slow');
            }else {
                $this.closest('li').siblings('li').find('ul:visible').slideUp('slow');
                $this.siblings('ul').slideDown('slow');
            }
        }
        if( $this.is('a') || $this.is('span') || $this.attr('clas').match(/\b(menu-expand)\b/) ){
            $this.parent().toggleClass('menu-open');
        }else if( $this.is('li') && $this.attr('class').match(/\b('menu-item-has-children')\b/) ){
            $this.toggleClass('menu-open');
        }
    });
}(jQuery));