from flask import jsonify
import app


class TranslationController:
    def decrypt(morse):
        morse += ' '
        text, currentLetter = '', ''
        spaces = 0

        for char in morse:
            if char != ' ':
                currentLetter += char
                spaces = 0
            else:
                spaces += 1
                if spaces == 2:
                    text += ' '
                else:
                    text += app.database_client.get(currentLetter)
                    currentLetter = ''

        return jsonify({'Decrypted message': text.strip()}), 200

    def encrypt(text):
        morse = ''
        for letter in text.lower():
            if letter == ' ':
                morse += ' '

            else:
                morse += app.database_client.get(letter) + ' '

        return jsonify({'Encrypted message': morse.strip()}), 200
