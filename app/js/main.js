const CheckPasswords = require('check-passwords');
const helpers = require('./helpers');

window.onload = function () {
  const route = helpers.normalizePath(location.pathname);

  switch (route) {
    case 'signup': {
      new CheckPasswords({
        onMatch: function () {
          this.target.onsubmit = null;
        },
        onDontMatch: function () {
          alert('The password aren\'t equals');
          this.target.onsubmit = e => e.preventDefault();
        }
      }).watch();
    }
      break;
    default:
      return false;
  }

  console.log(`Hello, PI ${Math.PI}`);
};
