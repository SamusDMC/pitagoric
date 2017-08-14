const { Collection } = require('../backbone')

const Phrase = require('../models/Phrase')

module.exports = Collection.extend({
  url: '/api/phrases',
  model: Phrase
})
