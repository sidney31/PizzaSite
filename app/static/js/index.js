import './jquery-3.7.1.min.js'

if ($("header")) {
    //header animate
    let scrollPosition = 0;
    $(window).scroll(() => {
        let navbar = $(".fade-navbar");

        if ($(window).scrollTop() > scrollPosition)
            navbar.css("translateY", "-100px");
        else
            navbar.css("translateY", "0");

        scrollPosition = $(window).scrollTop()
    });
}

//dropdown for mobile
if (window.matchMedia("(max-width: 992px)").matches) {
    $('.dropdown').each((i, e) => {
        e.onclick = () => {
            let dropDownMenu = $('.dropdown-menu')
            let display = dropDownMenu.css("display")
            let newDisplay = (display === 'none') ? 'block' : 'none'
            dropDownMenu.css("display", newDisplay)
        }
    })
}
