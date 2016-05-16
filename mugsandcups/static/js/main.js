$(document).ready(function() {
    
    $('.testimonials div').eq(Math.floor((Math.random() * $('.testimonials div').length))).show();

    setInterval(function() {
        var $items = $('.testimonials div');
        var $currentItem = $items.filter(':visible');
        var currentIndex = $currentItem.index();
        var nextIndex = currentIndex;
        while (nextIndex == currentIndex) {
            nextIndex = Math.floor((Math.random() * $items.length));
        }
        $currentItem.fadeOut(1000, function() {
            $items.eq(nextIndex).fadeIn(1000);
        });
    }, 4000);

});