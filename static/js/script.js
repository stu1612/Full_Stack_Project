$(document).ready(function() {

    $("p").on({
        mouseenter: function() {
            $(this).css("color", "black");
        },
    });

    $(".drop_btn").mouseenter(function() {
        $("#panel, #panel_2, #panel_3").slideToggle("slow");
    });

    $(".drop_btn").mouseleave(function() {
        $("#panel, #panel_2, #panel_3").slideToggle("slow");
    });

    $(".drop_btn").on({
        mouseenter: function() {
            $('.input_search, .cart, .projects').css("background-color", "yellow"), 2000;
        },
    });

    $(".drop_btn").on({
        mouseleave: function() {
            $('.input_search, .cart, .projects').css("background-color", "white");
        },
    });
});