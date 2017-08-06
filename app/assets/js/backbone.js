const Backbone = require('backbone')
const Cookies = require('js-cookie')

// Overwrite sync function for handle errors.
Backbone.sync = (function (syncFunc) {
  return function (method, model, options) {
    options = options || {}

    const { beforeSend, error } = options

    // Add headers.
    options.beforeSend = function (request) {
      request.setRequestHeader('withCredentials', true)

      if (beforeSend) {
        return beforeSend.apply(this, arguments)
      }
    }

    // Handle unauthorized error (401).
    options.error = function (request, response, errorThrown) {
      if (error) {
        error.call(options.context, request, response, errorThrown)
      }

      if (request.status === 401) {
        const { error, expired, exist } = JSON.parse(request.responseText)

        // When the error is by the token.
        if (error === 'token') {
          // When exist and is expired.
          if (exist && expired) {
            Cookies.remove('token')
          }

          window.location = '/login'
        }
      }
    }

    return syncFunc.apply(this, arguments)
  }
})(Backbone.sync)

module.exports = Backbone
