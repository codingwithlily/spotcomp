# SpotComp
SpotComp is a Streamlit web app that allows users to upload two images of a mole to compare them and determine if there's any concern for skin cancer. The app calculates the Structural Similarity Index (SSI) between the two images and provides a recommendation based on the similarity index.

## URL
The SpotComp app is deployed here: 
https://spotcomp.streamlit.app/

## Note

This app assumes that the uploaded images are of the same mole and have similar orientations. It uses the Structural Similarity Index (SSI) as a metric to compare the images. It is intended for informational purposes only and should not be used as a substitute for professional medical advice.




## How to Use

1. Open the app in your web browser.
2. Upload the first image of the mole by clicking on "Upload first image..." button.
3. Upload the second image of the mole by clicking on "Upload second image..." button.
4. Click on the "Compare" button to compare the two images.
5. The app will calculate the Structural Similarity Index (SSI) between the two images and display the result.
6. If the similarity index is below 0.9, a warning message will be displayed indicating a significant change in the mole, and it is recommended to consult a dermatologist. If the similarity index is 0.9 or above, a message will be displayed indicating no significant change in the mole, but regular check-ups are recommended.
7. To compare another set of images, upload another pair of images, and click on the "Compare" button.




## To deploy and run this app locally, follow these steps:

1. Install Python.
2. Install the required Python packages listed in `requirements.txt` using pip:
pip install -r requirements.txt
3. Run the Streamlit app using the following command: 
streamlit run app.py


## Requirements

- Python 3.x
- Streamlit
- Pillow
- NumPy
- scikit-image

