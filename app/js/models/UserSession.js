const { Model } = require('../backbone')

module.exports = Model.extend({
  urlRoot: '/api/current_user'
})
