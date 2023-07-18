import mysql.connector


class MySqlService:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user='root',
            password="20058082"
        )
        self.cursor = self.db.cursor()

    def showDatabases(self):
        self.cursor.execute("show databases;")
        for i, v in enumerate(self.cursor.fetchall()):
            print(f"{i+1} - {v[0]}")
