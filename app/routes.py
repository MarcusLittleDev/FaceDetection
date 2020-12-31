from app import app
from flask import render_template, jsonify, request
from detection import detect_face


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Face Detection')


@app.route('/process_image/', methods=['POST'])
def process_image():

    image = request.form['image']
    return detect_face(image)
