import streamlit as st

st.set_page_config(page_title="CSS Layout Demo", layout="wide")

st.markdown("""
<style>

/* Adjust the main block container to have more top padding */
/* Remove default padding */
.block-container {
    padding-top: 2rem;
}
            
/* Style headers with a custom font and color */
/*Header*/
.header{
        font-size:35px;
        font-weight:bold;
        color:white;
        background:linear-gradient(90deg, #ff7e5f, #feb47b);
        padding:20px;
        border-radius:10px;
        text-align:center;
        margin-bottom:25px;
}
            
/*Card*/
.card{
    background-color:#ffffff;
    padding:20px;
    border-radius:15px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
}
            
/*Card title*/
.card-title{
    font-size:20px;
    font-weight:600;
    margin-bottom:10px;
}
            
.kanishka{
    color: #4CAF50;
    font-weight: bold;
    font-size: 150px;
    text-align: center;'
}
            
/*Sidebar styles*/
section[data-testid="stSidebar"] {

            


""")