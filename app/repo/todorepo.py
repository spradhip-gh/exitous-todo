import psycopg2
from config import Config

class TodoRepo:
    def __init__(self):
        self.conn = psycopg2.connect(Config.DATABASE_URL)

    def create_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    completed BOOLEAN DEFAULT FALSE
                );
            """)
        self.conn.commit()

    def get_all_todos(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, title, completed FROM todos;")
            todos = cur.fetchall()
        return [{"id": row[0], "title": row[1], "completed": row[2]} for row in todos]
