/**
*
* -----------------------------------------------------------------------------
*
* Template : Evenio - Events & Conference HTML Template
* Author : reacthemes
* Author URI : http://www.reactheme.com/
*
* -----------------------------------------------------------------------------
*
**/
(function($) {
	"use strict";
    // sticky menu
    var header = $('.menu-sticky');
    var win = $(window);

    win.on('scroll', function() {
       var scroll = win.scrollTop();
       if (scroll < 1) {
           header.removeClass("sticky");
       } else {
           header.addClass("sticky");
       }

        $("section").each(function() {
        var elementTop = $(this).offset().top - $('#rs-header').outerHeight();
            if(scroll >= elementTop) {
                $(this).addClass('loaded');
            }
        });
    });
	
    //window load
    $(window).on( 'load', function() {
        $("#loading").delay(1500).fadeOut(500);
        $("#loading-center").on( 'click', function() {
        $("#loading").fadeOut(500);
        })
    })
    
    //slider
    var slidercarousel = $('.slider-carousel');
    if(slidercarousel.length){
        $(".slider-carousel").owlCarousel({
            margin: 0,
            nav: false,
            navText:[
                "<i class='fa fa-angle-left'></i>",
                "<i class='fa fa-angle-right'></i>"
            ],
            loop: true,
            dots: true,
            mouseDrag: false,
            items: 1,
            autoplay: true,
            animateOut: 'fadeOut',
            autoplayTimeout: 5000,
            autoplayHoverPause: false,
            responsiveClass: true
        });
    }

   
   // onepage nav
   var navclose = $('#onepage-menu');
   if(navclose.length){
       $(".nav-menu li a").on("click", function () {
           if ($(".showhide").is(":visible")) {
               $(".showhide").trigger("click");
           }
       });
       if ($.fn.onePageNav) {
           $(".nav-menu").onePageNav({
               currentClass: "active-menu"
           });
        }
    }
    var searchParent = $('.search-parent');
    if(searchParent.length){ 
        $( ".search-parent" ).on( "click", function() {
          $( this).toggleClass( "open_add_class", 1000 );
        });
    }

    // collapse hidden  
     var navMain = $(".navbar-collapse");
     navMain.on("click", "a:not([data-toggle])", null, function () {
         navMain.collapse('hide');
     });  

    // wow init
    new WOW().init();

    $('.collapse.show').prev('.card-header').addClass('active');
    $('#accordion, #bs-collapse, #accordion1')
    .on('show.bs.collapse', function (a) {
        $(a.target).prev('.card-header').addClass('active');
    })
    .on('hide.bs.collapse', function (a) {
        $(a.target).prev('.card-header').removeClass('active');
    });
    
    // magnificPopup init
    var imagepopup = $('.image-popup');
    if(imagepopup.length){
        $('.image-popup').magnificPopup({
            type: 'image',
            callbacks: {
                beforeOpen: function() {
                   this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure animated zoomInDown');
                }
            },
            gallery: {
                enabled: true
            }
        });
    }

    // Get a quote popup
    var popupquote = $('.popup-quote');
    if(popupquote.length){
        $('.popup-quote').magnificPopup({
            type: 'inline',
            preloader: false,
            focus: '#qname',
            removalDelay: 500,
            callbacks: {
                beforeOpen: function() {
                    this.st.mainClass = this.st.el.attr('data-effect');
                    if(win.width() < 800) {
                        this.st.focus = false;
                    } else {
                        this.st.focus = '#qname';
                    }
                }
            }
        });
    }
    
    //preloader
    $(window).on('load', function() {
        $("#pre-load").delay(1000).fadeOut(500);
    })

    //Videos popup jQuery 
    var popupvideos = $('.popup-videos, .popup-border');
    if(popupvideos.length){
        $('.popup-videos, .popup-border').magnificPopup({
            disableOn: 10,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        }); 
    }

    //CountDown Timer
    var CountTimer = $('.CountDownTimer');
    if(CountTimer.length){ 
        $(".CountDownTimer").TimeCircles({
            fg_width: 0.030,
            bg_width: 0.8,
            circle_bg_color: "#eeeeee",
            circle_fg_color: "#eeeeee",
            time: {
                Days:{
                    color: "#032390"
                },
                Hours:{
                    color: "#032390"
                },
                Minutes:{
                    color: "#032390"
                },
                Seconds:{
                    color: "#032390"
                }
            }
        }); 
    }

    /*-------------------------------------
        OwlCarousel
    -------------------------------------*/
    $('.rs-carousel').each(function() {
        var owlCarousel = $(this),
        loop = owlCarousel.data('loop'),
        items = owlCarousel.data('items'),
        margin = owlCarousel.data('margin'),
        stagePadding = owlCarousel.data('stage-padding'),
        autoplay = owlCarousel.data('autoplay'),
        autoplayTimeout = owlCarousel.data('autoplay-timeout'),
        smartSpeed = owlCarousel.data('smart-speed'),
        dots = owlCarousel.data('dots'),
        nav = owlCarousel.data('nav'),
        navSpeed = owlCarousel.data('nav-speed'),
        xsDevice = owlCarousel.data('mobile-device'),
        xsDeviceNav = owlCarousel.data('mobile-device-nav'),
        xsDeviceDots = owlCarousel.data('mobile-device-dots'),
        smDevice = owlCarousel.data('ipad-device'),
        smDeviceNav = owlCarousel.data('ipad-device-nav'),
        smDeviceDots = owlCarousel.data('ipad-device-dots'),
        smDevice2 = owlCarousel.data('ipad-device2'),
        smDeviceNav2 = owlCarousel.data('ipad-device-nav2'),
        smDeviceDots2 = owlCarousel.data('ipad-device-dots2'),
        mdDevice = owlCarousel.data('md-device'),
        centerMode = owlCarousel.data('center-mode'),
        HoverPause = owlCarousel.data('hoverpause'),
        mdDeviceNav = owlCarousel.data('md-device-nav'),
        mdDeviceDots = owlCarousel.data('md-device-dots');
        owlCarousel.owlCarousel({
            loop: (loop ? true : false),
            items: (items ? items : 4),
            lazyLoad: true,
            center: (centerMode ? true : false),
            autoplayHoverPause: (HoverPause ? true : false),
            margin: (margin ? margin : 0),
            //stagePadding: (stagePadding ? stagePadding : 0),
            autoplay: (autoplay ? true : false),
            autoplayTimeout: (autoplayTimeout ? autoplayTimeout : 1000),
            smartSpeed: (smartSpeed ? smartSpeed : 250),
            dots: (dots ? true : false),
            nav: (nav ? true : false),
            navText: ["<i class='flaticon-left-arrow'></i>", "<i class='flaticon-right-arrow'></i>"],
            navSpeed: (navSpeed ? true : false),
            responsiveClass: true,
            responsive: {
                0: {
                    items: (xsDevice ? xsDevice : 1),
                    nav: (xsDeviceNav ? true : false),
                    dots: (xsDeviceDots ? true : false),
                    center: false,
                },
                768: {
                    items: (smDevice2 ? smDevice2 : 2),
                    nav: (smDeviceNav2 ? true : false),
                    dots: (smDeviceDots2 ? true : false),
                    center: false,
                },
                992: {
                    items: (smDevice ? smDevice : 3),
                    nav: (smDeviceNav ? true : false),
                    dots: (smDeviceDots ? true : false),
                    center: false,
                },
                1200: {
                    items: (mdDevice ? mdDevice : 4),
                    nav: (mdDeviceNav ? true : false),
                    dots: (mdDeviceDots ? true : false),
                }
            }
        });
    });

    // Skill bar 
    var skillbar = $('.skillbar');
    if(skillbar.length) {
        $('.skillbar').skillBars({  
            from: 0,    
            speed: 4000,    
            interval: 100,  
            decimals: 0,    
        });
    }

		
    // Counter Up
    var counter_Up = $('.rs-count');
    if(counter_Up.length) {  
        $('.rs-count').counterUp({
            delay: 20,
            time: 2000
        });
    }
    
    // scrollTop init	
    var totop = $('#scrollUp');    
    win.on('scroll', function() {
        if (win.scrollTop() > 150) {
            totop.fadeIn();
        } else {
            totop.fadeOut();
        }
    });
    totop.on('click', function() {
        $("html,body").animate({
            scrollTop: 0
        }, 500)
    });

    //canvas menu
    var navexpander = $('#nav-expander, #nav-expander2');
    if(navexpander.length){
        $('#nav-expander, #nav-expander2, #nav-close, #nav-close2, .offwrap').on('click',function(e){
            e.preventDefault();
            $('body').toggleClass('nav-expanded');
        });
    }

    // View Course
    $('.course-view-part .view-icons .view-grid').on('click',function(e){
        e.preventDefault();
        $('.rs-popular-courses').removeClass('list-view');
    });
    $('.course-view-part .view-icons .view-list').on('click',function(e){
        e.preventDefault();
        $('.rs-popular-courses').addClass('list-view');
    });
    
	
    // categories btn
    $('.cat-menu-inner').hide();
    $('.cat-btn').on('click',function(){
        $('.cat-menu-inner').slideToggle();
    })

    
    if($('.rs_click_menu').length) {
        $('.rs_click_menu').on('click', function() {
            $( '.menu-responsive' ).toggleClass("active__main__menu");
        });
    }
    if($('.rs_click_menu').length) {
        $('#rs_click__id').click(function(){
            $(this).toggleClass('rs__open_hum');
        });
    }
    $('.menu-wrap-off a').each(function(){
        var href = $(this).attr("href");
        if(href == "#"){
            $(this).addClass('hash');
        }else{
            $(this).removeClass('hash');
        }
    });

    // Parallax Stuff
    if ($(".stuff").length) {
        var stuff = $('.stuff').get(0);
        var parallaxInstance = new Parallax(stuff);
    }
    if ($(".stuff2").length) {
        var stuff = $('.stuff2').get(0);
        var parallaxInstance = new Parallax(stuff);
    }
    if ($(".stuff3").length) {
        var stuff = $('.stuff3').get(0);
        var parallaxInstance = new Parallax(stuff);
    }
    if ($(".stuff4").length) {
        var stuff = $('.stuff4').get(0);
        var parallaxInstance = new Parallax(stuff);
    }
    if ($(".stuff5").length) {
        var stuff = $('.stuff5').get(0);
        var parallaxInstance = new Parallax(stuff);
    }
    if ($(".stuff6").length) {
        var stuff = $('.stuff6').get(0);
        var parallaxInstance = new Parallax(stuff);
    }
    if ($(".stuff7").length) {
        var stuff = $('.stuff7').get(0);
        var parallaxInstance = new Parallax(stuff);
    }

    // swiper Slider
    if (window.innerWidth > 991) {
        if ($(".swiper-container").length) {
            var swiper = new Swiper('.swiper-container', {
                direction: 'vertical',
                slidesPerView: 1,
                speed: 700,
                spaceBetween: 0,
                mousewheel: true,
                pagination: {
                el: '.swiper-pagination',
                    clickable: true,
                    renderBullet: function (index, className) {
                        return '<span class="' + className + '">' + (index + 1) + '</span>';
                    },
                },
            });
        }
    }

   /******** Mobile Menu Start ********/
   
   $('.mobile-navbar-menu a').each(function(){
       var href = $(this).attr("href");
       if(href ="#"){
           $(this).addClass('hash');
       }else{
           $(this).removeClass('hash');
       }
   });

   $.fn.menumaker = function(options) {
     var mobile_menu = $(this), settings = $.extend({
       format: "dropdown",
       sticky: false
     }, options);

       return this.each(function() {
       mobile_menu.find('li ul').parent().addClass('has-sub');
       var multiTg = function() {
           mobile_menu.find(".has-sub").prepend('<span class="submenu-button"><em></em></span>');
           mobile_menu.find(".hash").parent().addClass('hash-has-sub');
           mobile_menu.find('.submenu-button').on('click', function() {
               $(this).toggleClass('submenu-opened');
               if ($(this).siblings('ul').hasClass('open-sub')) {
                   $(this).siblings('ul').removeClass('open-sub').hide('fadeIn');
                   $(this).siblings('ul').hide('fadeIn');                                     
               }
               else {
                   $(this).siblings('ul').addClass('open-sub').hide('fadeIn');
                   $(this).siblings('ul').slideToggle().show('fadeIn');
               }
           });
       };

       if (settings.format === 'multitoggle') multiTg();
       else mobile_menu.addClass('dropdown');
       if (settings.sticky === true) mobile_menu.css('position', 'fixed');
      var resizeFix = function() {
           if ($( window ).width() > 991) {
               mobile_menu.find('ul').show('fadeIn');
               mobile_menu.find('ul.sub-menu').hide('fadeIn');
           }          
       };
       resizeFix();
       return $(window).on('resize', resizeFix);
       });
   };

   $(document).ready(function(){
       $("#mobile-navbar-menu").menumaker({
       format: "multitoggle"
       });
   });
})(jQuery);