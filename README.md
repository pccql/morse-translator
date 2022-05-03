## How to run

- Create a virtual environment
   - `python3 -m venv venv`
- Active the environment
   - `. venv/bin/activate`
- Install the dependencies
   - `pip install -r requirements.txt`
- Create a .env file with this data:
```
FLASK_APP=src/app
FLASK_ENV=development
```
- Start the redis server:
  - `redis-server`
- On another terminal, run the morse translator API:
  - `flask run`
- Go to http://127.0.0.1:5000/docs to see the API documentation