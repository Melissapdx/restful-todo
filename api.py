from flask import Flask, request
from flask_restful import Resource, Api, abort
from model import TodoItem, TodoItemSchema

app = Flask(__name__)
api = Api(app)

def serialize_todo(todo):
    schema = TodoItemSchema()
    result = schema.dump(todo)
    return result


class ToDos(Resource):
    # Will return ALL todos, OR todos that match id.
    def get(self, id=None):
        if id is None:
            todo = TodoItem.objects
            schema = TodoItemSchema(many=True)
            result = schema.dump(todo)
            return result
        else:
            try:
                todo = TodoItem.objects(id=id).first()
                return serialize_todo(todo)
            except Exception as e:
                abort(404, message="No Todo with that ID")

    # Creates ToDos
    def post(self, id=None):
        if id is not None:
            abort(401,message="Please use Put to update items")

        task = request.form['task']
        new_todo = TodoItem(task=task).save()
        return serialize_todo(new_todo)

    # Updates ToDos
    def put(self, id=None):
        try:
            todo = TodoItem.objects(id=id).first()
        except Exception as e:
            abort(404, message="No Todo with that ID")
        if 'task' in request.form:
            todo.task = request.form['task']
        if 'completed' in request.form:
            todo.completed = True if request.form['completed'] == 'True' else False
        todo.save()
        return serialize_todo(todo)



    # Deletes ToDos
    def delete(self, id=None):
        if id is None:
            abort(404, message="Not a valid Todo item to delete")
        else:
            todo_to_delete = TodoItem.objects(id=id).first()
            todo_to_delete.delete()
            return "Item was successfully deleted"


api.add_resource(ToDos, "/", '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
