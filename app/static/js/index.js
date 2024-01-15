import './jquery-3.7.1.min.js'

if ($("header")) {
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


if (window.matchMedia("(max-width: 992px)").matches) {
    $('.dropdown').each((i, e) => {
        e.onclick = () => {
            let dropDownMenu = $('.dropdown-menu')
            let display = dropDownMenu.css("display")
            let newDisplay = (display === 'none') ? 'block' : 'none'
            dropDownMenu.css("display", newDisplay)
        }
    })

    $('.dropdown-item').each((i, e) => {
        e.onclick = () => {
            $('.navbar-collapse').removeClass('show');
        }
    })
}

window.ajax_query = function (dish_id) {
    $.ajax({
        type: "get",
        url: `cart/add/${dish_id}/`,
        success: function (data) {
            update_values(data, dish_id)
        }
    });
    return false;
}

function update_values(data, dish_id) {
    let dish = $(`#dish_${dish_id}`)[0]
    let cart = data['cart']
    let total_price = get_total_price(cart)

    $('#total-price').text(`(${cart['total_price']}₽)`)
}

function get_total_price(cart) {
    let json = JSON.stringify(cart, null, 2)


    // cart.toJSON.forEach((k, v) => {
    //     console.log(`k:${k} - v:${v}`)
    // })
    return 10
}