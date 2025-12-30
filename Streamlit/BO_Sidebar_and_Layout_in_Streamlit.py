import streamlit as st

#------------ Sidebar in Streamlit ------------#
# st.sidebar.title("Menu")

# name = st.sidebar.text_input("Enter your name: ")
# st.sidebar.write("---")
# role = st.sidebar.selectbox("Select role: ", ["DS Engineer","AI Engineer","ML Engineer", "Web Developer"])

# st.write("Name: ", name)
# st.write("Role: ", role)



#------------ Layout in Streamlit ------------#
# col1, col2 = st.columns(2)

# with col1:
#     st.header("Column 1")
#     st.write("This is the first column.")

# with col2:
#     st.header("Column 2")
#     st.write("This is the second column.")



#------------ Real Internship-Style Layout ------------#

st.title("Internship Dashboard")

st.sidebar.header("User Input")

name = st.sidebar.text_input("Name")
domain = st.sidebar.selectbox("Domain", ["","Data Science", "AI", "ML", "Web Development"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Profile")
    st.write("Name: ",name)

with col2:
    st.subheader("Domain")
    st.write("Selected Domain: ", domain)