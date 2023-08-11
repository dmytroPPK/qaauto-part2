import sqlite3


class BaseDb:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)

    def close(self):
        if self.connection:
            self.connection.close()

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        if not params:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        cursor = self.connection.cursor()
        if not params:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
        return cursor.fetchall()


# Tests
if __name__ == "__main__":
    db_file = "test.db"

    # Creating the database
    db = BaseDb(db_file)
    db.connect()

    # Creating a table
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        );
    '''
    db.execute(create_table_query)

    # Inserting data
    insert_data_query = '''
        INSERT INTO users (name, age) VALUES (?, ?);
    '''
    db.execute(insert_data_query, ("Alice", 25))
    db.execute(insert_data_query, ("Bob", 30))

    # Selecting data
    select_data_query = '''
        SELECT * FROM users;
    '''
    users = db.select(select_data_query)
    for user in users:
        print(user)

    # Closing the database
    db.close()
