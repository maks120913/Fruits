import sqlite3
conn = sqlite3.connect('FruitBasket.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Color TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO Fruits (Name, Color) VALUES ('Яблуко', 'Червоне')")
cursor.execute("INSERT INTO Fruits (Name, Color) VALUES ('Банан', 'Жовтий')")
cursor.execute("INSERT INTO Fruits (Name, Color) VALUES ('Апельсин', 'Помаранчевий')")
cursor.execute("UPDATE Fruits SET Color = 'Зелене' WHERE Name = 'Яблуко'")

cursor.execute("SELECT * FROM Fruits WHERE Color = 'Жовтий'")
yellow_fruits = cursor.fetchall()
print("Жовті фрукти:")
for fruit in yellow_fruits:
    print(fruit)

cursor.execute("SELECT * FROM Fruits")
all_fruits = cursor.fetchall()
print("\nВсі фрукти:")
for fruit in all_fruits:
    print(fruit)

conn.commit()
conn.close()
