import streamlit as st
from api.people_api import deserialize_file, Person

st.set_page_config(
    page_title='Home',
    page_icon='🏠'
)
 
option = st.selectbox('Select Person', deserialize_file(), index=0)
print(option)

st.experimental_set_query_params()

if option:
    person = Person(option.first_name, option.last_name, option.age)
    link = person.generate_link()
    st.write(f"check this out {link}")