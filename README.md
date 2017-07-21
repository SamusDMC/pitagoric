# Math Blog

¿What is Math Blog?, well i will attempt build a site for learn much stuff of mathematics.

This is under construction, if you have one idea please send me a message to morenoricardo237@gmail.com.

## Installation

1.  Clone the repo.
2.  Install the dependencies for the front-end with `npm i & bower install`.
3.  Install the dependencies for the back-end, please see the requeriments bellow.

## Requeriments

-   npm & bower (as manager of modules).
-   webpack (as bundler).
-   gulpjs (as task automation).

### For the front-end

Javascript:

-   backbone.
-   underscore.
-   jquery.
-   prosemirror.
-   checkpasswords.

CSS:

-   flexboxgrid.
-   mixins.scss.

### For the back-end

Python:

-   flask.
-   flask-via.
-   flask-compress.
-   flask-sqlalchemy.

## List of models

-   User.
-   Post.
-   Post category.

## TODO list

* [ ] Create DER.
* [ ] Create all models.
* [ ] Test the models.
* [ ] Create the API.
  * [ ] User service.
  * [ ] Post service.
* [ ] Test the API.

## Debug

For debug the project execute the file `debug.sh`, if you need run the server in a specific port then execute with the port as parameter. With port: `./debug.sh 8081`.

## Build the assets.

For build the assets just run `gulp`.
