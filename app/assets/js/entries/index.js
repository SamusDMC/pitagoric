const $ = require('jquery')
const _ = require('underscore')

const UserSession = require('../models/UserSession')
const PhraseView = require('../views/PhraseView')
const helpers = require('../helpers')

$(function () {
  const userSession = new UserSession()
  const phraseView = new PhraseView({
    el: '#phrases-container'
  })

  helpers.commonViews({
    header: {
      model: userSession
    }
  })
  helpers.headerBehavior()
  userSession.fetch()
})
