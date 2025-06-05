import streamlit as st
from compoents import mycompoent

def main():
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Education <-
    </div>''', unsafe_allow_html=True)
    
    t0 = """
    Master of Science in Marketing Analytics
    The Chinese University of Hong Kong | September 2024 - May 2025
    GPA: 3.9/4.0
    Thesis: "The Impact of Social Media Sentiment on Brand Equity: an Analytical Approach Using Big Data"
    Relevant Coursework: Machine Learning in Marketing, Social Media Analytics, Marketing Research, Social Media Analytics
    """.strip("\n").splitlines()
    
    t0[1] = '<span style="font-weight: bold;">'+t0[1].replace(" | ", "</span> | ")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    
    t1 = """
    Bachelor of Science in Finance
    The Chinese University of Hong Kong (Shenzhen) | September 2020 - May 2024
    GPA: 3.7/4.0
    Graduated with Honors
    Relevant Coursework: Investment Analysis, Derivatives and Financial Engineering, Financial Risk Management, Financial Statement Analysis, Corporate Finance, Portfolio Management
    """.strip("\n").splitlines()
    
    t1[1] = '<span style="font-weight: bold;">'+t1[1].replace(" | ", "</span> | ")
    
    mycompoent.element1(f"➥ {t1[0]}", "<br>".join(t1[1:]))
    
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Certifications <-
    </div>''', unsafe_allow_html=True)
    
    t2 = """
         CFA Level 2
         Chartered Financial Analyst Institute | June 2024
         Advanced knowledge of investment analysis and portfolio management, with a focus on asset valuation and financial reporting
         """.strip("\n").splitlines()
    t2[1] = '<span style="font-weight: bold;">'+t2[1].replace(" | ", "</span> | ")
    mycompoent.element1(f"➥ {t2[0]}", "<br>".join(t2[1:]))
    
    t2 = """
         Financial Risk Manager (FRM)
         Global Association of Risk Professionals | January 2024
         Validated expertise in risk management principles and practices, including market, credit, and operational risk
         """.strip("\n").splitlines()
    t2[1] = '<span style="font-weight: bold;">'+t2[1].replace(" | ", "</span> | ")
    mycompoent.element1(f"➥ {t2[0]}", "<br>".join(t2[1:]))
    
    t2 = """
         Google Analytics Individual Qualification
         Google | November 2023
         Demonstrated expertise in using Google Analytics to track and analyze website performance, user behavior, and marketing effectiveness
         """.strip("\n").splitlines()
    t2[1] = '<span style="font-weight: bold;">'+t2[1].replace(" | ", "</span> | ")
    mycompoent.element1(f"➥ {t2[0]}", "<br>".join(t2[1:]))
    
    
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Academic Projects <-
    </div>''', unsafe_allow_html=True)
    
    t2 = """
         Integrated Marketing Communications Strategy Development
         ✎ Led a team to create a comprehensive IMC strategy for a local startup
         ✎ Conducted market research to identify target demographics and key messaging
         ✎ Developed a multi-channel campaign that integrated social media, email marketing, and traditional advertising, resulting in a 30% increase in brand awareness within three months
         """.strip("\n").splitlines()
    mycompoent.element1(f"➥ {t2[0]}", "<br>".join(t2[1:]))
    
    t2 = """
         Market Basket Analysis Using Association Rules
         ✎ Developed an analytical model to identify product associations in transaction data
         ✎ Utilized the Apriori algorithm to uncover buying patterns
         ✎ Improved cross-selling strategies, resulting in a 15% increase in average transaction value
         """.strip("\n").splitlines()
    mycompoent.element1(f"➥ {t2[0]}", "<br>".join(t2[1:]))