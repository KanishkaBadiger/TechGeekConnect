import streamlit as st
import pandas as pd

st.title("Student Information Application")

# Initialize session state to store student data
if "students" not in st.session_state:
    st.session_state.students = []

# Create tabs
tab1, tab2, tab3 = st.tabs(["Home", "Student Form", "Student Data"])

# -------------------- TAB 1: HOME --------------------
with tab1:
    st.title("This is Home Tab")
    st.subheader("Welcome to Application")

# -------------------- TAB 2: STUDENT FORM --------------------
with tab2:
    st.header("Student Information Form")

    with st.form("student_form"):
        name = st.text_input("Student Name")
        age = st.number_input("Student Age", min_value=1, max_value=100)
        department = st.text_input("Student Department")

        submit = st.form_submit_button("Submit")

        if submit:
            student_data = {
                "Name": name,
                "Age": age,
                "Department": department
            }

            st.session_state.students.append(student_data)
            st.success("Student data submitted successfully!")

# -------------------- TAB 3: STUDENT DATA --------------------
with tab3:
    st.header("Submitted Student Data")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)
        st.table(df)
    else:
        st.info("No student data available yet.")

