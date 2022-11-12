import sqlite3
n = input()
# Подключение к БД
con = sqlite3.connect(n)

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM films
            WHERE (year > 1996) and genre=(
SELECT id FROM genres 
    WHERE title = 'музыка' or title = 'анимация')""").fetchall()

# Вывод результатов на экран
for elem in result:
    a = elem[1]
    for i in a:
        print(i)

con.close()