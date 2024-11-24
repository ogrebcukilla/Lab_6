import sqlite3
import hashlib
import os

# Використання статичного секретного ключа (погана практика)
SECRET_KEY = "12345"

# SQL-ін'єкція через невикористання параметризованих запитів
def unsafe_sql_query(user_input):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)  # Небезпечний метод
    results = cursor.fetchall()
    conn.close()
    return results

# Використання слабкого алгоритму хешування (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 вважається небезпечним

# Виконання команди оболонки без перевірки вхідних даних
def unsafe_os_command(user_input):
    os.system(f"ping {user_input}")  # Може бути вразливим до командної ін'єкції

# Недостатній захист файлів
def insecure_file_access(filename):
    with open(filename, "r") as file:  # Може дозволити доступ до чутливих файлів
        return file.read()

if __name__ == "__main__":
    print("Вразливості для демонстрації Snyk:")
    username = input("Введіть ім'я користувача: ")
    print(unsafe_sql_query(username))
    password = input("Введіть пароль: ")
    print(f"Хеш пароля (MD5): {hash_password(password)}")
    command_input = input("Введіть IP-адресу або домен для ping: ")
    unsafe_os_command(command_input)
    file_name = input("Введіть назву файлу для читання: ")
    print(insecure_file_access(file_name))
