from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("usuarios.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conn.commit()

@app.route("/saudacao")
def saudacao():

    return jsonify({
        "mensagem": "Olá! API funcionando!"
    })


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    dados = request.get_json()

    nome = dados["nome"]
    email = dados["email"]

    cursor.execute("""
    INSERT INTO usuarios (nome, email)
    VALUES (?, ?)
    """, (nome, email))

    conn.commit()

    return jsonify({
        "mensagem": "Usuário cadastrado!"
    })

@app.route("/usuarios")
def usuarios():

    cursor.execute("SELECT * FROM usuarios")

    dados = cursor.fetchall()

    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)