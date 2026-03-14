from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# 摩斯電碼對照表
MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--.."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random_letter")
def random_letter():
    letter = random.choice(list(MORSE_CODE.keys()))
    return jsonify({"letter": letter, "morse": MORSE_CODE[letter]})

if __name__ == "__main__":
    app.run(debug=True)
