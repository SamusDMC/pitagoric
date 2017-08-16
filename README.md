# Pitagoric

¿What is **Pitagoric**?, well i will attempt build a site for learn much stuff of mathematics.

This is under construction, if you have one idea please send me a message to morenoricardo237@gmail.com.

## Installation

1.  Clone the repo.
2.  Install the dependencies for the front-end with `npm install & bower install`.
3.  Install the dependencies for the back-end with `sudo pip install -r requeriments.txt`.

## List of models

-   User.
-   Post.
-   Post category.
-   Post Comments.

## TODO list

* [ ] Create all models.
* [ ] Create DER.
* [x] Test the models.
* [ ] Create the API.
  * [x] User service.
  * [x] Phrases service.
  * [x] Post service.
  * [x] Post category service.
* [ ] Test the API.

## Build

For build the assets just run `gulp`.

### Tasks

Execute the file `helpers.sh` for make a set of task (important).

## Run & Debug

Run the project in normal mode with `./run.py`. The default port is `8080`.

For debug the project execute the file `debug.sh`, if you need run the server in a specific port then execute with the port as parameter. With port: `./debug.sh 8081`.

## Test

You should have `nose2` installed to test this app. For test the app just run `nose2`.
