import numpy as np
import pickle as pkl
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPool2D
# import requests
from sklearn.neighbors import NearestNeighbors
import os
from numpy.linalg import norm
import streamlit as st

# Set page configuration and custom CSS


# st.set_page_config(layout="centered")
# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: #D8BFD8;  /* Lavender background */
#     }
#     .sidebar .sidebar-content {
#         background: #D8BFD8;  /* Lavender background for sidebar */
#     }
#     .stButton {
#         background-color: #FFC0CB !important;  /* Millennial Pink button background */
#         color: black !important;  /* Black text color for button */
#     }
#     .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
#         color: black;  /* Black heading color */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Header
st.header('Its My Mantra : Styles that suits your Body Type')

# Load the precomputed image features and filenames
Image_features = pkl.load(open('Images_features.pkl', 'rb'))
filenames = pkl.load(open('filenames.pkl', 'rb'))

def extract_features_from_images(image_path, model):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_expand_dim = np.expand_dims(img_array, axis=0)
    img_preprocess = preprocess_input(img_expand_dim)
    result = model.predict(img_preprocess).flatten()
    norm_result = result / norm(result)
    return norm_result

# Load the pre-trained model
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False
model = tf.keras.models.Sequential([model, GlobalMaxPool2D()])

# Fit the NearestNeighbors model
neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
neighbors.fit(Image_features)

# User input for body type
body_type = st.selectbox('Choose your Body type', ['Pear', 'Hourglass', 'Rectangle', 'Apple', 'Inverted Triangle'])

# User input for categories
categories = st.selectbox('Choose Clothes category', ['Tops', 'Jeans', 'Dresses', 'Shoes', 'Accessories'])

# Submit button
if st.button('Submit'):
    folder_name = f'{body_type}{categories}'
    # folder_path = os.path.join('pre_saved_images', folder_name)
    
    # Get an image file from the selected folder
    if os.path.exists(folder_name):
        image_files = [os.path.join(folder_name, file) for file in os.listdir(folder_name) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            selected_image_path = image_files[0]  # Take the first image for simplicity
            st.subheader('Suggested style for you')
            st.image(selected_image_path)
            
            # Extract features from the selected image
            input_img_features = extract_features_from_images(selected_image_path, model)
            
            # Recommend clothes based on the selected image
            distance, indices = neighbors.kneighbors([input_img_features])
            st.subheader('Recommended Products for above style')
            col1, col2, col3, col4, col5 = st.columns(5)
            for i, idx in enumerate(indices[0][1:]):  # Skip the first index (it's the selected image itself)
                col = eval(f'col{i + 1}')
                col.image(filenames[idx])
        else:
            st.error(f'No images found in folder {folder_name}.')
    else:
        st.error(f'Folder {folder_name} does not exist.')
