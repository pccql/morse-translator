from curses.ascii import isalnum
from flask import jsonify
import app


class TranslationController:
    def decrypt(morse):
        morse += ' '
        text, currentLetter = '', ''
        spaces = 0
        badRequest = False

        for char in morse:
            if char.isalnum():
                badRequest = True
                break

            elif char != ' ':
                currentLetter += char
                spaces = 0

            else:
                spaces += 1
                if spaces == 2:
                    text += ' '
                else:
                    text += app.database_client.get(currentLetter)
                    currentLetter = ''

        if badRequest:
            return jsonify({'message': 'Only dashes, dots and spaces are allowed'}), 400

        return jsonify({'Decrypted message': text.strip()}), 200

    def encrypt(text):
        textWithoutSpaces = text.replace(' ', '')

        if not textWithoutSpaces.isalnum():
            return jsonify({'message': 'Only letters and numbers are allowed'}), 400

        morse = ''
        for letter in text.lower():
            if letter == ' ':
                morse += ' '

            else:
                morse += app.database_client.get(letter) + ' '

        return jsonify({'Encrypted message': morse.strip()}), 200
