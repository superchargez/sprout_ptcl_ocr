import streamlit as st
import pandas as pd
from PIL import Image
import ocr  # assuming maintain.py is in the same directory
import outputter  # assuming outputter.py is in the same directory

# Load the logo from the file
logo = Image.open('ptcl.png')

# Display the logo in the sidebar
st.sidebar.image(logo, use_column_width=False)

# Load the DataFrame from the CSV file
df = pd.read_csv('output.csv')

# Sidebar controls
st.sidebar.header('Controls')
run_ocr = st.sidebar.button('OCR', key='run_ocr')
generate_csv = st.sidebar.button('Generate CSV', key='generate_csv')
browse_images = st.sidebar.button('Browse for Images', key='browse_images')
show_comments = st.sidebar.checkbox('Comments', value=True, key='show_comments')
show_replies = st.sidebar.checkbox('Replies', value=True, key='show_replies')
show_time = st.sidebar.checkbox('Time', value=True, key='show_time')


# Run maintain.py when the OCR button is clicked
if run_ocr:
    ocr.ocr()  # assuming maintain.py has a function called run()

# Run outputter.py when the Generate CSV button is clicked
if generate_csv:
    outputter.outputter()  # assuming outputter.py has a function called run()

# Filter the DataFrame based on the checkboxes
if not show_comments:
    df = df.loc[:, ~df.columns.str.contains('Comments')]
if not show_replies:
    df = df.loc[:, ~df.columns.str.contains('Replies')]
if not show_time:
    df = df.loc[:, ~df.columns.str.contains('Time')]

# Main DataFrame display
st.dataframe(df)

# Bottom page with logos and checkboxes
st.header('Select Groups')

# Define the networks and accounts
networks = ['Facebook', 'Twitter', 'Instagram', 'Linkedin']
accounts = ['Ufone', 'Upaisa', 'Corporate']

# Create a row of logos and accounts
logos_and_accounts = st.columns(len(networks))
for i, network in enumerate(networks):
    logo = Image.open(f'C:\\Users\\jawad\\Downloads\\projects\\ocr\\images\\logos\\{network.lower()}.png')
    logos_and_accounts[i].image(logo, use_column_width=False)
    logos_and_accounts[i].write(network)

# Create a separate row of checkboxes
checkboxes = st.columns(len(networks))
checkboxes_dict = {}
for i, account in enumerate(accounts):
    checkbox = checkboxes[i].checkbox(account, value=True, key=f'{account}_checkbox')  # Added a unique key for each checkbox
    checkboxes_dict[account] = checkbox

# Filter the DataFrame based on the checkboxes at the bottom
for account, checkbox in checkboxes_dict.items():
    if not checkbox:
        df = df.loc[:, ~df.columns.str.contains(account)]
