import sqlite3
# Verbindung zu sqlite-DB
conn = sqlite3.connect('studenten.db')

# Erstellung von Cursor um sql-Befehl durchzuführen
cursor = conn.cursor()

# Erstellung von Tabellen in studenten.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL,
    course VARCHAR(32) NOT NULL
    );
''')

# Erste Funktion hinzufügen (CREATE)
def add_student(name, age, course):
    cursor.execute('''
    INSERT INTO students (name, age, course) VALUES (?, ?, ?)      
    ''', (name, age, course))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Erstellung von READ Funktion
def show_students():
    cursor.execute('SELECT id, name FROM students')
    students = cursor.fetchall()
    for student in students:
        print(student)

# UPDATE Function to update student data
def update_student(id, name, age, course):
    cursor.execute('''
    UPDATE students SET name = ?, age = ?, course = ?
    WHERE id = ?
    ''', (name, age, course, id))
    conn.commit()
    print(f"updated student with id {id}")

# DELETE Function to delete student data
def delete_student(id):
    cursor.execute('''
    DELETE FROM students WHERE id = ?              
    ''', (id,))
    conn.commit()
    print(f"Student mi ID {id} wurde gelöscht.")

# Main
def main()
    while True:
        


# delete_student(2)
# update_student(2, "Cansin", 36, "TECHSTARTER")
# add_student('Abdullah', 34, 'TECHSTARTER')
show_students()