module.exports = {
  // ...
}

// Resolve the problem with the context (is by webpack).
Object.keys(module.exports).forEach(function (key) {
  if (typeof module.exports[key] === 'function') {
    module.exports[key] = module.exports[key].bind(module.exports)
  }
})
