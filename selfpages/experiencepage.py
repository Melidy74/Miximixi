import streamlit as st
from compoents import mycompoent, interactive

def main():
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Professional Experience <-
    </div>''', unsafe_allow_html=True)
    
    t0 = """
    Marketing Analyst Intern
    ByteDance | June 2024 - August 2024
    Conducted market research to analyze consumer trends and preferences, utilizing tools such as SPSS and Google Analytics
    Developed and implemented marketing strategies that increased customer engagement by 25%
    Presented findings and recommendations to senior management, contributing to strategic decision-making
    """.strip("\n").splitlines()
    
    t0[1] = '<span style="font-weight: bold;">'+t0[1].replace(" | ", "</span> | ")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    
    t0 = """
    Research Assistant
    University of CUHK(SZ), Department of Marketing | January 2024 - May 2024
    Assisted in conducting research on consumer behavior and marketing effectiveness
    Analyzed survey data and presented findings to faculty and students, enhancing curriculum development
    Contributed to a published paper on digital marketing trends and their impact on consumer decision-making
    Mentored undergraduate students on research methodologies and programming
    """.strip("\n").splitlines()
    
    t0[1] = '<span style="font-weight: bold;">'+t0[1].replace(" | ", "</span> | ")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    
    t0 = """
    M&A Analyst Intern
    Tencent Holdings Ltd. | May 2023 - August 2023
    Assisted in the evaluation of potential acquisition targets by conducting comprehensive market research and financial analysis
    Collaborated with cross-functional teams to assess strategic fit, synergies, and risks associated with prospective deals
    IDeveloped detailed financial models to forecast revenue growth and profitability for acquired companies, contributing to investment recommendations
    Participated in due diligence processes, analyzing financial statements, market conditions, and competitive landscapes
    """.strip("\n").splitlines()
    
    t0[1] = '<span style="font-weight: bold;">'+t0[1].replace(" | ", "</span> | ")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Projects <-
    </div>''', unsafe_allow_html=True)
    
    t0 = """
    Marketing Attribution Modeling
    Description: Developed a machine learning model to analyze the effectiveness of various marketing channels in driving conversions
    Skills Used: Python, R, Scikit-learn, A/B testing
    Outcome: Improved marketing ROI by 20% by identifying high-performing channels and optimizing budget allocation
    """.strip("\n").splitlines()
    
    for i in t0[1:]:
        t0[t0.index(i)] = '<span style="font-weight: bold;">'+t0[t0.index(i)].replace(":", "</span>:")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    
    t0 = """
    Sentiment Analysis for Brand Monitoring
    Description:  Implemented a sentiment analysis tool to evaluate customer feedback on social media and review platforms
    Skills Used: Python, NLTK, BERT, Data Visualization (Tableau)
    Outcome: Enhanced brand reputation management by providing real-time insights and reducing negative sentiment by 30%
    """.strip("\n").splitlines()
    
    for i in t0[1:]:
        t0[t0.index(i)] = '<span style="font-weight: bold;">'+t0[t0.index(i)].replace(":", "</span>:")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    
    t0 = """
    Churn Prediction Modeling
    Description: Created a predictive model to identify customers at risk of churning, using historical customer data and machine learning algorithms
    Skills Used: Python, Pandas, TensorFlow, Logistic Regression
    Outcome: Reduced churn rate by 15% through targeted retention strategies based on model insights
    """.strip("\n").splitlines()
    
    for i in t0[1:]:
        t0[t0.index(i)] = '<span style="font-weight: bold;">'+t0[t0.index(i)].replace(":", "</span>:")
    
    mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]))
    st.write(" ")
    
    with st.expander("Interactive Data Visualization Demo", True):
        st.info("**Description:** An interactive demonstration of various data visualization techniques.")
        interactive.display_interactive_chart()
    
    st.markdown('''
    <br><div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    -> Professional Skills <-
    </div>''', unsafe_allow_html=True)
    
    col = st.columns(2, border=True)
    
    with col[0]:
        t0 = """
        Technical Skills
        Marketing Analytics Tools: Google Analytics, HubSpot, Salesforce
        Data Analysis: SQL, Excel, R, Python
        Digital Marketing: SEO, SEM, Social Media Advertising, Email Marketing
        Visualization: Matplotlib, Seaborn, Tableau, PowerBI
        CRM Software: Salesforce, Zoho CRM
        A/B Testing Tools: Optimizely, VWO
        """.strip("\n").splitlines()
    
        for i in t0[1:]:
            t0[t0.index(i)] = '<span style="font-weight: bold;">'+t0[t0.index(i)].replace(":", "</span>:")
    
        mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]), color="transparent")
    
    with col[1]:
        t0 = """
        Soft Skills
        Communication: Exceptional verbal and written communication skills
        Leadership: Proven ability to lead cross-functional teams and drive strategic initiatives
        Problem-solving: Strong analytical and critical thinking abilities
        Time Management: Efficient at prioritizing tasks and meeting deadlines
        Strategic Thinking: Strong analytical and critical thinking skills for data-driven decision-making
        Adaptability: Quick learner who thrives in dynamic environments
        """.strip("\n").splitlines()
    
        for i in t0[1:]:
            t0[t0.index(i)] = '<span style="font-weight: bold;">'+t0[t0.index(i)].replace(":", "</span>:")
    
        mycompoent.element1(f"➥ {t0[0]}", "<br>".join(t0[1:]), color="transparent")