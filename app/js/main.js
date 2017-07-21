const CheckPasswords = require('check-passwords')
const helpers = require('./helpers')
const Backbone = require('backbone')
const _ = require('underscore')
const { $ } = Backbone

$(function () {
  const route = helpers.normalizePath(window.location.pathname)

  switch (route) {
    case 'signup': {
      new CheckPasswords({
        onMatch: function () {
          this.target.onsubmit = null
        },
        onDontMatch: function () {
          window.alert('The password aren\'t equals')
          this.target.onsubmit = e => e.preventDefault()
        }
      }).watch()
    }
      break
    default:
      return false
  }
})
