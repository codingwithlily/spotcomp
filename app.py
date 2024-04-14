import streamlit as st
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2gray

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

# Upload first image
col1, col2 = st.columns(2)
with col1:
    uploaded_file1 = st.file_uploader("Upload first image...", type=['jpg', 'jpeg', 'png'])

# Upload second image
with col2:
    uploaded_file2 = st.file_uploader("Upload second image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file1 and uploaded_file2:
    # Read and display the uploaded images
    image1 = Image.open(uploaded_file1)
    image2 = Image.open(uploaded_file2)

    st.image([image1, image2], caption=['Image 1', 'Image 2'], width=300)

    # Resize images to the same size
    min_width = min(image1.width, image2.width)
    min_height = min(image1.height, image2.height)
    image1 = image1.resize((min_width, min_height))
    image2 = image2.resize((min_width, min_height))

    # Convert images to grayscale
    image1_gray = rgb2gray(np.array(image1))
    image2_gray = rgb2gray(np.array(image2))

    # Check if "Compare" button is clicked
    if st.button("Compare"):
        # Calculate a valid window size for SSIM
        win_size = min(7, min(min_height, min_width))
        if win_size % 2 == 0:
            win_size -= 1

        # Calculate Structural Similarity Index (SSI) with the valid window size
        similarity_index = ssim(image1_gray, image2_gray, win_size=win_size)

        st.write(f'Similarity Index: {similarity_index}')

        if similarity_index < 0.9:
            st.warning("There's a significant change in the mole. Please consult a dermatologist.")
        else:
            st.success("There's no significant change in the mole. However, regular check-ups are recommended.")