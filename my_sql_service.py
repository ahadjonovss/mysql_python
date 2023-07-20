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

    def showDatabaseMenu(self):
        while True:
            print("1. Tablelar ro'yxatini olish 2.Table qo'shish  3. Orqaga qaytish")
            databaseMenuDecision = int(input("Kerakli menuni tanlang >>> "))
            if databaseMenuDecision == 1:
                self.showTables()
            elif databaseMenuDecision == 2:
                self.createTable()
            else:
                break

    def createTable(self):
        nameOfTable = input("Table nomini kiriting >>> ")
        print("Table yaratilmoqda...")
        t.sleep(2)
        print("Oz qoldi...")
        t.sleep(1)
        self.cursor.execute(f"Create table {nameOfTable} (id serial);")
        print(f"{nameOfTable} muvaffaqqiyatli yaratildi")


    def showTables(self):
        self.cursor.execute("Show tables;")
        for i, v in enumerate(self.cursor.fetchall()):
            print(f"{i+1} - {v[0]}")

    def selectDatabase(self):
        selectedDb = int(input("Kerakli database idsini yozing  "))
        self.cursor.execute(f"Use {self.allDatabases[selectedDb - 1][0]};")
        self.showDatabaseMenu()

    def createDatabase(self):
        dbName = input("Database uchun nom kiriting: ")
        print(f"{dbName} nomli database create qilinmoqda...")
        t.sleep(3)
        print("Oz qoldi...")
        t.sleep(2)
        self.cursor.execute(f"Create database if not exists {dbName}")
        print("Database muvaffaqqiyatli ochildi")
