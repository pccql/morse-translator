import utils.morseCodeTable as morseCode


def populateDatabase(redis_client):
    tableSize = len(morseCode.TABLE) * 2

    if len(redis_client.keys()) == tableSize:
        return

    for key, value in morseCode.TABLE.items():
        redis_client.set(key, value)
        redis_client.set(value, key)
