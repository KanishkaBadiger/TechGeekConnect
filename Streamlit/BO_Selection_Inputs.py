
import streamlit as st

#--------------st.selectbox() – Dropdown Example-------------------#
# '''
st.title("Selectbox Example")

city = st.selectbox(
    "Select your City: ",
    [" ", "Pune", "Mumbai", "Delhi", "Banglore", "Chennai"]
)

st.write("You selected: ", city)
# '''

#-----------------st.radio() - Radio Buttons Example-------------------#
st.title("Radio Button Example")
gender =  st.radio(
    "Select gender",
    ["-","Male", "Female", "Other"]
)

st.write("Gender:", gender)


#-----------------st.checkbox()-_True/false------------------#
st.title("Checkbox Example")
agree = st.checkbox("I agree to the terms and conditions")

if agree:
    st.write("Thank you for agreeing!")

