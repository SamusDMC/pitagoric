const { View, $ } = require('../backbone')
const _ = require('underscore')
const getRandomly = require('get-randomly')

const Phrases = require('../collections/Phrases')

module.exports = View.extend({
  initialize () {
    this.template = _.template($('#phrase-tmp').html())
    this.collection = new Phrases()

    this.collection.fetch({
      data: {
        lang: $('html').attr('lang')
      },
      success: this.collectionSuccess.bind(this)
    })
  },
  collectionSuccess () {
    this.render()
  },
  intervalPhrasesCb () {
    const randomPhrase = getRandomly(this.collection.toJSON())

    if (this.$el.html() !== '') {
      this.$el.empty()
    }

    this.$el.html(this.template(randomPhrase))
  },
  render () {
    this.intervalPhrasesCb()
    this.intervalPhrases = setInterval(this.intervalPhrasesCb.bind(this), 10000)
  }
})
