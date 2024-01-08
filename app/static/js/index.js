if (document.querySelector("header")) {
    //header animate
    var scrollPosition = 0;
    window.addEventListener('scroll', () => {
        let navbar = document.querySelector(".fade-navbar");

        if (window.scrollY > scrollPosition) {
            navbar.style.transform = "translateY(-100px)";
        } else {
            navbar.style.transform = "translateY(0)";
        }
        scrollPosition = window.scrollY;
    });
}
