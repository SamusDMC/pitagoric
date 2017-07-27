const Backbone = require('backbone')
const _ = require('underscore')

const ProfileView = require('./views/ProfileView')

const { $ } = Backbone

// Routing with the pathname.
$(function () {
  const profileView = new ProfileView()
})
