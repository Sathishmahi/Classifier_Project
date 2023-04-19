import streamlit as st
import os 
import cv2
st.title("Classifier")
st.header("Welcome to Classifier")
st.subheader("by Sathish")

#  streamlit run app.py --server.port 8501
# npx localtunnel --port 8501
try:
    file_details=st.file_uploader(label="select files note class name and file name must be same", 
                                  type=['mp4','AVI','WebM'], accept_multiple_files=True,
                disabled=False, label_visibility="visible")
    if not file_details:
        for i in file_details:
            with open(f'demo_{i}.webm'.name, mode='wb') as f:
                f.write(file_details.read())

except ValueError as e:
    st.exception(e)
    raise e


# Create a simple button that does nothing
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")