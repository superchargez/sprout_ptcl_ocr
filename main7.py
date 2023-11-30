import streamlit as st
import pandas as pd
from PIL import Image
import ocr  # assuming maintain.py is in the same directory
import outputter  # assuming outputter.py is in the same directory
import os

# Initialize df as an empty DataFrame
df = pd.DataFrame()

# Load the logo from the file
logo = Image.open('ptcl.png')

# Display the logo in the sidebar
st.sidebar.image(logo, use_column_width=False)

# Sidebar controls
st.sidebar.header('Control Buttons')
run_ocr = st.sidebar.button('RUN OCR', key='run_ocr')
generate_csv = st.sidebar.button('Generate CSV', key='generate_csv')

st.sidebar.header('Data Types')
show_comments = st.sidebar.checkbox('Comments', value=True, key='show_comments')
show_replies = st.sidebar.checkbox('Replies', value=True, key='show_replies')
show_time = st.sidebar.checkbox('Time', value=True, key='show_time')

# Run maintain.py when the OCR button is clicked
if run_ocr:
    ocr.ocr()  # assuming maintain.py has a function called run()

# Run outputter.py when the Generate CSV button is clicked
if generate_csv:
    outputter.outputter()  # assuming outputter.py has a function called run()

# Upload the CSV file
if df.empty:
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    elif os.path.isfile('output.csv'):
        df = pd.read_csv('output.csv')
    else:
        st.write("Please upload a CSV file.")

# Filter the DataFrame based on the checkboxes
if not df.empty:
    if not show_comments:
        df = df.loc[:, ~df.columns.str.contains('Comments')]
    if not show_replies:
        df = df.loc[:, ~df.columns.str.contains('Replies')]
    if not show_time:
        df = df.loc[:, ~df.columns.str.contains('Time')]

# Define the networks and accounts
networks = ['facebook', 'twitter', 'instagram', 'linkedin']
accounts = ['Ufone', 'Upaisa', 'Corporate']
st.header('Select Groups')
# Create a row of logos and checkboxes
logos_and_checkboxes = st.columns(len(networks))
checkboxes_dict = {}
for i, network in enumerate(networks):
    logo = Image.open(f'C:\\Users\\jawad\\Downloads\\projects\\ocr\\images\\logos\\{network.lower()}.png')
    logos_and_checkboxes[i].image(logo, use_column_width=False)
    checkbox = logos_and_checkboxes[i].checkbox(network, value=True, key=f'{network}_checkbox')  # Added a unique key for each checkbox
    checkboxes_dict[network] = checkbox

# Create checkboxes for the accounts in the sidebar
st.sidebar.header('Choose Accounts')
account_checkboxes_dict = {}
for account in accounts:
    checkbox = st.sidebar.checkbox(account, value=True, key=f'{account}_checkbox')  # Added a unique key for each checkbox
    account_checkboxes_dict[account] = checkbox

# Filter the DataFrame based on the checkboxes at the bottom
for network, checkbox in checkboxes_dict.items():
    if not checkbox:
        df = df.loc[:, ~df.columns.str.contains(network)]

# Filter the DataFrame based on the account checkboxes
for account, checkbox in account_checkboxes_dict.items():
    if not checkbox:
        df = df.loc[:, ~df.columns.str.contains(account)]

# Main DataFrame display
if not df.empty:
    st.dataframe(df)
    csv = df.to_csv(index=False)
    download_csv = st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv',
    )
