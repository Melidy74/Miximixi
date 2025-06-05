import streamlit as st

def element1(text, t, color="rgba(0,0,0,0.05)"):
    st.markdown(f'''
    <div>
        <div style="font-size: 24px; font-weight: bold; margin-bottom: 5px; border-bottom: 1px solid black;">{text}</div>
        <div style="background: {color}; padding: 12px; border-radius: 6px;">{t}</div>
    </div>''', unsafe_allow_html=True)