import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename


@app.route('/upload', methods=['POST'])
def upload_file():
    # simple authentication
    if 'key' not in request.form:
        resp = jsonify({'message': 'Access denied'})
        resp.status_code = 403
        return resp

    if request.form['key'] != app.config['ACCESS_KEY']:
        resp = jsonify({'message': 'Access denied'})
        resp.status_code = 403
        return resp

    # check if form complete
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    if request.files['file'].filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp

    if 'ref' not in request.form:
        resp = jsonify({'message': 'No case reference in the request'})
        resp.status_code = 400
        return resp

    # check dir
    path = os.path.join(app.config['UPLOAD_FOLDER'], request.form['ref'])
    dir_exists = os.path.exists(path)

    if not dir_exists:
        os.makedirs(path)

    #process upload
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(path, filename))
    resp = jsonify({'message': 'File successfully uploaded'})
    resp.status_code = 201
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3737)
