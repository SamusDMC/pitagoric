const $ = require('jquery')

const UserSession = require('../models/UserSession')
const LoginView = require('../views/LoginView')
const helpers = require('../helpers')

$(function () {
  const userSession = new UserSession()
  const loginView = new LoginView({
    el: $('#form-login')
  })

  helpers.commonViews({
    header: {
      model: userSession
    }
  })
  helpers.headerBehavior()
  userSession.fetch()
})
