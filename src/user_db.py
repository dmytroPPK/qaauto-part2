from src.base_db import BaseDb
from dataclasses import dataclass
from pprint import pprint


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


# Tests
if __name__ == "__main__":
    db_file = "userdatabase.db"

    # Creating the UserDb instance
    user_db = UserDb(db_file)

    user_db.execute("delete from users")

    user_db.add_user(User('John', 24, "john.a@com"))
    all_users = user_db.get_users()
    pprint(all_users)

    # user_db.delete_user_by_id(1)
    # all_users = user_db.get_users()
    # pprint(all_users)

    john = user_db.get_user_by_id(1)
    pprint(john)

    john.age = 30
    john.email = "John.Man@gmail.com"
    user_db.update_user_by_id(john)

    new_john = user_db.get_user_by_id(1)
    pprint(john)

    # Inserting data
    # user_db.execute("INSERT INTO users (name, age) VALUES (?, ?);", ("Alice", 25))
    # user_db.execute("INSERT INTO users (name, age) VALUES (?, ?);", ("Bob", 30))

    # Selecting users
    # users = user_db.get_users()
    # for user in users:
    #     print(user)

    # Updating user
    # user_db.update_user(1, "Alice Smith", 26)

    # Deleting user
    # user_db.delete_user(2)

    # Getting user by ID
    # user_by_id = user_db.get_user_by_id(1)
    # print("User by ID:", user_by_id)

    # Closing the UserDb instance (which also closes the underlying Database connection)
    user_db.close()
