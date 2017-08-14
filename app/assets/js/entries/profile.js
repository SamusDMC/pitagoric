const Backbone = require('../backbone')
const _ = require('underscore')

const ProfileView = require('../views/ProfileView')
const helpers = require('../helpers')

const { $ } = Backbone

$(function () {
  const profileView = new ProfileView()

  helpers.commonViews({
    header: {
      model: profileView.model
    }
  })
  helpers.headerBehavior()
})
