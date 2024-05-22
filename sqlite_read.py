import sqlite3

sqliteConnection = sqlite3.connect('demo.db')
print("database connected")


cursor = sqliteConnection.cursor()
print("Database initialized")

read_table_query ="""
SELECT * from user;"""
cursor.execute(read_table_query)
print(cursor.fetchall())


sqliteConnection.close()