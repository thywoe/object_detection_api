from flask import Flask, jsonify, request, render_template, flash
from werkzeug.utils import secure_filename
import json
import os
from image_object_detection import image_detection


ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg', 'gif'}
app = Flask(__name__)

# os generated secret key
app.config['SECRET_KEY'] = os.urandom(16)

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/detection-api', methods=['GET', 'POST'])
def dectect():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        # check if request contain file 
        if 'image' not in request.files:
            flash('No file selected')
            return render_template("index.html")
        image = request.files['image']
        if image.filename == '':
            flash('Invalid file')
            return render_template("index.html")
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save('image-uploads/'+filename)
            result = image_detection("./image-uploads")
            return jsonify({"data":result})
            

if __name__ == '__main__':
    app.run(debug=True)
    