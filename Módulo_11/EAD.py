import sqlite3

conn = sqlite3.connect("tarefas_casa.db")
cursor = conn.cursor()

# criar
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
""")

conn.commit()

# adicionar
cursor.execute("""
INSERT INTO tarefas (descricao)
VALUES ('Lavar a louça')
""")

cursor.execute("""
INSERT INTO tarefas (descricao)
VALUES ('Arrumar o quarto')
""")

cursor.execute("""
INSERT INTO tarefas (descricao)
VALUES ('Fazer lição de Python')
""")

conn.commit()

# visualizar 
print("\n🏠 LISTA DE TAREFAS")

cursor.execute("SELECT * FROM tarefas")

for tarefa in cursor.fetchall():
    print(tarefa)

# excluir
cursor.execute("""
DELETE FROM tarefas
WHERE id = 2
""")

conn.commit()

print("\n✔ Tarefa removida!")
print("\n📋 LISTA FINAL")

cursor.execute("SELECT * FROM tarefas")

for tarefa in cursor.fetchall():
    print(tarefa)

conn.close()

print("\n✔ Desafio extra concluído!")