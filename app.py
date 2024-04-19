from flask import Flask, request
import time
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Retrieve the 'sleep' parameter from the URL, default to 0 if not provided
    sleep_time = float(request.args.get('sleep', 0))
    
    # Introduce a delay based on the sleep_time value
    time.sleep(sleep_time / 1000)

    # Retrieve the 'size_kb' parameter from the URL, default to 0 if not provided
    size_kb = int(request.args.get('size_kb', 0))
    
    # Generate a random string of the requested size in KB
    response = os.urandom(size_kb * 1024).hex()  # os.urandom returns random bytes, which are then converted to a hex string

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

    
