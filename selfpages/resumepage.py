import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

annotations = []

def main():
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Resume <-
    </div>''', unsafe_allow_html=True)
    
    pdf_viewer("statics/resume.pdf", annotations=annotations)
    
    with open("statics/resume.pdf", "rb") as f:
        pdf = f.read()
    
    st.sidebar.download_button(
        label="Download resume",
        data=pdf,
        file_name="resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )