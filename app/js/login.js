const $ = require('jquery')

const helpers = require('./helpers')

$(window).load(function () {
  helpers.checkLocalStorage()
})

$(function () {
  console.log('Log-in')
})
