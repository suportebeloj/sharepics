let navbar = $('.navbar.navbar-expand-lg.navbar-dark.fixed-top')
let ishare = $('#ishare')

$(window).scroll(() => {
    if ($(this).scrollTop() > 300) {
        navbar.removeClass('navbar-dark')
        navbar.addClass('navbar-light bg-light border-bottom')
        ishare.addClass('dark')

    }
    else {
        navbar.addClass('navbar-dark')
        navbar.removeClass('navbar-light bg-light border-bottom')
        ishare.removeClass('dark')
    }
})