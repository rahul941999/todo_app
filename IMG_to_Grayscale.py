import streamlit as st
from PIL import Image, UnidentifiedImageError

st.set_page_config(layout='wide')
st.title('Convert Images into Greyscale Images(black and white).',)
with st.expander('start camera'):
    cam_img = st.camera_input("Camera")
    if cam_img:
        img = Image.open(cam_img)
        g_img = img.convert('L')
        st.image(g_img)

with st.expander('upload image'):
    upl_img = st.file_uploader('upload Image')
    if upl_img:
        try:
            img = Image.open(upl_img)
            g_img = img.convert('L')
            st.image(g_img)
        except UnidentifiedImageError:
            st.error('please select an image!!')
