import sqlite3

# Создаем базу данных
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Создаем таблицу "students"
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  age INTEGER,
                  grade TEXT)''')

# Вставляем несколько записей в таблицу "students"
students_data = [
    ('Олим', 24, '79/100'),
    ('Самира', 19, '81/100'),
    ('Мафтуна', 21, '85/100'),
    ('Диана', 23, '94/100'),
]

cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students_data)
conn.commit()

# Функция для получения информации о студенте по имени
def get_student_by_name(name):
    cursor.execute("SELECT name, age, grade FROM students WHERE name=?", (name,))
    student = cursor.fetchone()
    if student:
        return f"Имя: {student[0]}, Возраст: {student[1]}, Оценка: {student[2]}"
    else:
        return "Студент не найден"

# Функция для обновления оценки студента
def update_student_grade(name, new_grade):
    cursor.execute("UPDATE students SET grade=? WHERE name=?", (new_grade, name))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Оценка студента {name} успешно обновлена на {new_grade}")
    else:
        print(f"Студент {name} не найден")

# Функция для удаления студента
def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Студент {name} успешно удален")
    else:
        print(f"Студент {name} не найден")

# Пример использования функций
print(get_student_by_name("Олим"))  # Получение информации о студенте
update_student_grade("Диана", "94/100")     # Обновление оценки студента
delete_student("Мафтуна")            # Удаление студента

# Закрываем соединение с базой данных
conn.close()