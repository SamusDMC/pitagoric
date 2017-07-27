const Backbone = require('backbone')

module.exports = Backbone.Model.extend({
  urlRoot: '/api/get_session',
  createSession () {
    const userStringify = JSON.stringify(this.toJSON())

    window.localStorage.setItem('userSession', userStringify)
  }
})
