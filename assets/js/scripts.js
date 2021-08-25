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


(function(document, history, location) {
    var HISTORY_SUPPORT = !!(history && history.pushState);
  
    var anchorScrolls = {
      ANCHOR_REGEX: /^#[^ ]+$/,
      OFFSET_HEIGHT_PX: 54,
  
      /**
       * Establish events, and fix initial scroll position if a hash is provided.
       */
      init: function() {
        this.scrollToCurrent();
        $(window).on('hashchange', $.proxy(this, 'scrollToCurrent'));
        $('body').on('click', 'a', $.proxy(this, 'delegateAnchors'));
      },
  
      /**
       * Return the offset amount to deduct from the normal scroll position.
       * Modify as appropriate to allow for dynamic calculations
       */
      getFixedOffset: function() {
        return this.OFFSET_HEIGHT_PX;
      },
  
      /**
       * If the provided href is an anchor which resolves to an element on the
       * page, scroll to it.
       * @param  {String} href
       * @return {Boolean} - Was the href an anchor.
       */
      scrollIfAnchor: function(href, pushToHistory) {
        var match, anchorOffset;
  
        if(!this.ANCHOR_REGEX.test(href)) {
          return false;
        }
  
        match = document.getElementById(href.slice(1));
  
        if(match) {
          anchorOffset = $(match).offset().top - this.getFixedOffset();
          $('html, body').animate({ scrollTop: anchorOffset});
  
          // Add the state to history as-per normal anchor links
          if(HISTORY_SUPPORT && pushToHistory) {
            history.pushState({}, document.title, location.pathname + href);
          }
        }
  
        return !!match;
      },
      
      /**
       * Attempt to scroll to the current location's hash.
       */
      scrollToCurrent: function(e) { 
        if(this.scrollIfAnchor(window.location.hash) && e) {
            e.preventDefault();
        }
      },
  
      /**
       * If the click event's target was an anchor, fix the scroll position.
       */
      delegateAnchors: function(e) {
        var elem = e.target;
  
        if(this.scrollIfAnchor(elem.getAttribute('href'), true)) {
          e.preventDefault();
        }
      }
    };
  
      $(document).ready($.proxy(anchorScrolls, 'init'));
  })(window.document, window.history, window.location);
  