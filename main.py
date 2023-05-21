import streamlit as st

st.set_page_config(layout='wide', page_icon='random')

col1, col2 = st.columns(2)  # Columnas para la fotografía y una breve descripción de mi

with col1:  # Foto
    st.image('images/photo.jpg')

with col2:  # Descripción
    st.title('David Ramirez')
    content = """
    Hi! Im David, and this is my web app.
    """
    st.info(content)

info_text = '''
Below you can check all the applications I have made with Python. 
Please feel free to contact me for any question or issue.
'''
st.info(info_text)


