const { View, $ } = require('../backbone')

module.exports = View.extend({
  events: {
    'submit': 'onSubmit'
  },
  onSubmit (event) {
    this.username = $('input[type=text]').val()
    this.password = $('input[type=password]').val()
    const base64Credentials = window.btoa(`${this.username}:${this.password}`)

    // Request for authenticate the user with HTTP BASIC-AUTH.
    $.ajax({
      method: event.target.method.toUpperCase(),
      url: event.target.action,
      beforeSend: function (request) {
        request.setRequestHeader('Authorization', `Basic ${base64Credentials}`)
      },
      success: this.successResponse.bind(this),
      error: this.errorResponse.bind(this)
    })

    event.preventDefault()
  },
  successResponse (response) {
    // Redirect to his profile.
    window.location = `/user/${this.username}`
  },
  errorResponse (request, response) {
    // Handle the unauthorized response.
    if (request.status === 401) {
      const { error, username } = JSON.parse(request.responseText)

      if (error === 'login') {
        if (username) {
          this.wrongPassword()
        } else {
          this.wrongUsername()
        }
      }
    }
  },
  wrongUsername () {
    console.log('Wrong username.')
  },
  wrongPassword () {
    console.log('Wrong password.')
  }
})
