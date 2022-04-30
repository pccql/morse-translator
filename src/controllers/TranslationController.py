from flask import jsonify


class TranslationController:
    def morseToText(morse):
        text = morse

        return jsonify({'Decoded message': text}), 200

    def textToMorse(text):
        morse = text

        return jsonify({'Encoded message': morse}), 200
