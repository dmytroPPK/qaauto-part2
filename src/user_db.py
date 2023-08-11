from dataclasses import dataclass
from src.base_db import BaseDb


@dataclass
class User:
    name: str
    age: int
    email: str
    id: int = 0


class UserDb(BaseDb):
    def __init__(self, db_path):
        super().__init__(db_path)
        self.connect()
        self._create_users_table()

    def __del__(self):
        if self.connection:
            self.close()

    def _create_users_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT
            );
        '''
        self.execute(create_table_query)

    def add_user(self, new_user: User):
        query = '''
            INSERT INTO users (name, age, email) VALUES (?, ?, ?);
        '''
        self.execute(query, tuple(new_user.__dict__.values())[0:3])

    def get_users(self) -> [User]:
        query = '''
            SELECT name, age, email, id FROM users;
        '''
        result = self.fetch_all(query)
        list_users = [User(*row) for row in result]
        return list_users

    def get_user_by_id(self, user_id: int) -> User:
        query = '''
            SELECT name, age, email, id FROM users WHERE id = ?;
        '''
        rows = self.fetch_all(query, (user_id,))
        result = User(*rows[0]) if len(rows) > 0 else None
        return result

    def update_user_by_id(self, user_to_update: User):
        query = '''
            UPDATE users SET name = ?, age = ?, email = ? WHERE id = ?;
        '''
        self.execute(query, tuple(user_to_update.__dict__.values()))

    def delete_user_by_id(self, user_id: int):
        delete_query = '''
            DELETE FROM users WHERE id = ?;
        '''
        self.execute(delete_query, (user_id,))
