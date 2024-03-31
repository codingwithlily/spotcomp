from flask import Flask, render_template, request
from PIL import Image
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare_images():
    if 'file1' not in request.files or 'file2' not in request.files:
        return "Please upload two images.", 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    # Load images using PIL (Python Imaging Library)
    img1 = Image.open(file1)
    img2 = Image.open(file2)

    # Convert images to numpy arrays
    np_img1 = np.array(img1)
    np_img2 = np.array(img2)

    # Image comparison (Example: Mean Squared Error)
    mse = np.mean(np.square(np_img1 - np_img2))

    if mse < 1000:  # Adjust threshold as per your requirement
        result = "Images are similar."
    else:
        result = "Images are different."

    return result


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
