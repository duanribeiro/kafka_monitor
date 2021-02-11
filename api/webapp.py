from flask import Flask
import time
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    sleeping = random.randint(0, 5)
    time.sleep(sleeping)

    return {'sleeping_time': sleeping}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)