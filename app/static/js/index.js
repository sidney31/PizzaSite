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

window.ajax_query = function (dish_id, quantity = 0) {

    let url = `cart/add/${dish_id}/`
    if (quantity !== 0)
        url = `cart/remove/${dish_id}/${quantity}`

    $.ajax({
        type: 'get',
        url: url,
        success: function (data) {
            update_values(data, dish_id)
        }
    });
}

function update_values(data, dish_id) {
    let cart = data['cart']
    let total_price = data['total_price']

    let quantity_int = 0;

    if (cart[dish_id])
        quantity_int = cart[dish_id]['quantity']

    $('#total-price').text(`(${total_price}₽)`)
    let quantity_block = $(`#dish_${dish_id} #quantity`).get(0)
    $(quantity_block).text(quantity_int)

    let editCart = $(`#dish_${dish_id} #edit_cart`).get(0)
    let inCart = $(`#dish_${dish_id} #in_cart`).get(0)

    if (quantity_int > 0) {
        $(editCart).removeClass('d-none')
        $(inCart).addClass('d-none')
    } else {
        $(editCart).addClass('d-none')
        $(inCart).removeClass('d-none')
    }
}
