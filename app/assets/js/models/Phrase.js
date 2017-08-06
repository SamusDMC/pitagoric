const { Model } = require('../backbone')

const getRandomly = require('get-randomly')

module.exports = Model.extend({
  urlRoot: '/api/phrase',
  initialize () {
    if (typeof this.get('phrase') === 'undefined') {
      this.set('phrase', getRandomly(this.get('phrases')))
    }

    this.set('dedications', this.get('dedications').join(', '))
  }
})
