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
run_ocr = st.sidebar.button('OCR')
generate_csv = st.sidebar.button('Generate CSV')
browse_images = st.sidebar.button('Browse for Images')
show_comments = st.sidebar.checkbox('Comments', value=True)
show_replies = st.sidebar.checkbox('Replies', value=True)
show_time = st.sidebar.checkbox('Time', value=True)
select_all = st.sidebar.checkbox('Select All', value=True)

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

# Define the columns
cols = st.columns(4)

# Define the networks and accounts
networks = ['Facebook', 'Twitter', 'Instagram', 'Linkedin']
accounts = ['Ufone', 'Upaisa', 'Corporate']

# Now you can use this updated groups list in your for loop
checkboxes = []
for i, network in enumerate(networks):
    logo = Image.open(f'C:\\Users\\jawad\\Downloads\\projects\\ocr\\images\\logos\\{network.lower()}.png')
    cols[i].image(logo, use_column_width=False)
    for account in accounts:
        checkbox = cols[i].checkbox(account, value=True, key=f'{network} {account}')  # Added a unique key for each checkbox
        checkboxes.append((f'{network} {account}', checkbox))

# Filter the DataFrame based on the checkboxes at the bottom
for group, checkbox in checkboxes:
    if not checkbox:
        df = df.loc[:, ~df.columns.str.contains(group)]
