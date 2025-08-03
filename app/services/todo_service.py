from ..models import Todo
from ..db import db

class TodoService:
    @staticmethod
    def get_all_todos():
        return Todo.query.all()

    @staticmethod
    def get_todo_by_id(todo_id):
        return Todo.query.get_or_404(todo_id)

    @staticmethod
    def create_todo(data):
        if not data or not 'title' in data:
            return None, "Title is required"
        
        new_todo = Todo(title=data['title'], completed=data.get('completed', False))
        
        db.session.add(new_todo)
        db.session.commit()
        
        return new_todo, None

    @staticmethod
    def update_todo(todo_id, data):
        todo = Todo.query.get_or_404(todo_id)
        
        todo.title = data.get('title', todo.title)
        todo.completed = data.get('completed', todo.completed)
        
        db.session.commit()
        
        return todo

    @staticmethod
    def delete_todo(todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
