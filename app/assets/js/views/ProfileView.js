const { View } = require('../backbone')

const UserSession = require('../models/UserSession')
const helpers = require('../helpers')

module.exports = View.extend({
  initialize () {
    this.model = new UserSession()

    this.model.fetch()
    this.listenTo(this.model, 'change', this.render)
  },
  render () {
    console.log(this.model.toJSON())
  }
})
