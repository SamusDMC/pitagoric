const { View, $ } = require('../backbone')
const _ = require('underscore')
const getRandomly = require('get-randomly')

const Phrases = require('../collections/Phrases')
const Phrase = require('../models/Phrase')

module.exports = View.extend({
  initialize () {
    const thisView = this;

    this.collection = new Phrases()

    this.collection.fetch({
      data: {
        lang: $('html').attr('lang')
      },
      success: function () {
        thisView.render()
      }
    })
  },
  intervalPhrasesCb () {
    const randomPhrase = getRandomly(this.collection.toJSON())
    const phraseTemplate = _.template($('#phrase-tmp').html())

    if ($('#phrases-container').html() !== '') {
      $('#phrases-container').empty()
    }
    $('#phrases-container').append(phraseTemplate(randomPhrase))
  },
  render () {
    this.intervalPhrasesCb()
    this.intertalPhrases = setInterval(this.intervalPhrasesCb.bind(this), 10000)
  }
})
