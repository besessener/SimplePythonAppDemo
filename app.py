from flask import Flask
import time
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # simulating load with random sleep
    sleep_time = random.uniform(0, 1)
    time.sleep(sleep_time)
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    