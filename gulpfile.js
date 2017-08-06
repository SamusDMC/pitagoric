const gulp = require('gulp')
const sass = require('gulp-sass')
const webpack = require('webpack-stream')
const babel = require('gulp-babel')
const uglyfly = require('gulp-uglyfly')
const size = require('gulp-size')

const sourcemaps = require('gulp-sourcemaps')
const imagemin = require('gulp-imagemin')

const webpackConfig = require('./webpack.config.js')

// Webpack development version.
if (process.env.DEV) {
  webpackConfig.devtool = 'source-map'
}

gulp.task('scss', function () {
  gulp.src('./app/assets/scss/main.scss')
    .pipe(sass({ outputStyle: 'compressed' }))
    .pipe(size({ title: 'After compressed' }))
    .pipe(gulp.dest('./app/static/css'))
})

gulp.task('webpack-dev', function () {
  gulp.src('./app/assets/js/')
    .pipe(babel())
    .pipe(webpack(webpackConfig))
    .pipe(size())
    .pipe(gulp.dest('./app/static/js'))
})

gulp.task('webpack', function () {
  gulp.src('./app/assets/js/')
    .pipe(webpack(webpackConfig))
    .pipe(babel())
    .pipe(uglyfly())
    .pipe(size('After uglyfly'))
    .pipe(gulp.dest('./app/static/js'))
})

gulp.task('imagemin', function () {
  gulp.src('./app/assets/images/*')
    // .pipe(imagemin())
    .pipe(gulp.dest('./app/static/images'))
})

gulp.task('default', ['scss', 'webpack', 'imagemin'])

gulp.task('watch-js', function () {
  gulp.watch(['./app/assets/js/**/*.js'], ['webpack-dev'])
})

gulp.task('watch-scss', function () {
  gulp.watch(['./app/assets/scss/**/*.scss'], ['scss'])
})
