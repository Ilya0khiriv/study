import sqlite3
connection = sqlite3.connect("not_telegram.db" )
cursor = connection.cursor()
cex = cursor.execute

cex("""CREATE TABLE IF NOT EXISTS Users
(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, balance INTEGER NOT NULL
)
""")


for i in range(1, 11):
    user = f"User{i}"
    mail = f"example{i}@gmail.com"
    age = int(f"{i}"+"0")
    balance = 1000
    cex("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (user, mail, age, balance))

for i in range(1, 11):
    if i % 2 != 0:
        cex("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))


_store = 2
for i in range(1, 11):
    _store += 1

    if _store == 3:
        _store = 0
        cex("DELETE FROM Users WHERE username=?", (f"User{i}",))

cex("SELECT * FROM Users where age != ?", (60,))
rows = cursor.fetchall()


cex("DELETE FROM Users WHERE id=?", (6,))


cex("SELECT AVG(balance) from Users")
average = cursor.fetchone()[0]
print(average)

connection.commit()
connection.close()
