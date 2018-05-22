new ClipboardJS('.btn-copy');

$(window).scroll(function () {
    var topOfDiv = $('#header_wrap').offset().top;
    var height = $('#header_wrap').outerHeight();
    if ($(window).width() > 700) {
        if ($(window).scrollTop() > (topOfDiv + height)) {
            $(".trigger").addClass("stuck");
            $("#header_wrap").addClass("stuck");
        } else {
            $(".trigger").removeClass("stuck");
            $("#header_wrap").removeClass("stuck");
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

$('.navbar-toggle').on('click', function () {
    $('.trigger').toggleClass('trigger-mobile');
    $('#mobile_links').fadeToggle(200);
    $('#mobile_links').css("display", "inline");
});

$('.live-deploy-table').on('show.bs.collapse', function () {
    $(".collapse.show")
        .not(this)
        .collapse('toggle');
});

$(document).ready(function () {
    $('.live-deploy-table tr').on('shown.bs.collapse', function () {
        $(this).prev().find(".plus-icon").html('<i class="fas fa-minus fa-lg"></i>');
    });
    
    $('.live-deploy-table tr').on('hidden.bs.collapse', function () {
        $(this).prev().find(".plus-icon").html('<i class="fas fa-plus fa-lg"></i>');
    });
});