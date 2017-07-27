const { View, $ } = require('backbone')
const UserSession = require('../models/UserSession')
const helpers = require('../helpers')

module.exports = View.extend({
  initialize () {
    this.model = helpers.session(UserSession)

    if (helpers.sessionExists()) {
      this.render()
    } else {
      this.listenTo(this.model, 'change', this.render)
    }
  },
  render () {
    console.log(this.model.toJSON())

    $('#logout').click(function () {
      window.localStorage.removeItem('userSession')
    })
  }
})
