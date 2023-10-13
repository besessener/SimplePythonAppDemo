from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def hello():
    # Retrieve the 'sleep' parameter from the URL, default to 0 if not provided
    sleep_time = float(request.args.get('sleep', 0))
    
    # Introduce a delay based on the sleep_time value
    time.sleep(sleep_time / 1000)

    return f"Slept for {sleep_time} milli seconds."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    