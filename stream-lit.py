
# create a sidebar that includes 
# input file
# input file name
# input player description
# run the agent
# print the report
# save the report with the input name
! pip install -- upgrade pip

from xml.dom.minidom import Document
import streamlit as st

buffer, col2, col3 = st.columns([1, 20, 60])

with col2:
    player = st.sidebar.text_input("player name"),
    image = st.sidebar.file_uploader("Choose a file", accept_multiple_files=True)


with col3:
    Markdown(results)

try:
    doc = Document('cleanded_doc.docx')
    doc_para = doc.add_paragraph(results)
    doc.save('cleaned_doc.docx')
except Exception as e:
    print(f"An error occurred: {e}")