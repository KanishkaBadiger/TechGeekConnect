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
        background:linear-gradient(90deg, #4CAF50, #2E86C1);
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
            background-color: #f4f6f9;
}
            
/*Custom text style*/
</style>

""",unsafe_allow_html=True)

st.markdown(
    '<div class="header">Streamlit CSS Dashboard</div>', 
    unsafe_allow_html=True
)

#How to use this properties

st.sidebar.title("Navigation")
st.sidebar.radio(
    "Go to",
    ("Home", "Analytics", "Settings")
)

#Options like
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Users</div>
        <h2>1,234</h2>
        <p>Active users</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Sales</div>
        <h2>$12,345</h2>
        <p>Total sales</p>
    </div>
    """, unsafe_allow_html=True)    

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Orders</div>
        <h2>567</h2>
        <p>New orders</p>
    </div>
    """, unsafe_allow_html=True)    
