# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from textwrap import fill
import pickle
import requests
import base64
import json
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder




# st.markdown("# Prediction page ")
st.sidebar.markdown("# Prediction page 🎉")
# background-color:#996600;

html_style = """
<div style="padding:8px;border-radius:40px;margin-bottom:24px">
<h2 style="color:#0B75CB;text-align:center;font-size:32px">Fraud Detection</h2>
</div>"""
st.sidebar.markdown(html_style,unsafe_allow_html=True)

html_style2 = """
<div style="padding:8px; border-radius:40px;">
<h2 style="color: #0B75CB;text-align:center;font-size:64px">Predicting with ML 🎉</h2>
</div>"""
st.markdown(html_style2,unsafe_allow_html=True)

# img2 = Image.open("ch4.png")
# st.image(img2, caption="jobs")

# Define the CSS style
# border-radius: 200px;
css = """
<style>
    .rounded-image {
        overflow: hidden;
        padding: 0px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
        margin-left: 30px;
    }
</style>
# """

# Display the CSS style
st.markdown(css, unsafe_allow_html=True)

# Display the image with rounded corners
image_path = 'fr10.png'
image_html = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}"></div>'
st.markdown(image_html, unsafe_allow_html=True)

# number_project=st.sidebar.selectbox("Select Num of Projects on last year", (1, 3, 4, 5, 6, 7, 8, 9,10)) 


import streamlit as st


# V2 = st.sidebar.number_input(
#     "Select the value of V2",
#     -5.00, 6.00, step=0.1,
#     key="V2",
#     help="Select the value of V2"
# )

# V3 = st.sidebar.number_input(
#     "Select the value of V3",
#     -10.00, 10.00, step=0.1,
#     key="V3",
#     help="Select the value of V3"
# )

V4 = st.sidebar.number_input(
    "Select the value of V4",
    -5.00, 10.00, step=0.1,
    key="V4",
    help="Select the value of V4"
)

V7 = st.sidebar.number_input(
    "Select the value of V7",
    -10.00, 3.00, step=0.1,
    key="V7",
    help="Select the value of V7"
)
V9 = st.sidebar.number_input(
    "Select the value of V9",
    -14.00, 10.00, step=0.1,
    key="V9",
    help="Select the value of V9"
)

V10 = st.sidebar.number_input(
    "Select the value of V10",
    -10.00, 3.00, step=0.1,
    key="V10",
    help="Select the value of V10"
)

V11 = st.sidebar.number_input(
    "Select the value of V11",
    -5.00, 10.00, step=0.1,
    key="V11",
    help="Select the value of V11"
)

V12 = st.sidebar.number_input(
    "Select the value of V12",
    -11.00, 3.00, step=0.1,
    key="V12",
    help="Select the value of V12"
)

V14 = st.sidebar.number_input(
    "Select the value of V14",
    -15.00, 3.00, step=0.1,
    key="V14",
    help="Select the value of V14"
)

V16 = st.sidebar.number_input(
    "Select the value of V16",
    -10.00, 3.00, step=0.1,
    key="V16",
    help="Select the value of V16"
)

V17 = st.sidebar.number_input(
    "Select the value of V17",
    -15.00, 6.00, step=0.1,
    key="V17",
    help="Select the value of V17"
)

# V27 = st.sidebar.number_input(
#     "Select the value of V27",
#     -1.00, 1.00, step=0.1,
#     key="V27",
#     help="Select the value of V27"
# )



filename = "final_rf"
# filename ="RF_model_s"
model = pickle.load(open(filename, "rb"))

my_dict = {
    'V4': V4,
    'V7': V7,
    'V9': V9,
    'V10': V10,
    'V11': V11,
    'V12': V12, 
    'V14': V14,
    'V16': V16,
    'V17': V17, 
    
}



import pandas as pd
import streamlit as st

