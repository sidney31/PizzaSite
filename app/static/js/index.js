if (document.querySelector("header")) {
    //header animate
    let scrollPosition = 0;
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

if (window.matchMedia("(max-width: 992px)").matches) {
    let dropDown = document.querySelectorAll('.dropdown')
    dropDown.forEach(e => {
        e.onclick = () => {
            let dropDownMenu = e.querySelector('.dropdown-menu')

            // TODO: rewrite
            if (dropDownMenu.style.display === 'none')
                dropDownMenu.style.display = 'block'
            else
                dropDownMenu.style.display = 'none'
        }
    })
}
