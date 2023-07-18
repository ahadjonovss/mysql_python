import mysql.connector
import time as t



class MySqlService:
    def __init__(self):
        self.allDatabases = None
        self.db = mysql.connector.connect(
            host="localhost",
            user='root',
            password="20058082"
        )
        self.cursor = self.db.cursor()

    def showDatabases(self):
        self.cursor.execute("show databases;")
        self.allDatabases = self.cursor.fetchall()
        for i, v in enumerate(self.allDatabases):
            print(f"{i + 1} - {v[0]}")
        self.selectDatabase()


    def showTables(self):
        self.cursor.execute("Show tables;")
        print(self.cursor.fetchall())



    def selectDatabase(self):
        selectedDb = int(input("Kerakli database idsini yozing  "))
        self.cursor.execute(f"Use {self.allDatabases[selectedDb-1][0]};")
        self.showTables()

    def createDatabase(self):
        dbName = input("Database uchun nom kiriting: ")
        print(f"{dbName} nomli database create qilinmoqda...")
        t.sleep(3)
        print("Oz qoldi...")
        t.sleep(2)
        self.cursor.execute(f"Create database if not exists {dbName}")
        print("Database muvaffaqqiyatli ochildi")
