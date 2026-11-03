import sqlite3

conn = sqlite3.connect("database.db")
print("opened db with sucess")

#conn.execute("CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT, pwd TEXT)")
#print("table created sucessfully")
conn.execute("ALTER TABLE students ADD COLUMN pwd TEXT")


conn.close()