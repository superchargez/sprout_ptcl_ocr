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
# Define a dictionary to map long names to short names
name_map = {
    'Upaisa': 'Pesa',
    'Ufone': 'Fone',
    'Corporate': 'Corp',
}

# Replace long names with short names in the groups list
groups = ['Facebook Ufone', 'Facebook Upaisa', 'Facebook Corporate', 'Twitter Ufone', 'Twitter Upaisa', 'Instagram Ufone', 'Instagram Upaisa', 'Linkedin Ufone']
groups = [' '.join([name_map.get(word, word) for word in group.split()]) for group in groups]

# Define the columns
cols = st.columns(len(groups))

# Now you can use this updated groups list in your for loop
for i, group in enumerate(groups):
    network, name = group.split(' ', 1)
    logo = Image.open(f'C:\\Users\\jawad\\Downloads\\projects\\ocr\\images\\logos\\{network.lower()}.png')
    cols[i].image(logo, use_column_width=False)
    cols[i].checkbox(name, value=True, key=group)  # Added a unique key for each checkbox
