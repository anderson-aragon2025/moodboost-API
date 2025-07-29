from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Frases motivadoras por emoción
frases_motivadoras = {
    "muy alegre": [
        "¡Tu energía es contagiosa! Sigue brillando.",
        "¡Que gusto que te sientas tan bien! Recuerda: “La alegría es la forma más sencilla de gratitud.” – Karl Barth"
    ],
    "alegre": [
        "¡Sigue con esa actitud positiva!",
        "¡Perfecto! Recuerda: “La felicidad se encuentra en las pequeñas cosas.”"
    ],
    "neutro": [
        "Hoy puede parecer normal, pero es una nueva oportunidad.",
        "“Cada día es una página en blanco.”"
    ],
    "triste": [
        "Está bien sentirse así, el sol también vuelve a salir.",
        "Es una pena saber que te sientes asi, pero recuerda: “Después de la lluvia, siempre sale el arcoíris.”"
    ],
    "muy triste": [
        "No estás solo. Incluso los días oscuros pasan.",
        "Es una pena saber que te sientes asi, pero recuerda: “La esperanza es lo que nos impulsa cuando todo parece perdido.”"
    ]
}

def detectar_sentimiento(texto):
    try:
        analisis = TextBlob(texto)
        polaridad = analisis.sentiment.polarity

        if polaridad > 0.5:
            return "muy alegre"
        elif 0.05 < polaridad <= 0.5:
            return "alegre"
        elif -0.05 <= polaridad <= 0.05:
            return "neutro"
        elif -0.5 <= polaridad < -0.05:
            return "triste"
        else:
            return "muy triste"
    except Exception as e:
        return f"Error al analizar: {str(e)}"

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({'sentimiento': 'Error: cuerpo inválido. Esperaba JSON'}), 400

    texto = data.get('texto', '')
    if not texto.strip():
        return jsonify({'sentimiento': 'Error: el campo "texto" está vacío o no proporcionado'}), 400

    sentimiento = detectar_sentimiento(texto)
    frase = random.choice(frases_motivadoras.get(sentimiento, ["Sigue adelante, lo estás haciendo bien."]))

    # Mantiene "sentimiento" para ToolJet y agrega "frase_motivadora"
    return jsonify({
        'sentimiento': sentimiento,
        'frase_motivadora': frase
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
