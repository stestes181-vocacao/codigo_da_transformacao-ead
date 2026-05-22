import sqlite3

conn = sqlite3.connect("artistas_clientes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

conn.commit()

print("✔ Banco e tabela criados com sucesso")