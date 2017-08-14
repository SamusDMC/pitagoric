const { View, $ } = require('../backbone')
const _ = require('underscore')

module.exports = View.extend({
  initialize () {
    this.template = _.template($('#header-auth-tmp').html())

    this.listenTo(this.model, 'change', this.render)
  },
  render () {
    const { username, profile_image } = this.model.toJSON()
    const content = this.template({ username, profile_image })

    this.$el.append(content)
  }
})
