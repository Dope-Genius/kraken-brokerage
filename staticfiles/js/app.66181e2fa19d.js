// Navigation button
const navbtn = document.querySelector('.rand-span')
const navlink = document.querySelector('.nav-link-list')

navbtn.addEventListener('click', function(){
  console.log('working')
  navlink.classList.toggle('nav-display')
});

// Sticky Header
const dealsSection = document.querySelector('.section--deals');
const nav = document.querySelector('.nav');

// Make Nav Sticky on scroll
window.addEventListener('scroll', function(){
  console.log(window.scrollY);
  if (window.scrollY > 30){
    nav.classList.add('navSticky')
  } else {
    nav.classList.remove('navSticky')
  }
});


function myFunction() {
  /* Get the text field */
  var copyText = document.getElementById("myInput");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}

function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// Hide and show password
// const password = document.querySelector('#password');
// const password2 = document.querySelector('#password2');

// const togglePassword = document.querySelector('#togglePassword');
// const togglePassword2 = document.querySelector('#togglePassword2');


// togglePassword.addEventListener('click', function (e) {
//   const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
//     password.setAttribute('type', type);
//     // toggle the eye / eye slash icon
//     // this.classList.toggle('bi-eye bi-eye);
//     if(togglePassword.classList.contains("bi-eye")) {
//       togglePassword.classList.remove('bi-eye')
//       togglePassword.classList.add('bi-eye-slash')
//     } else {
//       togglePassword.classList.add('bi-eye')
//       togglePassword.classList.remove('bi-eye-slash')
//     }
// });

// togglePassword2.addEventListener('click', function (e) {
//   const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
//     password2.setAttribute('type', type);
//     // toggle the eye / eye slash icon
//     if(togglePassword2.classList.contains("bi-eye")) {
//       togglePassword2.classList.remove('bi-eye')
//       togglePassword2.classList.add('bi-eye-slash')
//     } else {
//       togglePassword2.classList.add('bi-eye')
//       togglePassword2.classList.remove('bi-eye-slash')
//     }
// });
