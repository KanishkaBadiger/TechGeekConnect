import streamlit as st
import pandas as pd
import PyPDF2
from PIL import Image

st.title("File Processing Demo App")

#Upload any file
uploaded_file = st.file_uploader(
    "Upload a file (PDF, TXT, CSV, Excel, Image)", 
    type=['csv', 'xlsx', 'pdf', 'png', 'jpg', 'jpeg']
)

if uploaded_file is not None:

    #Display file Info
    st.write("File Name:", uploaded_file.name)
    st.write("File Size:", uploaded_file.size, "bytes")
    st.write("File Type:", uploaded_file.type)

    #-----Txt File Processing-----#
    if uploaded_file.type == "text/plain":
        st.header("Text File Content")
        text = uploaded_file.read().decode("utf-8")
        st.text(text)

    #-----CSV file processing-----#
    elif uploaded_file.type == "text/csv":
        st.header("CSV File Content")
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    #-----PDF file processing-----#
    elif uploaded_file.type == "application/pdf":
        st.subheader("PDF File Text")
        try:
            reader = PyPDF2.PdfReader(uploaded_file)
            st.write(f"Total pages: ",len(reader.pages))
            text = reader.pages[0].extract_text()
            st.text(text)
        except :
            st.error("Error reading PDF file.")

    #-----Image file processing-----#
    elif uploaded_file.type.startswith("image/",accept_multiple_files=True):
        st.subheader("Image Preview")
        image = Image.open(uploaded_file)
        # st.image(image, caption="Uploaded Image", use_column_width=True)
        st.image(image, caption="Uploaded Image")
        

    else:
        st.warning("Unsupported file type!")
