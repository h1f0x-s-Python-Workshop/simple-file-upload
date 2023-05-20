from flask import Flask

UPLOAD_FOLDER = ''
ACCESS_KEY = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ACCESS_KEY'] = ACCESS_KEY
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024