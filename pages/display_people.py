import streamlit as st
from api.people_api import deserialize_file, Person
import logging
import rich

url = st.experimental_get_query_params()
people = None
logging.debug('line 7')

if 'options' not in st.session_state:
    rich.print('[green] options [/green]')
    st.session_state['options'] = deserialize_file()
if 'default' not in st.session_state:
    rich.print('[blue] default [/blue]')
    st.session_state.default = st.session_state.options

if url:
    logging.debug('line 15')
    person = Person()
    person.first_name = url['first'][0]
    person.last_name = url['last'][0]
    person.age = url['age'][0]
    for index,key in enumerate(st.session_state.options):
        if str(key) == str(person):
            rich.print('[magenta] hi [/magenta]')
            st.session_state.default=st.session_state.options[index]
            rich.print('[magenta] bye [/magenta]')
options = []
with st.sidebar:
    rich.print('[red] sidebar [/red]')
    options = st.multiselect(
        label="multiselect",
        options=st.session_state.options,
        default=st.session_state.default
    )
    rich.print('[underline red] sidebar [/underline red]')

for person in options:
    st.text(f'First name: {person.first_name}')
    st.text(f'Last name: {person.last_name}')
    st.text(f'Age: {person.age}')
    st.image(person.image())
    st.markdown('---')