$(function(){
    $('.dropdown').hover(function() {
        $(this).addClass('open');
    },
    function() {
        $(this).removeClass('open');
    });
});

$(document).ready(function(){
    $('[data-toggle="popover"]').popover({trigger:"hover"});
});
