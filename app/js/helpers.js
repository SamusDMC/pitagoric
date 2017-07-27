module.exports = {
  getSession () {
    const localStorageSession = window.localStorage.getItem('userSession')

    let userSessionData

    try {
      userSessionData = JSON.parse(localStorageSession)
    } catch (err) {
      // Custom error.
      throw new Error('The user session has been a stringify object.')
    }

    return userSessionData
  },
  sessionExists () {
    return window.localStorage.getItem('userSession') !== null
  },
  session (UserSession) {
    if (this.sessionExists()) {
      return new UserSession(this.getSession())
    } else {
      const user = new UserSession()

      user.fetch()
      user.on('change', user.createSession, user)

      return user
    }
  },
  checkLocalStorage () {
    if (this.sessionExists()) {
      window.localStorage.removeItem('userSession')
    }
  }
}

// Resolve the problem with the context (is by webpack).
Object.keys(module.exports).forEach(function (key) {
  module.exports[key] = module.exports[key].bind(module.exports)
})
