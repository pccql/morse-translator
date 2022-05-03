import utils.morseCodeTable as morseCode


def populateDatabase(database_client):
    try:
        tableSize = len(morseCode.TABLE) * 2

        if len(database_client.keys()) == tableSize:
            return

        for key, value in morseCode.TABLE.items():
            database_client.set(key, value)
            database_client.set(value, key)
    except:
        print("❌ Connection to Redis database failed, make sure to run 'redis-server' in another terminal ❌")
