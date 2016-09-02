

$(window).scroll(function() {
    var topOfDiv = $('#header_wrap').offset().top;
    var height = $('#header_wrap').outerHeight();
    if ($(window).width() > 700) {
        if ($(window).scrollTop() > (topOfDiv + height)) {
            $(".trigger").addClass("stuck");
        } else {
            $(".trigger").removeClass("stuck");
        }
    }
});

function synchTab(frameName) {
    var elList, i;

    if (frameName == null) {
        return;
    }

    elList = document.getElementsByTagName("a");
    for (i = 0; i < elList.length; i++) {
        if (elList[i].target == frameName) {
            if (elList[i].href == window.frames[frameName].location.href) {
                elList[i].className += " activeTab";
                elList[i].blur();
            } else {
                removeName(elList[i], "activeTab");
            }
        }
    }
}

function removeName(el, name) {
    var i, curList, newList;

    newList = [];
    curList = el.className.split(" ");
    for (i = 0; i < curList.length; i++) {
        if (curList[i] != name) {
            newList.push(curList[i]);
        }
    }
    el.className = newList.join(" ");
}

$('.mobile_nav').on('click', function () {
    $('.trigger').toggleClass('trigger_mobile');
    $('#mobile_links').fadeToggle(200);
    $('#mobile_links').css("display", "inline");
});

/**
$('#mobile_nav').click(function () {
    $header = $(this);
    $content = $header.next();
    $('.trigger').toggleClass('trigger_mobile');
    $content.slideToggle(400);
})
*/

/**
$(document).ready(function () {
    $('.eachExample').find('.insideExample').hide();

    $('.h3Example').on({
        mouseenter: function() {
            //$(this).css('color', '#0B794B');
            $(this).css('cursor', 'pointer');
        }
    });

    $('.h3Example').on('click', function () {
        $(this).toggleClass('activeExample');
        $(this).siblings('.insideExample').toggle(400);
    });

    $('.h3Example').tooltip({
        position: { my: "right-10% bottom-15%" },
    });
});
*/
