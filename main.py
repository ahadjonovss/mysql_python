import mysql.connector
import my_sql_service as mySql

mySqlService = mySql.MySqlService()


print("TANLANG")
print("1. Database ro'yxatini olish  2. Database qo'shish")
firstDecision = int(input())
if firstDecision == 1:
    mySqlService.showDatabases()

