import streamlit as st
import uuid


def add_row(nome_item):
    col11, col22, col33, col44 = st.columns(4)

    with col11:
        st.text("  _____  ")
        st.write(nome_item)
        
    with col22:
        number22 = st.number_input(label="", value=0, format="%d", key=str(uuid.uuid4()))

    with col33:
        option = st.selectbox(
     '',
     ('Alta', 'Media', 'Baixa'),key=str(uuid.uuid4()))

    with col44:
        justificativa = st.selectbox(
     '',
     ('XXXXX', 'YYYYYY','ZZZZZ'),key=str(uuid.uuid4()))
        

st.title('Plano Anual de Compras')

with st.form('my_form', clear_on_submit=True):
    title = st.text_input('Código Escola', '')

    #header
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text("Itens")
                
    with col2:
        st.text("Quantitativo")
        
    with col3:
        st.text("Urgencia")
        
    with col4:
        st.text("Justificativa")

    #body    
    add_row("Cadeiras")
    
    add_row("Mesas")

    add_row("Projetores")

    add_row("Kit Educatron")

    add_row("Mesas Refeitorio")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Parabens! Submetido :)")
