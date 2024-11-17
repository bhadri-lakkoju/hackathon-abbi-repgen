
import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to AbbI GenReport')


# Declare a form and call methods directly on the returned object
form = st.form(key='my_form')
form.text_input(label='Enter text to view the report')
submit_button = form.form_submit_button(label='Get Report')
form.text_area(label='Report data', height=300)


