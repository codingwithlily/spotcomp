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
uploaded_files = st.file_uploader("Choose images...", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

MAX_FILE_SIZE = 5 * 1024 * 1024

if uploaded_files is not None and len(uploaded_files) == 2:
    # Read and display the uploaded images
    image1 = Image.open(uploaded_files[0])
    image2 = Image.open(uploaded_files[1])

    st.image([image1, image2], caption=['Image 1', 'Image 2'], width=300)

    # convert images to numpy arrays for comparison
    img1_array = np.array(image1)
    img2_array = np.array(image2)

    # calculate Structural Similarity Index (SSI)
    similarity_index = ssim(img1_array, img2_array, multichannel=True)

    st.write(f'Similarity Index: {similarity_index}')

    if similarity_index < 0.9:
        st.warning("There's a significant change in the mole. Please consult a dermatologist.")
    else:
        st.success("There's no significant change in the mole. However, regular check-ups are recommended.")