df = pd.DataFrame.from_dict([my_dict])
df.index = ["----------------Customer Information----------------"] * len(df)
# st.write("<table style='width:100%; text-align:center;'>", unsafe_allow_html=True)
# st.write("<tr><th colspan='", len(styled_data.columns), "' style='font-size: 1.5rem;'>Customer Information</th></tr>", unsafe_allow_html=True)

def highlight_cells(value):
    return "font-size: 1.5rem; color: #1991F3; font-family: italic;"

def display_transposed_table(data):
    # Transpose the dataframe
    transposed_data = data.T

    # Apply the highlight function to the first two rows
    styled_data = transposed_data.style.applymap(highlight_cells, subset=pd.IndexSlice[transposed_data.index[:], :])

    # Format the first two rows with 2 decimal places
    styled_data = styled_data.format("{:.2f}", subset=pd.IndexSlice[transposed_data.index[:], :])

    # Format the rest of the rows as integers
    # styled_data = styled_data.format("{:.0f}", subset=pd.IndexSlice[transposed_data.index[11:], :])

    # Display the styled DataFrame using st.table
    css = """
    <style>
    table {
        color: white;  /* Change text color */
        border-collapse: collapse;
        width: 100%;
    }
    tr {
        font-size: 2rem;
        
    }
    th {
        text-align: center;
        background-color: #CCE7FC;
        border: 2px solid white;
        
    }
    td {
        text-align: center !important;
        flex: 1;
        
    }
    th, td {
        padding: 1rem; 
        text-align: center;
        
    }
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)
    # st.dataframe(styled_data, width=800, height=423)
    st.table(styled_data)
    

display_transposed_table(df)


#########################################################33

# Prediction with user inputs
predict = st.button("Predict")
result2 = model.predict_proba(df)
result = model.predict(df)

css2 = """
<style>
    .rounded-image {
        overflow: hidden;
        margin-right: 50px;
        margin-left: 70px;
        max-width: 80%;
    }
</style>
# """
# st.success(result2[0][1])
try: 
    if predict :            
        
        # if (result[0] == 0):
        #     # st.balloons()
        #     st.confetti()
        #     st.success(f'It seems that it is a normal transaction')
        #     # img = Image.open("ch.jpg")
        #     # st.image(img, caption="stay")


        #     st.markdown(css2, unsafe_allow_html=True)

        #     # Display the image with rounded corners
        #     image_path2 = 'fr5.jpg'
        #     image_html2 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path2, "rb").read()).decode()}"></div>'
        #     st.markdown(image_html2, unsafe_allow_html=True)


        # elif (result[0] == 1):
        # # st.success(f'The employee: {result[0]} the company')
        #     st.warning(f'Fraud Detected Successfuly')
        #     # img = Image.open("ch6.jpg")
        #     # st.image(img, caption="left")
        #     st.markdown(css2, unsafe_allow_html=True)
        #     # Display the image with rounded corners
        #     image_path3 = 'fr4.jpg'
        #     image_html3 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path3, "rb").read()).decode()}"></div>'
        #     st.markdown(image_html3, unsafe_allow_html=True)
        if (result2[0][1] <= 0.5):
            st.info(f'The Probability is about {(1 - result2[0][1]) * 100 } % Not Fraud')
            st.info(f'But be careful ')
            st.markdown(css2, unsafe_allow_html=True)

            # Display the image with rounded corners
            image_path2 = 'fr12.png'
            image_html2 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path2, "rb").read()).decode()}"></div>'
            st.markdown(image_html2, unsafe_allow_html=True)

        elif (result2[0][1] >= 0.5):
            st.error(f'The Probability is about {(result2[0][1]) * 100} % Fraud')
            st.markdown(css2, unsafe_allow_html=True)
            # Display the image with rounded corners
            image_path3 = 'fr4.jpg'
            image_html3 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path3, "rb").read()).decode()}"></div>'
            st.markdown(image_html3, unsafe_allow_html=True)

    else: 
        st.warning('Select values first...')
# st.subheader('Prediction Probability')
# st.write(prediction_probability)
except:
    st.warning('Something went wrong, please try again.')




