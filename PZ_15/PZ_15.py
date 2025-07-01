#Вариант 31
#Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой
#организации. БД должна содержать таблицу Клиент со следующей структурой записи:
#ФИО клиента, код помещения, срок аренды, стоимость аренды за весь срок.

import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    print(f"Подключение к базе данных {db_file} успешно")
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Клиент (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        фио_клиента TEXT NOT NULL,
        код_помещения TEXT NOT NULL,
        срок_аренды INTEGER NOT NULL,
        стоимость_аренды REAL NOT NULL
    )
    ''')
    conn.commit()
    return True

def add_client(conn, фио, код, срок, стоимость_месяц):
    cursor = conn.cursor()
    общая_стоимость = срок * стоимость_месяц
    cursor.execute('''
    INSERT INTO Клиент (фио_клиента, код_помещения, срок_аренды, стоимость_аренды)
    VALUES (?, ?, ?, ?)
    ''', (фио, код, срок, общая_стоимость))
    conn.commit()
    print(f"Клиент {фио} успешно добавлен")

def show_all_clients(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Клиент")
    clients = cursor.fetchall()
    
    print("\nСписок всех клиентов:")
    print("{:<3} {:<30} {:<15} {:<10} {:<15}".format(
        "ID", "ФИО", "Код помещения", "Срок", "Стоимость", "Дата создания"))
    print("-" * 95)
    
    for client in clients:
        print("{:<3} {:<30} {:<15} {:<10} {:<15.2f}".format(
            client[0], client[1], client[2], client[3], client[4]))

def main():
    conn = create_connection("аренда_помещений.db")
    
    create_table(conn)
    
    add_client(conn, "Иванов Иван Иванович", "101", 12, 50000)
    add_client(conn, "Петрова Анна Сергеевна", "205", 6, 75000)
    add_client(conn, "Сидоров Михаил Петрович", "302", 24, 40000)

    show_all_clients(conn)

    conn.close()

if __name__ == '__main__':
    main()