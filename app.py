import streamlit as st
from PIL import Image
import boto3

accessKey=''
secretKey=''
region='us-east-1'

def load_image(img):
    return Image.open(img)

st.title('Emotion Recognition using AWS')

img_file=st.file_uploader('Upload the Face',type=['png','jpg','jpeg'])

if img_file is not None:
    file_details={}
    file_details['name']=img_file.name
    file_details['type']=img_file.type
    file_details['size']=img_file.size
    st.write(file_details)
    st.image(load_image(img_file),width=250)

    with open('uploads/src.jpg','wb') as f:
        f.write(img_file.getbuffer())
    
    client=boto3.client(
        'rekognition',
        aws_access_key_id=accessKey,
        aws_secret_access_key=secretKey,
        region_name=region)
    
    sourceImage=open('uploads/src.jpg','rb')
    
    response=client.detect_faces(
        Image={'Bytes':sourceImage.read()},
        Attributes=[
            'ALL'
        ]
    )
    #st.write(response)
    if response['FaceDetails']:
        st.write(response['FaceDetails'][0]['Emotions'])
    

