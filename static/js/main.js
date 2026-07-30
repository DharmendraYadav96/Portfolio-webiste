// ===========================================
// Portfolio Main JavaScript
// ===========================================

document.addEventListener("DOMContentLoaded", () => {

    console.log("Portfolio Loaded");

    navbarScrollEffect();

    smoothScroll();

    scrollTopButton();

});


// ===========================================
// Navbar Background
// ===========================================

function navbarScrollEffect(){

    const navbar = document.querySelector(".custom-navbar");

    window.addEventListener("scroll",()=>{

        if(window.scrollY > 40){

            navbar.classList.add("navbar-scrolled");

        }

        else{

            navbar.classList.remove("navbar-scrolled");

        }

    });

}


// ===========================================
// Smooth Scroll
// ===========================================

function smoothScroll(){

    document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

        anchor.addEventListener("click",function(e){

            e.preventDefault();

            const target=document.querySelector(
                this.getAttribute("href")
            );

            if(target){

                target.scrollIntoView({

                    behavior:"smooth"

                });

            }

        });

    });

}


// ===========================================
// Scroll Top
// ===========================================

function scrollTopButton(){

    const button=document.getElementById("scrollTop");

    window.addEventListener("scroll",()=>{

        if(window.scrollY>300){

            button.classList.add("show");

        }

        else{

            button.classList.remove("show");

        }

    });

    button.addEventListener("click",()=>{

        window.scrollTo({

            top:0,

            behavior:"smooth"

        });

    });

}
// ======================================
// Fade Animation
// ======================================

const observer = new IntersectionObserver(entries=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

});

document.querySelectorAll(".fade-up").forEach(section=>{

    observer.observe(section);

});
// =============================
// Active Navigation on Scroll
// =============================

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".sidebar-menu a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 120;

        if(window.scrollY >= sectionTop){

            current = section.getAttribute("id");

        }

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if(link.getAttribute("href") === "#" + current){

            link.classList.add("active");

        }

    });

});