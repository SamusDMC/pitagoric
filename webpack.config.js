const path = require('path')

module.exports = {
  entry: './app/js/main.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'app/static/js')
  },
  resolve: {
    alias: {
      underscore: path.resolve(__dirname, 'node_modules/backbone/node_modules/underscore')
    }
  }
}
