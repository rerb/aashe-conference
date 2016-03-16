$(function(){
    $('.dropdown').hover(function() {
        $(this).addClass('open');
    },
    function() {
        $(this).removeClass('open');
    });
});


function getTimeRemaining(endtime) {
  var t = Date.parse(endtime) - Date.parse(new Date());
  return Math.floor(t / 1000)
}
var clock = $('.clock').FlipClock(
        Math.floor((Date.parse(new Date("2016-10-9")) - Date.parse(new Date()))/1000), {
    clockFace: 'DailyCounter',
    countdown: true,
    showSeconds: false
});
