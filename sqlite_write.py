import sqlite3

sqliteConnection = sqlite3.connect('demo.db')
print("database connected")


cursor = sqliteConnection.cursor()
print("Database initialized")


insert_table_query = """
INSERT into user (name,address,contact)
 values("Bishwajeet","Birgunj","9824210052")"""
cursor.execute(insert_table_query)
sqliteConnection.commit()
print ("data inserted sucessfully")


insert_table_query = """
INSERT into user (name,address,contact)
  values("Bishwajeet","Birgunj","9824210052")
  """
cursor.execute(insert_table_query)
sqliteConnection.commit()
print ("data inserted sucessfully")
