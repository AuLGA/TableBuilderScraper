from flask import Flask, request, jsonify
from pyautogui import locateOnScreen
import os
import PIL

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/screenshot_check')
def screenshot_check():
    
    located = locateOnScreen("./queue_window.png")

    return jsonify({"located": located})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)