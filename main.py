import mysql.connector
import my_sql_service as mySql
import os

mySqlService = mySql.MySqlService()

print("TANLANG")
while True:
    print("1. Database ro'yxatini olish  2. Database qo'shish  3. Chiqish")
    firstDecision = int(input())
    if firstDecision == 1:
        mySqlService.showDatabases()


    if firstDecision == 2:
        mySqlService.createDatabase()
    if firstDecision == 3:
        break



