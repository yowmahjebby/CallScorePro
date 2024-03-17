(function ($) {

  "use strict";

    // PRE LOADER
    $(window).load(function(){
      $('.preloader').fadeOut(1000); // set duration in brackets    
    });
    

    // MENU
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });

    $(window).scroll(function() {
      if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
          } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
          }
    });
    

    // PARALLAX EFFECT
    $.stellar({
      horizontalScrolling: false,
    }); 


    // MAGNIFIC POPUP
    $('.image-popup').magnificPopup({
        type: 'image',
        removalDelay: 300,
        mainClass: 'mfp-with-zoom',
        gallery:{
          enabled:true
        },
        zoom: {
        enabled: true, // By default it's false, so don't forget to enable it

        duration: 300, // duration of the effect, in milliseconds
        easing: 'ease-in-out', // CSS transition easing function

        // The "opener" function should return the element from which popup will be zoomed in
        // and to which popup will be scaled down
        // By defailt it looks for an image tag:
        opener: function(openerElement) {
        // openerElement is the element on which popup was initialized, in this case its <a> tag
        // you don't need to add "opener" option if this code matches your needs, it's defailt one.
        return openerElement.is('img') ? openerElement : openerElement.find('img');
        }
      }
    });


    // SMOOTH SCROLL
    $(function() {
      $('.custom-navbar a, #home a').on('click', function(event) {
        var $anchor = $(this);
          $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
          }, 1000);
            event.preventDefault();
      });
    });  
})(jQuery);

function showErrorMessage(element, message) {
  document.querySelector("."+element).classList.add("display-error-message");
  document.querySelector("."+element).innerHTML = message;
};

function clearErrorMessages() {
  let errors = document.querySelectorAll(".error");
  for (var i = 0; i < errors.length; i++) {
    errors[i].classList.remove("display-error-message");
    errors[i].innerHTML = "";
  }
};

function signUpFormValidation(event) {

  clearErrorMessages();

  var username = document.getElementById('sign_up').querySelector('#username').value;
  var password1 = document.getElementById('sign_up').querySelector('#password1').value;
  var password2 = document.getElementById('sign_up').querySelector('#password2').value;
  var email = document.getElementById('sign_up').querySelector('#email').value;

  // Username validation
  var usernameRegex = /^[a-zA-Z0-9@/./+/-/_]{8,150}$/;
  if (!usernameRegex.test(username)) {
      showErrorMessage('user-error', 'Username must be atleast 8 characters. Letters, digits, and @/./+/-/_ only');
      event.preventDefault();
  }

  // Password validation
  var similarInfo = ['first name', 'last name', 'username', 'email']; // Replace with actual personal information
  if (similarInfo.some(info => password1.includes(info))) {
      showErrorMessage('pass1-error', 'Your password can’t be too similar to your other personal information');
      event.preventDefault();
  }
  if (password1.length < 8) {
      showErrorMessage('pass1-error', 'Your password must contain at least 8 characters');
      event.preventDefault();
  }
  var commonPasswords = [ 'password', 'password1','password123', '12345678', '123456789', '1234567890',  '123456789a', 'letmein','letmein123', 'abcdefgh', 'abcdefghi', 'welcome']; // Replace with actual common passwords
  if (commonPasswords.includes(password1)) {
      showErrorMessage('pass1-error', 'Your password can’t be a commonly used password');
      event.preventDefault();
  }
  if (!isNaN(password1) && /^\d+$/.test(password1)) {
      showErrorMessage('pass1-error', 'Your password can’t be entirely numeric');
      event.preventDefault();
  }

  // Email validation
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
      showErrorMessage('email-error', 'Invalid email address');
      event.preventDefault();
  }

      // Password match validation
  if (password1 !== password2) {
      showErrorMessage('pass2-error', 'Passwords do not match');
      event.preventDefault();
  }
};