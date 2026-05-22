import sqlite3

conn = sqlite3.connect('anime_clientes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

cursor.execute("""
INSERT INTO Clientes (nome, email) VALUES
('Taylor Swift', 'taylor@music.com'),
('Billie Eilish', 'billie@music.com'),
('The Weeknd', 'weeknd@music.com'),
('Ariana Grande', 'ariana@music.com'),
('Ed Sheeran', 'ed@music.com'),
('Bruno Mars', 'bruno@music.com'),
('Dua Lipa', 'dua@music.com'),
('Justin Bieber', 'justin@music.com')
""")

conn.commit()

print("\n🎧 LISTA DE ARTISTAS:")
cursor.execute("SELECT * FROM Clientes")

for c in cursor.fetchall():
    print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

cursor.execute("""
UPDATE Clientes
SET email = 'theweeknd@newmusic.com'
WHERE nome = 'The Weeknd'
""")

print("\n✔ The Weeknd atualizado")

cursor.execute("""
DELETE FROM Clientes
WHERE nome = 'Bruno Mars'
""")

print("✔ Bruno Mars removido")

conn.commit()

print("\n🎵 LISTA FINAL:")
cursor.execute("SELECT * FROM Clientes")

for c in cursor.fetchall():
    print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

conn.close()

print("\n✔ Questão 2 concluída 🎧")