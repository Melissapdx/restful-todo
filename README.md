# Application Stack
Todo List implemented with a Restful API
Application:
python
flask
flask-restful

Database:
MongoDB
MongoEngine

Bridge:
Marshmellow

# Application Spec

TO DOs.

List Todos, Create Todos, Update/Delete Todos

Provide this via stack mentioned above, with a RESTful API.


# TODOs for the App

- Get Flask Working,
- Install Flask Restful
- Hello World with Flask Restful
- Install MongoDB, get MonoEngine to connect with it.
- Install Marshmellow


## Api Endpoints

/ (GET) - index, should return a list of all ToDos
/ (PUT) - should create a new TODO with given data.

/{id} (GET) - should return an individual ToDo that matches ID
/{id} (POST) - should update the ToDo that matches ID (with the fields we send)
/{id} (DELETE) - should delete the TODO at {id}
