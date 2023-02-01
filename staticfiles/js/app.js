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


console.log('hello world')