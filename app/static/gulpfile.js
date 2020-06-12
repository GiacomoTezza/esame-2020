var gulp        = require('gulp');
var concat      = require('gulp-concat');
var uglify      = require('gulp-uglify');
var jshint      = require('gulp-jshint');

gulp.task('minification', function () {
    gulp.src(['dynamitable.jquery.js'])
        .pipe(uglify())
        .pipe(concat('dynamitable.jquery.min.js'))
        .pipe(gulp.dest('./'))
    ;
});

gulp.task('lint', function () {
    gulp.src(['dynamitable.jquery.js'])
        .pipe(jshint())
        .pipe(jshint.reporter());
});

gulp.task('watch', function () {
    gulp.watch(['dynamitable.jquery.js'], ['minification', 'lint']);
});

gulp.task('default', ['watch']);