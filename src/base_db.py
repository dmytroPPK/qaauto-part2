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
