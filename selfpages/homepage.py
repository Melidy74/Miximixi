import streamlit as st
from compoents import mycompoent

def main():
    t0 = """
         Recent Master's Graduate in Marketing
         Chinese University of Hong Kong
         12 Chak Cheung St., Ma Liu Shui, HKSAR
         1155216514@link.cuhk.edu.hk
         1155216514@link.cuhk.edu.hk
    """.strip("\n").splitlines()
    
    col = st.columns([2, 1], border=True)
    col[0].markdown(f'''
    <div style="text-align: center; padding: 12px; border-radius: 6px; height: 200px; font-size: 22px;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%;">
        <span style="font-weight: bold;">{t0[0]}</span><br>
        {t0[1]}<br>
        {t0[2]}<br>
        <a src="{t0[4]}">{t0[3]}</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    col[1].image("statics/image.png")
    
    t1 = """
         ✎ I am a recent graduate in Marketing from Chinese University of Hong Kong, where I developed a strong foundation in digital marketing and consumer behavior. My academic journey fueled my passion for leveraging data to drive effective marketing strategies.
         ✎ During my studies, I successfully completed several hands-on projects that involved real-world applications of marketing principles. These projects sharpened my skills in market research, campaign development, and performance analysis. I gained proficiency in various marketing tools, including Google Analytics and HubSpot, which equipped me with the ability to analyze data effectively and measure campaign success.
         ✎ As I embark on my professional journey, I am enthusiastic about the opportunity to contribute to a dynamic marketing team. I am a proactive learner and a collaborative team player, eager to apply my skills in a professional environment. I am committed to continuous growth and development in the marketing field, and I look forward to making a meaningful impact in the industry.
         """
    mycompoent.element1("➥ About Me", "<br>".join(t1.strip("\n").splitlines()))
    
    t2 = """
         ✎ Programming Languages: Python, R
         ✎ Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
         ✎ Machine Learning: Scikit-learn, TensorFlow, Keras
         ✎ Database: SQL, MongoDB
         ✎ Data Visualization: Tableau, Power BI
         ✎ Statistical Analysis: Hypothesis Testing, Regression Analysis
         ✎ Soft Skills: Communication, Teamwork, Problem-Solving, Time Management
         """
    mycompoent.element1("➥ Skills", "<br>".join(t2.strip("\n").splitlines()))
    
    st.markdown('''
    <style>
        [data-testid="stColumn"] {
            background: rgba(0,0,0,0.05);
        }
    </style>
    ''', unsafe_allow_html=True)