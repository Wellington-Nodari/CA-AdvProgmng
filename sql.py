import sqlite3

with sqlite3.connect("myschool.db") as connection:
    c = connection.cursor()
    # c.execute('DROP TABLE room')
    # c.execute("""CREATE TABLE students(studentId INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(50),email VARCHAR(50),password VARCHAR(50))""")
    # c.execute("""CREATE TABLE students(studentId INTEGER PRIMARY KEY AUTOINCREMENT,fname VARCHAR(50),lname VARCHAR(50),email VARCHAR(50))""")
    # c.execute("""CREATE TABLE courses(courseId INTEGER PRIMARY KEY AUTOINCREMENT,courseName VARCHAR(50),duration INTEGER,price REAL)""")
    # c.execute("""CREATE TABLE std_enroll(enrollId INTEGER PRIMARY KEY AUTOINCREMENT,studentId INTEGER,courseId INTEGER, courseName VARCHAR(50),enrlDate TEXT, FOREIGN KEY(studentId) REFERENCES students(studentId), FOREIGN KEY(courseName) REFERENCES courses(courseName))""")
    #c.execute("""CREATE TABLE loginCred(credentialId INTEGER PRIMARY KEY AUTOINCREMENT,email VARCHAR(50),password VARCHAR(50), FOREIGN KEY(email) REFERENCES students(email))""")

    # c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Data Science", "24","950.00")')
    # c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Software Development", "24","1000.00")')
    # c.execute('INSERT INTO courses (courseName, duration, price) VALUES("DevOps", "12","850.00")')
    # c.execute('INSERT INTO courses (courseName, duration, price) VALUES("UI/UX Design", "12","650.00")')
    # c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Blockchain", "12","1150.00")')
    # c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Cybersecurity", "24","850.00")')
    #c.execute('INSERT INTO students (username, email, password) VALUES("Tha", "w","321")')
    #c.execute('INSERT INTO students (username, email, password) VALUES("dog", "d@nod.ie","987")')



    # c.execute('INSERT INTO students (fname, lname, email) VALUES("John", "Wick", "jw@mail.com")')
    # c.execute('INSERT INTO std_enroll (courseName, enrlDate) VALUES("DevOps", "2022-05-01")')
    # c.execute('INSERT INTO loginCred (email, password) VALUES("jw@mail.com", "123")')
    # c.execute('INSERT INTO room (roomName, maxGuests) VALUES("Blue Moon", 2)')

