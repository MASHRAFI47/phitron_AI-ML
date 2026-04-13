import streamlit as st

images = st.file_uploader("Enter image", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

if images:
    if len(images) <= 3:
        st.success("Pic uploaded successfully")
        col = st.columns(len(images))
        for i, per_image in enumerate(images):
            with col[i]:
                st.image(per_image)
            
    else:
        st.error("You can't upload more than 3 images")