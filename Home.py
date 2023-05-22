import streamlit as st
import pandas

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

# Se coloca un pequeño texto descriptivo debajo de las dos columnas superiores
info_text = '''
Below you can check all the applications I have made with Python. 
Please feel free to contact me for any question or issue.
'''
st.info(info_text)

# Se crea una variable df con pandas y se extrae la información de lo títulos,
    # descripción, imagenes y enlace en columnas nuevas.
df = pandas.read_csv('data.csv', sep=';')
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])  # Especificamos las medidas de las columnas. Se crea una
                                                        # columna vacia en el centro por el espacio.
with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image('images/' + rows['image'])
        st.write(f'[Source code]({rows["url"]})') # Este es un formato especial para los hipervínculos

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image('images/' + rows['image'])
        st.write(f'[Source code]({rows["url"]})')
