from flask import Flask, jsonify
import pytest

app = Flask(__name__)

@app.route("/")
def home():

    return jsonify({
        "mensagem": "API funcionando com sucesso!"
    })


def test_home():

    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert resposta.json["mensagem"] == "API funcionando com sucesso!"


if __name__ == "__main__":
    app.run(debug=True)