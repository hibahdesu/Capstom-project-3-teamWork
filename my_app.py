# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from textwrap import fill
import pickle
import requests
import json
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

st.sidebar.markdown("# Main page 🎈")

html_style0 = """
<div>
<h3 style="color: #049395;text-align:center; font-size:38px;  font-family: sans-serf; border-radius: 2rem .5rem; border: 1px solid #049395; padding: 1rem 1.5rem; margin-bottom: 2rem;">Welcome to the Fraud Detection App🎈</h3>
</div>"""
st.markdown(html_style0,unsafe_allow_html=True)

html_style0 = """
<div>
<h1 style="color: #044A95;text-align:center; font-size:64px";>Fraud Detection App</h1>
</div>"""
st.markdown(html_style0,unsafe_allow_html=True)

# Add image
# img = Image.open("car.jpg")
# st.image(img, caption="car")


import streamlit as st
from PIL import Image
import base64
        # overflow: hidden;
# Define the CSS style

background_color = """
    <style>
        body {
            background-color: #000;  /* Light blue color */
        }
    </style>
"""
st.markdown(background_color, unsafe_allow_html=True)


css = """
<style>
    .rounded-image {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
        max-width: 100%;
    }
</style>
"""
css2 = """
<style>
    .img2 {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 2rem;
        max-width: 100%;
    }
</style>
"""

# Display the CSS style
st.markdown(css, unsafe_allow_html=True)

# Display the image with rounded corners
image_path = 'fr3.jpg'
image_html = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}"></div>'
st.markdown(image_html, unsafe_allow_html=True)



# st.header("About The App")
html_style3 = """
<div style="padding:8px;margin-bottom:24px">
<h2 style="color:#61ABFB; font-size:42px; border-left: 4px solid #61ABFB; padding-left: .5rem; margin-bottom: 1rem">About the app</h2>
</div>"""
st.markdown(html_style3,unsafe_allow_html=True)
# st.markdown('The Fraud Detection Web App is a powerful and intelligent application designed to detect fraudulent activities in real-time. Built with advanced machine learning algorithms and cutting-edge technology, this web app offers a robust solution for businesses and organizations to safeguard themselves against fraudulent transactions, identity theft, and financial losses.')
# st.markdown("Also, our application aids credit card companies and banks in enhancing their credit card fraud detection systems, enabling them to identify and recognize fraudulent credit card transactions more effectively.")
# st.markdown('Fraud Detection App is a cutting-edge fraud detection application that empowers businesses to proactively safeguard their operations against the ever-evolving threat of fraudulent activities. With its powerful artificial intelligence and advanced machine learning algorithms, Fraud Detection App offers unparalleled protection and peace of mind.')


html_style8 = """
<div>
<p style="font-size:1rem; margin-bottom: 3rem;">Fraud Detection App is a cutting-edge fraud detection application that empowers businesses to proactively safeguard their operations against the ever-evolving threat of fraudulent activities. With its powerful artificial intelligence and advanced machine learning algorithms, Fraud Detection App offers unparalleled protection and peace of mind.</p>

</div>"""
st.markdown(html_style8,unsafe_allow_html=True)


html_style4 = """
<div style="padding:8px;">
<h2 style="color:#61ABFB; font-size:42px; border-left: 4px solid #61ABFB; padding-left: .5rem; margin-bottom: 1rem">Stay one step ahead of fraudsters</h2>
</div>"""
st.markdown(html_style4,unsafe_allow_html=True)
# st.markdown('Powered by state-of-the-art technology, Fraud Detection App is designed to detect and prevent fraudulent activities in real-time. Its robust algorithms analyze vast amounts of data, quickly identifying patterns, anomalies, and suspicious behaviors that may indicate fraud attempts. By staying one step ahead, Fraud Detection App ensures that you can protect your business and customers from financial loss and reputational damage.')


html_style8 = """
<div>
<p style="font-size:1rem; margin-bottom: 3rem; ">Powered by state-of-the-art technology, Fraud Detection App is designed to detect and prevent fraudulent activities in real-time. Its robust algorithms analyze vast amounts of data, quickly identifying patterns, anomalies, and suspicious behaviors that may indicate fraud attempts. By staying one step ahead, Fraud Detection App ensures that you can protect your business and customers from financial loss and reputational damage.</p>

</div>"""
st.markdown(html_style8,unsafe_allow_html=True)


html_style4 = """
<div style="padding:8px;">
<h2 style="color:#61ABFB; font-size:42px; border-left: 4px solid #61ABFB; padding-left: .5rem; margin-bottom: 1rem">Features</h2>
</div>"""
st.markdown(html_style4,unsafe_allow_html=True)
# Display the image with rounded corners
st.markdown(css2, unsafe_allow_html=True)
image_path4 = 'fr7.png'
image_html4 = f'<div class="img2"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path4, "rb").read()).decode()}"></div>'
st.markdown(image_html4, unsafe_allow_html=True)
# st.markdown("You can implements machine learning models to analyze historical transaction data and identify potential fraud.")


html_style8 = """
<div>
<p style="font-size:1rem; margin-bottom: 3rem">You can implements machine learning models to analyze historical transaction data and identify potential fraud.</p>

</div>"""
st.markdown(html_style8,unsafe_allow_html=True)


# Display the CSS style
st.markdown(css2, unsafe_allow_html=True)


html_style7 = """
<div>
<h2 style="color:#61ABFB; font-size:42px; border-left: 4px solid #61ABFB; padding-left: .5rem; margin-bottom: 1rem">Do you work in the banking field, and you're bored of old technique?</h2>
</div>"""
st.markdown(html_style7, unsafe_allow_html=True)


# Display the image with rounded corners
image_path2 = 'fr11.png'
image_html2 = f'<div class="img2"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path2, "rb").read()).decode()}"></div>'
st.markdown(image_html2, unsafe_allow_html=True)


html_style6 = """
<div>
<h4 style="color:#049395;text-align:center;font-size:24px">Hopefuly, you are in the right place, you can now use our Machine Learning Model and find the probability of fraud to save the customers.</h4>
<hr style="background: #61ABFB;">
</div>"""
st.markdown(html_style6,unsafe_allow_html=True)