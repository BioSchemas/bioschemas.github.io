/**
 * Enabling CLipboard
 */

new ClipboardJS('.btn-copy');

/**
 * Heading animation
 */

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


/**
 * Topnav over headings fix
 */

(function (document, history, location) {
  var HISTORY_SUPPORT = !!(history && history.pushState);
  var anchorScrolls = {
    ANCHOR_REGEX: /^#[^ ]+$/,
    OFFSET_HEIGHT_PX: 54,
    init: function () {
      this.scrollToCurrent();
      $(window).on('hashchange', $.proxy(this, 'scrollToCurrent'));
      $('body').on('click', 'a', $.proxy(this, 'delegateAnchors'));
    },
    getFixedOffset: function () {
      return this.OFFSET_HEIGHT_PX;
    },
    scrollIfAnchor: function (href, pushToHistory) {
      var match, anchorOffset;
      if (!this.ANCHOR_REGEX.test(href)) {
        return false;
      }
      match = document.getElementById(href.slice(1));
      if (match) {
        anchorOffset = $(match).offset().top - this.getFixedOffset();
        $('html, body').animate({ scrollTop: anchorOffset });
        if (HISTORY_SUPPORT && pushToHistory) {
          history.pushState({}, document.title, location.pathname + href);
        }
      }
      return !!match;
    },
    scrollToCurrent: function (e) {
      if (this.scrollIfAnchor(window.location.hash) && e) {
        e.preventDefault();
      }
    },
    delegateAnchors: function (e) {
      var elem = e.target;

      if (this.scrollIfAnchor(elem.getAttribute('href'), true)) {
        e.preventDefault();
      }
    }
  };
  $(document).ready($.proxy(anchorScrolls, 'init'));
})(window.document, window.history, window.location);

/**
 * Scroll to top
 */

var toggleHeight = $(window).outerHeight() / 3;

$(window).scroll(function () {
  if ($(window).scrollTop() > toggleHeight) {
    //Adds active class to make button visible
    $(".top_link").addClass("visible");

  } else {
    //Removes active class to make button visible
    $(".top_link").removeClass("visible");
  }
});

//Scrolls the user to the top of the page again
$(".top_link").click(function () {
  $("html, body").animate({ scrollTop: 0 }, "slow");
  return false;
});

/**
 * Activate tooltips
 */

 $(function () {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl, {
      animation: false
    })
  })
})

