from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher  
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        Caesar = CaesarCipher()
        encrypted_text = Caesar.encrypt_text(text, key)
        return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"
    except ValueError:
        return "Invalid key! Please enter a number."

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        Caesar = CaesarCipher()
        decrypted_text = Caesar.decrypt_text(text, key)
        return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
    except ValueError:
        return "Invalid key! Please enter a number."

# Vigenere Cipher
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# RailFence Cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputRails'])
        RailFence = RailFenceCipher()
        encrypted_text = RailFence.rail_fence_encrypt(text, key)
        return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"
    except ValueError:
        return "Invalid key! Please enter a number."

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputRails'])
        RailFence = RailFenceCipher()
        decrypted_text = RailFence.rail_fence_decrypt(text, key)
        return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
    except ValueError:
        return "Invalid key! Please enter a number."

# PlayFair Cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Transposition Cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        Transposition = TranspositionCipher()
        encrypted_text = Transposition.encrypt(text, key)
        return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"
    except ValueError:
        return "Invalid key! Please enter a number."

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        Transposition = TranspositionCipher()
        decrypted_text = Transposition.decrypt(text, key)
        return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
    except ValueError:
        return "Invalid key! Please enter a number."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)