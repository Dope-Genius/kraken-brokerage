// Dashboard Navigation
const listIcon = document.querySelector('.nav-list')
listIcon.addEventListener('click', function(){
    document.querySelector(".nav").classList.toggle('hideNav')
});

// Remove referral card
const closeBtn = document.querySelector('.close-btn')
closeBtn.addEventListener('click', function(){
    this.parentElement.style.display ='none'
});



