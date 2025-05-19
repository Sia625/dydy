import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>WU SIYE</h4>
        <p>Master of Marketing<br>
        The Chinese University of HongKong<br>
        <a href="mailto:wusiyecuhk@163.com">wusiyecuhk@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "签证照--精修版.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a Marketing Master's student at The Chinese University of Hong Kong, specializing in Big Data Marketing and Consumer Analytics. During my academic journey, I have built a solid foundation in Market Research, Big Data Strategy, Digital Marketing, and Social Media Analysis.

        My professional experience includes working with L'Oréal China, where I developed an innovative product strategy through extensive market research and data analysis. At InTime Commercial Co., Ltd., I led omnichannel marketing campaigns that significantly improved user conversion rates and customer retention. I also contributed to developing an AI virtual makeup try-on system during my internship at Alibaba's Asia-Pacific headquarters.

        I excel in leveraging data analytics for market insights and transforming analytical findings into actionable business strategies. With a proven track record in cross-functional collaboration and project management, I am passionate about innovation and ready to tackle new challenges in the dynamic field of marketing analytics.
        """
    )

    st.markdown(
        """
        ### Skills
        - Data Analytics: Excel (VLOOKUP, PivotTable), SPSS, Adobe Analytics
        - Marketing Tools: Canva, Photoshop, Social Media Platforms
        - Market Research: Survey Design, Data Collection, Consumer Insights
        - Project Management: Event Planning, Cross-functional Coordination
        - Business Analysis: Market Research, Competitive Analysis, Data Visualization
        - Language: Chinese (Native), English (TOEFL 106)
        - Professional Skills: Omnichannel Marketing, Content Marketing, Digital Strategy
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page