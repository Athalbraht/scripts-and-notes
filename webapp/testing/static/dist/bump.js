var __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

$(function() {
  var Bump;
  Bump = (function() {
    Bump.DEFAULTS = {
      lvl1: 1,
      lvl2: 2
    };

    function Bump() {
      var $B, _can_drag, _offset;
      $B = this;
      this.bumps = {
        center: $('.bump.bump-center'),
        left: $('.bump.bump-left'),
        right: $('.bump.bump-right'),
        all: $('.bump')
      };
      $(document).on('tap.bump click.bump', '[data-toggle="bump"]', function(event) {
        var target, _dir, _in;
        event.preventDefault();
        target = $(this.attributes['data-target'].nodeValue);
        if (target.length > 0) {
          _in = !target.hasClass('bump-in');
          _dir = target.hasClass('bump-left') ? "right" : "left";
          if (_in) {
            $B.bumps.left.css('zIndex', Bump.DEFAULTS.lvl1);
            $B.bumps.right.css('zIndex', Bump.DEFAULTS.lvl1);
            target.css('zIndex', Bump.DEFAULTS.lvl2).addClass('bump-in');
            return $B.bumps.center.removeClass("bump-in-" + ($B.flip(_dir))).addClass("bump-in-" + _dir);
          } else {
            $B.bumps.center.removeClass('bump-in-right bump-in-left');
            return $B.bumps[$B.flip(_dir)].removeClass('bump-in');
          }
        }
      });
      /*
      Optional touchSwipe features
      */

      if ($.fn.swipe) {
        _can_drag = false;
        _offset = 0;
        this.bumps.center.swipe({
          threshold: 20,
          swipeStatus: function(event, phase, direction, distance, duration, fingers) {
            var left, o, target, w, x;
            if (__indexOf.call(event.target.classList, 'bump-center') >= 0 || $(event.target).parent('.bump-center')) {
              switch (phase) {
                case 'start':
                  x = event.clientX;
                  o = $B.bumps.center.offset().left;
                  _offset = x - o;
                  w = $(window).width();
                  _can_drag = (x < w / 4 || x > w / 4 * 3) || o !== 0;
                  if (o === 0) {
                    $B.bumps.left.css('zIndex', Bump.DEFAULTS.lvl1);
                    return $B.bumps.right.css('zIndex', Bump.DEFAULTS.lvl1);
                  }
                  break;
                case 'move':
                  if (_can_drag && direction === 'left' || direction === 'right') {
                    left = event.clientX - _offset;
                    $B.bumps.center.addClass('bump-dragging');
                    if ($B.bumps.center.hasClass("bump-in-" + ($B.flip(direction)))) {
                      target = $B.bumps[direction];
                    } else {
                      target = $B.bumps[$B.flip(direction)];
                    }
                    if (Math.abs(left) > target.width()) {
                      return;
                    }
                    $B.bumps.center.css('left', left);
                    return target.addClass('bump-in').css('zIndex', Bump.DEFAULTS.lvl2);
                  }
                  break;
                case 'end':
                  $B.bumps.center.removeClass('bump-dragging');
                  left = event.clientX - _offset;
                  $B.bumps.center.removeAttr('style');
                  if (direction != null) {
                    if ($B.bumps.center.hasClass("bump-in-" + ($B.flip(direction)))) {
                      $B.bumps.center.removeClass('bump-in-right bump-in-left');
                      $B.bumps.right.removeClass('bump-in');
                      return $B.bumps.left.removeClass('bump-in');
                    } else {
                      $B.bumps.center.removeClass('bump-dragging');
                      if (Math.abs(left) > 50) {
                        target = $B.bumps[$B.flip(direction)];
                        left = target.width();
                        return $B.bumps.center.addClass("bump-in-" + direction);
                      } else {
                        $B.bumps.center.removeClass('bump-in-right bump-in-left');
                        $B.bumps.right.removeClass('bump-in');
                        return $B.bumps.left.removeClass('bump-in');
                      }
                    }
                  } else if ($B.bumps.center.hasClass("bump-in-left") || $B.bumps.center.hasClass("bump-in-right")) {
                    $B.bumps.center.removeClass('bump-in-right bump-in-left');
                    $B.bumps.right.removeClass('bump-in');
                    return $B.bumps.left.removeClass('bump-in');
                  }
              }
            }
          }
        });
      }
    }

    Bump.prototype.flip = function(dir) {
      if (dir === "left") {
        return "right";
      } else {
        return "left";
      }
    };

    return Bump;

  })();
  return new Bump();
});
