$(function () {
    // 为了隐藏滚动条
    $('.home').width(innerWidth)



    var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        loop: true,
        paginationClickable: true,
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false
    });

        var mustbuySwiper = new Swiper('#mustbuySwiper', {
        spaceBetween: 3,
        loop: true,
        slidesPerView: 3,
    });
})
