const path = require('path')
const entries = require('./entries')

module.exports = {
  entry: entries,
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'app/static/js')
  }
}
