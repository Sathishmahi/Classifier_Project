import streamlit as st
import os 
st.title("Classifier")
st.header("Welcome to Classifier")
st.subheader("by Sathish")

try:
    # for _ in range(int(no_of_classes)):
    file_details=st.file_uploader(label="select files note class name and file name must be same", type=['mp4','AVI','WebM'], accept_multiple_files=True,
                disabled=False, label_visibility="visible")
    for file_name in file_details:
        os.makedirs(file_name.name,exist_ok=True)

except ValueError as e:
    st.exception(e)
    raise e


# Create a simple button that does nothing
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")