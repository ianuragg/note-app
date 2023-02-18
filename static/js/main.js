// Set active to current page
jQuery(function ($) {
    var path = window.location.href;
    $('.nav_link').each(function () {
        if (this.href === path) {
            $(this).addClass('active');
        }
    });
    $('.footer_link').each(function () {
        if (this.href === path) {
            $(this).addClass('active');
        }
    });
});

// Navbar Toggler
document.addEventListener("DOMContentLoaded", function (event) {

    const showNavbar = (toggleId, navId, bodyId, headerId) => {
        const toggle = document.getElementById(toggleId),
            nav = document.getElementById(navId),
            bodypd = document.getElementById(bodyId),
            headerpd = document.getElementById(headerId)

        // Validate that all variables exist
        if (toggle && nav && bodypd && headerpd) {
            toggle.addEventListener('click', () => {
                // show navbar
                nav.classList.toggle('toggle-nav')

                // add padding to body
                bodypd.classList.toggle('body-padding')

            })
        }
    }

    showNavbar('header-toggle', 'nav-bar', 'body-pd', 'header')

    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')

    function colorLink() {
        if (linkColor) {
            linkColor.forEach(l => l.classList.remove('active'))
            this.classList.add('active')
        }
    }
    linkColor.forEach(l => l.addEventListener('click', colorLink))

});

//Change Theme
const themeToggler = document.querySelector(".theme-toggler");

const currentTheme = localStorage.getItem("theme");
if (currentTheme == "dark") {
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active-theme');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active-theme');
}
themeToggler.addEventListener("click", function () {
    document.body.classList.toggle("dark-theme-variables");

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active-theme');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active-theme');

    let theme = "light";
    if (document.body.classList.contains("dark-theme-variables")) {
        theme = "dark";
    }
    localStorage.setItem("theme", theme);
});


