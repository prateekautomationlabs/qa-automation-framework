import mysql.connector
from utils.data_reader import load_config

class MySQLClient:
    def __init__(self):
        config = load_config()['db']
        self.conn = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            database=config['name']
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def fetch_one(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
