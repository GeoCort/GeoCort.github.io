document.getElementById("mobileMenuBtn").addEventListener("click",()=>{
    let mobileMenu = document.getElementById("mobileMenu")
    if(mobileMenu.classList.contains("hidden")){
        mobileMenu.classList.remove("hidden")
        mobileMenu.classList.add("flex")
    }else{
        mobileMenu.classList.remove("flex")
        mobileMenu.classList.add("hidden")
    }
})