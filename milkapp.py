# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:33:12 2023

@author: harin
"""

import numpy as np
import pickle
import streamlit as st

loading_model = pickle.load(open("C:/Users/harin/milk quality prediction/milk_model_1.sav", 'rb'))
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/bottles-fresh-milk-with-american-cookies_23-2148239836.jpg?w=2000");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


def milkqualityy_prediction(input_data):
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction= loading_model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]== 0):
         return"𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐈𝐋𝐊 𝐈𝐒 𝐋𝐎𝐖"
    elif(prediction[0]==2):
         return"𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐈𝐋𝐊 𝐈𝐒 𝐌𝐄𝐃𝐈𝐔𝐌"
    else:
         return"𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐈𝐋𝐊 𝐈𝐒 𝐇𝐈𝐆𝐇"
         
         
def main():
    
    st.title('𝐌𝐢𝐥𝐤 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐏𝐫𝐞𝐝𝐢𝐜𝐭𝐢𝐨𝐧')
    
    pH = st.text_input('𝐏𝐇 𝐋𝐄𝐕𝐄𝐋')
    Temprature = st.text_input('𝐓𝐄𝐌𝐏𝐄𝐑𝐀𝐓𝐔𝐑𝐄')	
    Taste = st.text_input('𝐓𝐀𝐒𝐓𝐄 𝐋𝐄𝐕𝐄𝐋')
    Odor = st.text_input('𝐎𝐃𝐎𝐔𝐑 𝐋𝐄𝐕𝐄𝐋')
    Fat = st.text_input('𝐅𝐀𝐓 𝐋𝐄𝐕𝐄𝐋')
    Turbidity = st.text_input('𝐓𝐔𝐑𝐁𝐈𝐃𝐈𝐓𝐘')	
    Colour = st.text_input('𝐂𝐎𝐋𝐎𝐑 𝐋𝐄𝐕𝐄𝐋 𝐎𝐅 𝐌𝐈𝐋𝐊')
    
    # Prediction code
    predictionn = ''
    
    if st.button('𝐏𝐑𝐄𝐃𝐈𝐂𝐓'):
        predictionn = milkqualityy_prediction([pH, Temprature, Taste,	Odor, Fat, Turbidity, Colour
])
        
    st.success(predictionn)
    
if __name__=='__main__':
    main()
