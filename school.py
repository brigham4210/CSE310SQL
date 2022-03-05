import sqlite3

# connect to database
conn = sqlite3.connect('school.db')

# create a cursor
c = conn.cursor()


def insert_record():
    # insert values
    many_students = []
    type_in = "Y"

    while type_in != "N":
        first = input("First name: ").capitalize()
        last = input("Last: ").capitalize()
        grade = int(input("grade: "))
        email = input("Email: ").lower()
        many_students.append((first,last,grade,email))
        type_in = input("Type in more information?(Y/N) ").upper()
    

    c.executemany("INSERT INTO students VALUES (?,?,?,?)",many_students)

def student_info():
    c.execute("SELECT * FROM students")

    print()
    
    for student in c.fetchall():
        print(student)

def delete_record():
    print()
    print("which student do you want to delete?")
    first_name = input("Type in the first name: ").capitalize()
    last_name = input("Type in the last name: ").capitalize()
    
    c.execute("DELETE from students WHERE first_name = ? and last_name = ?", (first_name,last_name,))
    conn.commit()

option = None

while option != 0:
    if option == 1:
        insert_record()
    elif option == 2:
        delete_record()
    elif option == 3:
        student_info()

    print()
    print("Option 1: Insert record")
    print("Option 2: Delete record")
    print("Option 3: list record")
    print("Option 0: Close")

    option = int(input("Select you option: "))


# Commit our command
conn.commit()

# close the conection
conn.close()