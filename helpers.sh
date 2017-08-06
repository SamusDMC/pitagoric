#!/usr/bin/env bash
# Shell helpers.

# Copy font-awesome to app/static/fonts.
fa_cp () {
  fa_path_src='app/assets/scss/tools/vendor/font-awesome/fonts'
  fa_path_dest='app/static/fonts'

  cp $fa_path_src/* "$fa_path_dest"
}

fa_cp
