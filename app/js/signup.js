const CheckPasswords = require('check-passwords')
const $ = require('jquery')

const helpers = require('./helpers')

$(window).load(function () {
  helpers.checkLocalStorage()
})

$(function () {
  new CheckPasswords({
    onMatch: function () {
      this.target.onsubmit = null
    },
    onDontMatch: function () {
      window.alert('The password aren\'t equals')
      this.target.onsubmit = e => e.preventDefault()
    }
  }).watch()
})
