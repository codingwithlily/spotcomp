from flask import Flask, render_template, request
import cv2
import numpy as np
import os

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

    img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), cv2.IMREAD_COLOR)

    # Image comparison using OpenCV
    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    threshold = 0.9
    if similarity > threshold:
        result = "Images appear to be similar."
    else:
        result = "Images are different. Please consult your doctor."

    return result



if __name__ == '__main__':
    #app.run(debug=True, use_reloader=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

