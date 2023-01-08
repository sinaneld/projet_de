import streamlit as st
import numpy as np
from PIL import Image
from yolo import predict, get_text_description


st.title("Cats & Dogs")

uploaded_image = st.file_uploader("Upload your image to predict", type = ["jpg"], accept_multiple_files=False )

if uploaded_image is not None:
    input_image = np.array(Image.open(uploaded_image))

    if input_image is not None:
        prediction = predict(input_image)
        st.image(
            prediction.render()[0],
            caption=f"You amazing image has shape {input_image.shape[0:2]}",
            use_column_width=True,
        )
        st.text(get_text_description(prediction))