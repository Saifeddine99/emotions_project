import streamlit as st 

import pandas as pd 
import numpy as np
import pickle

import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Self Harm Risk", page_icon="	:clipboard:", layout="centered")

st.markdown("<h1 style='color: #0B5345;'>This Web App predicts the risk of self harm based on patient's emotions:</h1>", unsafe_allow_html = True)
st.write("#")
st.write("#")

col_1,col_2,col_3,col_4,col_5=st.columns([2,0.1,2,0.1,2])

with col_1:
    st.subheader("Feliz:")
    feliz=st.number_input(":h",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

    st.subheader("Vergonzoso:")
    vergonzoso=st.number_input(":'éf'h",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

    st.subheader("Culpable:")
    culpable=st.number_input(":hf'f",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

with col_3:
    st.subheader("Enfadado:")
    enfadado=st.number_input(":h1",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

    st.subheader("Angustiado:")
    angustiado=st.number_input(":hf'f1",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

    st.subheader("Frustrado:")
    frustrado=st.number_input(":h1fef",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

with col_5:
    st.subheader("Triste:")
    triste=st.number_input(":h2",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

    st.subheader("Relajado:")
    relajado=st.number_input(":h1dz",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

    st.subheader("Otra:")
    otra=st.number_input(":hef1",min_value=0,max_value=100,step=1,label_visibility ="collapsed")

    st.write("#")

st.write("#")
st.write("#")

my_array = np. array([feliz,enfadado,triste,vergonzoso,angustiado,relajado,culpable,frustrado,otra])
my_array=my_array.reshape(1,9)

emotions_list=["feliz","enfadado","triste","vergonzoso","angustiado","relajado","culpable","frustrado","otra"]
emotions=pd.DataFrame(my_array,columns=emotions_list)
st.subheader("Here is the summary of chosen emotions:")
st.dataframe(emotions,hide_index=True) 

st.write("#")
st.write("#")

col1, col2, col3 = st.columns([3,2,3])
with col2:
    center_button = st.button('Predict self harm risk')
if (center_button):
    
    # load model from file
    with open("trained_model.pickle.dat", 'rb') as f:
        model = pickle.load(f)
    # make predictions for test data
    y_pred = model.predict(emotions)
    st.write("#")
    if y_pred==1:
        st.header("There is a risk of self harm !")
    else:
        st.header("There is no risk of self harm !")