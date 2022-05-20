import sqlite3

with sqlite3.connect("myschool.db") as connection:
    c = connection.cursor()
    #c.execute('DROP TABLE students')
    #c.execute("""CREATE TABLE students(studentId INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(50),email VARCHAR(50),password VARCHAR(50))""")
    # c.execute("""CREATE TABLE students(studentId INTEGER PRIMARY KEY AUTOINCREMENT,fname VARCHAR(50),lname VARCHAR(50),email VARCHAR(50))""")
    # c.execute("""CREATE TABLE courses(courseId INTEGER PRIMARY KEY AUTOINCREMENT,courseName VARCHAR(50),duration INTEGER,price REAL)""")
    # c.execute("""CREATE TABLE std_enroll(enrollId INTEGER PRIMARY KEY AUTOINCREMENT,studentId INTEGER,courseId INTEGER,enrlDate TEXT, FOREIGN KEY(studentId) REFERENCES students(studentId), FOREIGN KEY(courseId) REFERENCES courses(courseId))""")

    c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Data Science", "24","950.00")')
    c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Software Development", "24","1000.00")')
    c.execute('INSERT INTO courses (courseName, duration, price) VALUES("DevOps", "12","850.00")')
    c.execute('INSERT INTO courses (courseName, duration, price) VALUES("UI/UX Design", "12","650.00")')
    c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Blockchain", "12","1150.00")')
    c.execute('INSERT INTO courses (courseName, duration, price) VALUES("Cybersecurity", "24","850.00")')
    #c.execute('INSERT INTO students (username, email, password) VALUES("Tha", "w","321")')
    #c.execute('INSERT INTO students (username, email, password) VALUES("dog", "d@nod.ie","987")')



    # c.execute('INSERT INTO room (roomName, maxGuests) VALUES("Sea Breeze", 2)')
    # c.execute('INSERT INTO room (roomName, maxGuests) VALUES("Sun Shine", 3)')
    # c.execute('INSERT INTO room (roomName, maxGuests) VALUES("Tropical Mood", 4)')
    # c.execute('INSERT INTO room (roomName, maxGuests) VALUES("Blue Moon", 2)')

