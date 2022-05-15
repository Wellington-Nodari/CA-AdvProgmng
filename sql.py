import sqlite3

with sqlite3.connect("myschool.db") as connection:
    c = connection.cursor()
    #c.execute('DROP TABLE students')
    c.execute("""CREATE TABLE students(studentId INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(50),email VARCHAR(50),password VARCHAR(50))""")
    c.execute('INSERT INTO students (username, email, password) VALUES("Well","w@nod.ie","123")')
    c.execute('INSERT INTO students (username, email, password) VALUES("Tha", "w","321")')
    c.execute('INSERT INTO students (username, email, password) VALUES("dog", "d@nod.ie","987")')
