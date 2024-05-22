import sqlite3
# to create database 
sqliteConnection = sqlite3.connect('demo.db')
print("database connected")


cursor = sqliteConnection.cursor()
print("Database initialized")
# to create table 

create_table_query ="""
CREATE TABLE user(id integer primary key AUTOINCREMENT, name text, address text, contact number)

"""
cursor.execute(create_table_query)