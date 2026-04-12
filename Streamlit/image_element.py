import streamlit as st

st.title("Media Elements", anchor=False)
st.divider()

#internal
st.image("images/Book.jpg")

#url
st.image("https://img.freepik.com/free-photo/courage-man-jump-through-gap-hill-business-concept-idea_1323-262.jpg?semt=ais_hybrid&w=740&q=80")

images = st.file_uploader("Enter Images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if images:
    col = st.columns(len(images))
    
    for i, image in enumerate(images):
        with col[i]:
            st.image(image)