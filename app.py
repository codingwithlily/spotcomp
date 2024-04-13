import streamlit as st
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim

st.set_page_config(layout="wide", page_title="Spot Comp")
#st.write("Spot Comp")


# front end elements of the web page
html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Spot Comp</h1> 
    </div> 
    """

# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True)
st.caption('by Lily Tsai')

st.write(
    "Upload two images of the mole to compare."
)
uploaded_files = [None, None]

# Upload first image
uploaded_files[0] = st.file_uploader("Upload first image...", type=['jpg', 'jpeg', 'png'])

# Upload second image
uploaded_files[1] = st.file_uploader("Upload second image...", type=['jpg', 'jpeg', 'png'])

if all(uploaded_files):
    # Read and display the uploaded images
    image1 = Image.open(uploaded_files[0])
    image2 = Image.open(uploaded_files[1])

    st.image([image1, image2], caption=['Image 1', 'Image 2'], width=300)

    # Convert images to numpy arrays for comparison
    img1_array = np.array(image1)
    img2_array = np.array(image2)

    # Ensure the images have the same shape
    min_height = min(img1_array.shape[0], img2_array.shape[0])
    min_width = min(img1_array.shape[1], img2_array.shape[1])
    img1_array = img1_array[:min_height, :min_width, :]
    img2_array = img2_array[:min_height, :min_width, :]

    # Calculate Structural Similarity Index (SSI) with a window size of 7
    similarity_index = ssim(img1_array, img2_array, win_size=7, multichannel=True)

    st.write(f'Similarity Index: {similarity_index}')

    if similarity_index < 0.9:
        st.warning("There's a significant change in the mole. Please consult a dermatologist.")
    else:
        st.success("There's no significant change in the mole. However, regular check-ups are recommended.")
