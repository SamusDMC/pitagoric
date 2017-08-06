const $ = require('jquery')

const helpers = require('../helpers')

$(window).on('load', function () {
  $('#form-login').on('submit', function (event) {
    const username = $('input[type=text]').val()
    const password = $('input[type=password]').val()
    const base64Credentials = window.btoa(`${username}:${password}`)

    // Request for authenticate the user with HTTP BASIC-AUTH.
    $.ajax({
      method: event.target.method.toUpperCase(),
      url: event.target.action,
      beforeSend: function (request) {
        request.setRequestHeader('Authorization', `Basic ${base64Credentials}`)
      },
      success: function (response) {
        // Redirect to his profile.
        window.location = `/user/${username}`
      },
      error: function (request, response) {
        // Handle the unauthorized response.
        if (request.status === 401) {
          const { error, username } = JSON.parse(request.responseText)

          if (error === 'login') {
            if (username) {
              // The password is wrong.
            } else {
              // The username is wrong.
            }
          }
        }
      }
    })

    event.preventDefault()
  })
})
