import streamlit as st
from compoents import mycompoent, interactive

def main():
    st.sidebar.markdown('''
    <br><div style="text-align: center; font-size: 18px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Contact Me <-
    </div>''', unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    Feel free to reach out to me through any of the following channels:  
    **Direct Contact**  
    **Email**: [1155216514@link.cuhk.edu.hk](mailto:1155216514@link.cuhk.edu.hk)  
    **Phone**: +852 5778 0302  
    **LinkedIn**: [linkedin.com/in/Melodysun](https://www.linkedin.com/in/melodysun/)  
    **GitHub**: [github.com/Melodysun](https://github.com/Melidy74)  
    """)
    
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Send Me a Message <-
    </div>''', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            name = st.text_input("Name")
        
        with col2:
            email = st.text_input("Email")
            
        with col3:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
        
    
    st.markdown("---")
    
    st.info("""
    **Office Hours:** I'm generally available for virtual meetings Monday through Friday, 9 AM to 5 PM CST.
    Please email me to schedule a call or video conference.
    """)