import streamlit as st
from streamlit_option_menu import option_menu
from selfpages import homepage, educitionpage, experiencepage, resumepage, concatpage
from compoents import footer

title = "Persional Site"

st.set_page_config(page_title=f"{title}", layout="wide")

icons = ["house", "book", "box", "file-earmark-person", "chat-square-dots"]
menus = ["Home Page", "Education Page", "Experience Page", "Resume Page", "Contact Page"]

with st.sidebar:
    menu = option_menu(title, menus, icons=icons, menu_icon="cast", default_index=1)
    
if menu == menus[0]:
    homepage.main()
if menu == menus[1]:    
    educitionpage.main()
if menu == menus[2]:
    experiencepage.main()
if menu == menus[3]:
    resumepage.main()
if menu == menus[4]:
    concatpage.main()

footer.display_footer()
st.markdown("""
    <style>
        .stSidebar {
            height: calc(100vh - 38px) !important;
        }
    </style>""", unsafe_allow_html=True)