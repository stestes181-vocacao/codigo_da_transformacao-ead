from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():

    return jsonify({
        "mensagem": "Olá! API Flask funcionando!"
    })

if __name__ == "__main__":
    app.run(debug=True)