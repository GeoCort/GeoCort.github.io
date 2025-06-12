toggleMenu = document.getElementById("hamburger")
mobileMenu = document.getElementById("mobileNav")
openedMenuCloseBtn = document.getElementById("innerMenuClose")
toggleMenuFunc = ()=>{
    mobileMenu.classList.toggle("hidden")
    mobileMenu.classList.toggle("flex")
}
toggleMenu.addEventListener("click", toggleMenuFunc)
openedMenuCloseBtn.addEventListener("click", toggleMenuFunc)