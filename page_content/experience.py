import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### L'Oréal
    **Consultant** | *Dec 2024 - Mar 2025*
    
    - TOP 200 Nationwide
    - Precision Breakthrough: Identified the core pain point of 73% of male users - oil control needs, and proposed the "All in Oil
      Control" product strategy. Through over 2,000 questionnaires, it was found that 86% of men with oily skin were willing to pay a
      30% premium for professional oil-control products.
    - Activity Design: Led the design of a replaceable essence tube membership system, innovatively integrating the mechanism of "7
      tubes for 1 nursing service + free skin testing", which was in line with ESG concepts and promoted footfall in offline stores.
    - Business Results: The plan was adopted by L'Oréal China's innovation team and won the top 200 in L'Oréal's 2025 Mainland China
      Business Competition.
    """)
    
    st.markdown("""
    ### InTime Commercial Co., Ltd.
    **Integrated Marketing Department Intern** | *May 2023 - Aug 2023*
    
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
    
    st.markdown("""
    ### China Post Group Corporation
    **Marketing** | *Dec 2022 - Feb 2023*
    
    - Cross - industry Collaboration: Forged a strategic partnership with China National Petroleum Corporation for cross - marketing,
      achieving a pension - policy exposure of over 50,000 views and acquiring over 500 new postal - card users. Led the monetization of
      offline financial - lecture traffic, designing a user journey that achieved a 35% on - site conversion rate.
    - Customer Relationship Enhancement: Conducted a survey of over 200 customers to understand their financial - management
      needs, developed tailored solutions, and proactively engaged with VIP customers and key institutions to promote China Post's
      personal - pension services, achieving a 98% customer - satisfaction rate.
    """)
    
    st.markdown("---")
    
    
    
   
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - Data Analytics: Excel (VLOOKUP, PivotTable), SPSS, Adobe Analytics
        - Marketing Tools: Canva, Photoshop, Social Media Platforms
        - Market Research: Survey Design, Data Collection, Consumer Insights
        - Project Management: Event Planning, Cross-functional Coordination
        - Business Analysis: Market Research, Competitive Analysis, Data Visualization
        - Language: Chinese (Native), English (TOEFL 106)
        - Professional Skills: Omnichannel Marketing, Content Marketing, Digital Strategy
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---")