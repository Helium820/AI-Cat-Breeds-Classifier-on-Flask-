import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import numpy as np

import cv2
import tensorflow as tf
from datetime import datetime as dt
import datetime
# from keras.models import load_model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configure application
app = Flask(__name__)

# # Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# # Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# @app.after_request
# def after_request(response):
#     """Ensure responses aren't cached"""
#     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     response.headers["Expires"] = 0
#     response.headers["Pragma"] = "no-cache"
#     return response

# ============

UPLOAD_FOLDER = 'static/uploads/'
# Upload directory
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_folder = "static")

# APP CONFIGURATIONS
app.config['SECRET_KEY']= 'YourSecretKey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def process_img(image_path):
    img_height = 256
    img_width = 256
    img = tf.keras.utils.load_img(image_path, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array


image_path = "cat_breed/TRAIN/ragdoll/61GUPlJL1kL.jpg"
model_name = "weights/save_at_2.h5.keras"

model = load_model(model_name,compile=False)
# model.summary()

### visualize the result using confusion matrix
PATH_TESTSET = "cat_breed/TEST"

generator= ImageDataGenerator()

train_ds = generator.flow_from_directory(
    directory=PATH_TESTSET,
    batch_size=8,
)

class_names = list(train_ds.class_indices)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Save the uploaded file as name of current time
            dt_now = dt.now().strftime("%Y%m%d%H%M%S%f")
            filename = dt_now + ".jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # PATH to static files
            img_dir = "./static/uploads/"
            path = img_dir + filename

            img_arr = process_img(path)
            pred = model.predict(img_arr)*100
            pred = np.round(pred,2)
            # predicted_classes = class_names[np.argmax(pred)]
            # score = np.max(pred[0])
            # ### print out message
            # print("Your image most likely belongs to {} with a {:.2f} percent confidence.".format(predicted_classes,100 * np.max(score)))

            top3ind = np.argsort(-pred)[0][:3]

        return render_template('temp.html',
                               img_path=path,
                               top3ind=top3ind,
                               class_names=class_names,
                               pred = pred[0])


if __name__ == '__main__':
    app.run()
