const CheckPasswords = require('check-passwords')
const $ = require('jquery')

const UserSession = require('../models/UserSession')
const helpers = require('../helpers')

$(function () {
  const userSession = new UserSession()
  const checkpswds = new CheckPasswords({
    onMatch () {
      this.target.onsubmit = null
    },
    onDontMatch () {
      window.alert('The password aren\'t equals')
      this.target.onsubmit = e => e.preventDefault()
    }
  })

  helpers.commonViews({
    header: {
      model: userSession
    }
  })
  helpers.headerBehavior()
  userSession.fetch()
  checkpswds.watch()
})
