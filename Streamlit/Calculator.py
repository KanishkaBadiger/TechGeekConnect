#Build calculator with basic functions using streamlit
# import streamlit as st

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# st.title("Simple Calculator")

# st.write("Select operation: ")

# operation = st.selectbox("Operation", ("Add", "Subtract", "Multiply", "Divide"))
# num1 = st.number_input("Enter first number:")
# num2 = st.number_input("Enter second number:")

# if st.button("Calculate"):
#     if operation == "Add":
#         result = add(num1, num2)
#     elif operation == "Subtract":
#         result = subtract(num1, num2)
#     elif operation == "Multiply":
#         result = multiply(num1, num2)
#     elif operation == "Divide":
#         result = divide(num1, num2)


#     st.write(f"The result is: {result}")



import streamlit as st

# Page configuration
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# App title
st.markdown(
    "<h1 style='text-align: center;'>🧮Streamlit Calculator</h1>",
    unsafe_allow_html=True
)

st.write("---")

# Input section
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result: {result}")

st.write("---")

