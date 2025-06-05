import streamlit as st

def display_footer():
    """Display a consistent footer across all pages"""
    footer = """
    <div class="footer">
        <p>© 2023 Sarah Johnson | <a href="mailto:sarah.johnson@example.com" style="color: #2C3E50; text-decoration: none;">Contact</a> | Last updated: May 2023</p>
    </div>
    
    <style>
    .footer {
        position: fixed;
        top: calc(100vh - 36px);
        left: 0px;
        height: 36px;
        width: 100%;
        background: #8E99A5;
        text-align: center;
        font-size: 0.8rem;
        color: black;
        z-index: 10 !important;
        line-height: 36px;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True) 