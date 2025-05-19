import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Sia_WU_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Sia WU")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** wusiyecuhk@163.com
    - **Phone:** 59575126
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly skilled marketer with over 5 years of experience in digital marketing. 
    """)

    st.header("Internship Experience")
    st.markdown("""
    **Consultant, L'Oréal.**
    - *Dec 2024 - Mar 2025*
    - TOP 200 Nationwide
    - Precision Breakthrough: Identified the core pain point of 73% of male users - oil control needs, and proposed the "All in Oil
      Control" product strategy. Through over 2,000 questionnaires, it was found that 86% of men with oily skin were willing to pay a
      30% premium for professional oil-control products.
    - Activity Design: Led the design of a replaceable essence tube membership system, innovatively integrating the mechanism of "7
      tubes for 1 nursing service + free skin testing", which was in line with ESG concepts and promoted footfall in offline stores.
    - Business Results: The plan was adopted by L'Oréal China's innovation team and won the top 200 in L'Oréal's 2025 Mainland China
      Business Competition.

    **IMC, InTime Commercial Co., Ltd.**
    - *May 2023 - Aug 2023*
    - Omnichannel Marketing Campaign: Planned and executed the 618 Shopping Festival. Collaborated with over 80 brands to launch
      "best - seller combos" and engaged Xiaohongshu influencers for promotion. Through short - video and live - stream marketing,
      achieved over 100,000 exposures, grew the follower base by over 6,000, and optimized the SKU mix via data analysis, resulting in
      an 8% increase in conversion rate.
    - Event Management: Led the "Tom and Jerry" pop - up store project. Designed interactive elements to attract young consumers,
      partnered with over 30 clothing brands, and achieved IP - peripheral sales of 80,000 yuan and clothing sales of 50,000 yuan. The
      optimized interactive layout extended the average customer stay time by 23%.
    - Social Media Content Strategy: Conceptualized and executed hot - topic campaigns like "Summer Cooling", integrated multi -
      brand resources, and managed full - funnel content distribution on social media, with an average article readership of over 5,000.
    - Cross - functional Coordination: Coordinated PR and SP content for various merchant brands, designed event - themed
      promotional materials, and collaborated with operations and engineering teams. Conducted on - site competitor analysis to enhance
      store traffic.
    """)

    st.header("Education")
    st.markdown("""
    **Bachelor of Marketing**
    - University of CUHK
    - *Graduated: June 2025*
    - GPA: 3.7/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
    """)

    st.header("Certifications")
    st.markdown("""
    - Dean's List
    """)

 

    st.header("Languages")
    st.markdown("""
    - **English:** Toefl 106
    - **Chinese:** Native
    """)

    st.header("Interests")
    st.markdown("""
    - Marketing Analytics
    - Digital Trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 