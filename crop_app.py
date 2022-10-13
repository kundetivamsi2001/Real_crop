import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
from PIL import Image
import warnings
def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model
html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> CROP RECOMMENDER 🌽🌾🌱 </h1>
    
    </div>
    """
def main():
    image = Image.open('logo.png')
    st.image(image,
           use_column_width=True)
    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("We recommend the most suitable crop to cultivate ☘️")
    st.subheader('Fill the below details')
    N=st.number_input('Nitrogen (%)',1,100)
    P=st.number_input('Phosporus(%)',1,100)
    K=st.number_input('Potassium(%)',1,100)
    temp=st.number_input('Temperature(c)',0.0,100.0)
    humid=st.number_input('Humidity',0.0,100.0)
    ph=st.number_input('Ph (0-7)',0.0,100.0)
    rain=st.number_input('Rainfall (mm)',0.0,100.0)
    inputs= [N, P, K, temp, humid, ph, rain]
    pred= np.array(inputs).reshape(1,-1)
    if st.button('Predict'):
                loaded_model = load_model('model.pkl')
                prediction = loaded_model.predict(pred)
                
                st.success(f"🔍Results  : {prediction.item().title()} are recommended by the Model  for your farm.")
                st.warning("⚠️It is an A.I generated crop prediction for Educational purpose  only not for commercial use")

if __name__ == '__main__':
	main()
