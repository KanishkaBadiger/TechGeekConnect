import streamlit as st

#---------Integration of button() and text_input()---------#

# st.title("button() and text_input() use example in Streamlit")

# name = st.text_input("Enter your name: ")

# if st.button("Submit"):
#     st.write(f"Welcome on board! {name}")

# age = st.number_input("Enter your age: ")

# if age:
#     st.write(f"Your age is: {age}")



#-----------------HW:User Info app---------#

st.title("User Info App")

name = st.text_input("Enter your name: ")
age = st.number_input("Enter your age:", min_value=0)

if st.button("Show Info"):
    st.write("Name: ", name)
    st.write("Age: ", age)




