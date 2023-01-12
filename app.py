import streamlit as st
from PIL import Image
import boto3

client=boto3.client('rekognition')


def open_image(img):
    return Image.open(img)

st.markdown("""
<style>
.stProgress .st-bo {
    background-color: green;
}
</style>
""", unsafe_allow_html=True)

st.title('Emotion Recognition')

img_file=st.file_uploader('upload face image',type=['png','jpg','jpeg'])

if img_file is not None:
    file_details={}
    file_details['type']=img_file.type
    file_details['name']=img_file.name
    file_details['size']=img_file.size
    st.write(file_details)
    st.image(open_image(img_file),width=250)

    with open('test.jpg','wb') as f:
        f.write(img_file.getbuffer())
    
    imageSource=open('test.jpg','rb')

    response=client.detect_faces(
        Image={'Bytes':imageSource.read()},
        Attributes=['ALL']
    )
    response=response['FaceDetails'][0]

    for i in response['Emotions']:
        st.text(i['Type']+ ' ')
        st.progress(int(i['Confidence']))
