const { Model } = require('../backbone')

const getRandomly = require('get-randomly')

module.exports = Model.extend({
  parse (response) {
    const dedicationsArr = response.dedications

    if (typeof response.phrase === 'undefined') {
      const randomlyPhrase = getRandomly(response.phrases)

      response.phrase = randomlyPhrase
    }

    let dedications = ''

    if (dedicationsArr.length > 1) {
      dedicationsArr.forEach(function (dedication, index, arr) {
        if (index === (arr.length - 1)) {
          dedications += ` & ${dedication}`
        } else {
          if (index === 0) {
            dedications += `${dedication}`
          } else {
            dedications += `, ${dedication}`
          }
        }
      })
    } else {
      dedications = dedicationsArr[0]
    }

    response.dedications = dedications

    return response
  }
})
