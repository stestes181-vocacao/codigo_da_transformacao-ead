import sqlite3

conn = sqlite3.connect('artistas_clientes.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Clientes')

cursor.execute('''
CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    genero_musical TEXT
)
''')

artistas_data = [
    ("Taylor Swift", "taylor@music.com", "Pop"),
    ("Billie Eilish", "billie@music.com", "Pop"),
    ("The Weeknd", "weeknd@music.com", "R&B"),
    ("Ariana Grande", "ariana@music.com", "Pop"),
    ("Drake", "drake@music.com", "Rap"),
    ("Bruno Mars", "bruno@music.com", "Funk Pop"),
    ("Dua Lipa", "dua@music.com", "Dance Pop"),
    ("Ed Sheeran", "ed@music.com", "Pop"),
    ("Rihanna", "rihanna@music.com", "R&B"),
    ("Justin Bieber", "justin@music.com", "Pop")
]

cursor.executemany("""
INSERT INTO Clientes (nome, email, genero_musical)
VALUES (?, ?, ?)
""", artistas_data)

conn.commit()

print("🎧 CONSULTAS MUSICAIS AVANÇADAS 🎧\n")

# 1. nome começando em 'D'
cursor.execute("""
SELECT * FROM Clientes
WHERE nome LIKE 'D%'
""")

print("⚡ Artistas com nome começando em 'D':")
for r in cursor.fetchall():
    print(f"   🎤 {r[1]} | 📧 {r[2]} | 🎶 {r[3]}")

# 2.  gênero Pop
cursor.execute("""
SELECT * FROM Clientes
WHERE genero_musical = 'Pop'
""")

print("\n🎵 Artistas do gênero Pop:")
for r in cursor.fetchall():
    print(f"   🎧 {r[1]} - {r[2]}")

cursor.execute("""
SELECT * FROM Clientes
WHERE nome LIKE '%a%'
ORDER BY nome
""")

print("\n📜 Artistas com a letra 'a' no nome:")
for i, r in enumerate(cursor.fetchall(), 1):
    print(f"   {i}. {r[1]} ({r[3]})")

cursor.execute("""
SELECT genero_musical, COUNT(*)
FROM Clientes
GROUP BY genero_musical
""")

print("\n📊 Ranking de gêneros musicais:")
for genero, total in cursor.fetchall():
    barra = "🎶" * total
    print(f"   {genero:12} : {total} artista(s) {barra}")

conn.close()

print("\n✔ Questão 3 concluída com sucesso 🎧")