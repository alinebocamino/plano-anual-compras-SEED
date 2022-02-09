import streamlit as st

st.title('SEED eh campeao')

with st.form('my_form', clear_on_submit=True):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
        

st.write("Outside the form")
