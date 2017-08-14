const HeaderAuthView = require('./views/HeaderAuthView')
const $ = require('jquery')

module.exports = {
  commonViews (config = {}) {
    const { header } = config

    // Header auth view.
    new HeaderAuthView({
      el: header.el || '#header-auth',
      model: header.model
    })
  },
  // Function for set the header behavior.
  headerBehavior () {
    const bodyHeight = window.document.body.clientHeight
    const windowInnerHeight = window.innerHeight
    const $header = $('header')

    if (bodyHeight > windowInnerHeight) {
      $(window).on('scroll', function () {
        if (this.pageYOffset > 100) {
          $header.removeClass('fadeOutDown-1s')
          $header.addClass('fadeInDownBig-1s')
          $header.show()
        } else {
          $header.removeClass('fadeInDownBig-1s')
          $header.addClass('fadeOutDown-1s')

          setTimeout(function () {
            $header.hide()
          }, 1000)
        }
      })
    } else {
      $header.show()
      $header.css('position', 'static')
    }

    $('#btn-toggle-menu i').click(function () {
      const $navList = $header.find('ul')
      const leftValue = $navList.css('left')

      if (leftValue === '0px') {
        $navList.animate({
          left: '-100%'
        })
      } else {
        $navList.animate({
          left: '0'
        })
      }
    })
  }
}

// Resolve the problem with the context (is by webpack).
Object.keys(module.exports).forEach(function (key) {
  if (typeof module.exports[key] === 'function') {
    module.exports[key] = module.exports[key].bind(module.exports)
  }
})
