from flask import request, jsonify
from . import todos_bp
from ..services.todo_service import TodoService

# Create a new todo
@todos_bp.route('/', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo, error = TodoService.create_todo(data)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(new_todo.to_dict()), 201

# Get all todos
@todos_bp.route('/', methods=['GET'])
def get_todos():
    todos = TodoService.get_all_todos()
    return jsonify([todo.to_dict() for todo in todos])

# Get a single todo
@todos_bp.route('/<int:id>', methods=['GET'])
def get_todo(id):
    todo = TodoService.get_todo_by_id(id)
    return jsonify(todo.to_dict())

# Update a todo
@todos_bp.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    todo = TodoService.update_todo(id, data)
    return jsonify(todo.to_dict())

# Delete a todo
@todos_bp.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    TodoService.delete_todo(id)
    return '', 204
