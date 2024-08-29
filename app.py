import streamlit as st
from PIL import Image

# Streamlit app title
st.title("Patient Admissions Predictive Analysis")

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Introduction", "Trends Over Time", "Diagnosis Distribution", "Discharge Status", "Recommendations", "Reflection"])

# Introduction section
if options == "Introduction":
    st.header("Introduction")
    st.write("""
    This application provides insights into patient admissions data, helping healthcare organizations optimize resources and improve patient care. 
    Explore the trends, distributions, and recommendations derived from the data.
    """)

# Trends Over Time section
elif options == "Trends Over Time":
    st.header("Patient Admissions Over Time")
    st.write("""
    The image below shows the trends in patient admissions over time, helping to identify periods of high and low patient inflow.
    """)
    image_trends = Image.open("D://Abhinav//Test//DiagViz//images//line2.png")
    st.image(image_trends, caption='Patient Admissions Over Time')
    image_trends2 = Image.open("D://Abhinav//Test//DiagViz//images//line.png")
    st.image(image_trends2, caption='Diagnosis Trends over time')

# Diagnosis Distribution section
elif options == "Diagnosis Distribution":
    st.header("Distribution of Diagnoses")
    st.write("""
    The image below displays the distribution of different diagnoses, highlighting the most common conditions leading to patient admissions.
    """)
    image_diagnosis1 = Image.open("D://Abhinav//Test//DiagViz//images//pie.png")
    st.image(image_diagnosis1, caption='Diagnosis Distribution')
    image_diagnosis2 = Image.open("D://Abhinav//Test//DiagViz//images//bar.png")
    st.image(image_diagnosis2, caption='Gender Distribution of Diagnoses - Image 1')
    image_diagnosis3 = Image.open("D://Abhinav//Test//DiagViz//images//marker.png")
    st.image(image_diagnosis3, caption='Age Distribution of Diagnoses - Image 2')

# Discharge Status section
elif options == "Discharge Status":
    st.header("Discharge Status")
    st.write("""
    The images below display the distribution of discharge statuses and mortality rates.
    """)
    image_discharge = Image.open("D://Abhinav//Test//DiagViz//images//discharge.png")
    st.image(image_discharge, caption='Discharge Distribution')
    image_mortality = Image.open("D://Abhinav//Test//DiagViz//images//mortality1.png")
    st.image(image_mortality, caption='Mortality Distribution')

# Recommendations section
elif options == "Recommendations":
    st.header("Recommendations")
    st.write("""
    Based on the analysis, the following recommendations are made to optimize healthcare operations:
    
    - **Resource Allocation**: Increase staff during peak admission periods.
    - **Preventive Measures**: Implement targeted interventions for high-risk diagnoses.
    - Increase resources for common diagnoses (Feasibility: High, Practicality: High).
    - Implement gender-sensitive treatment options (Feasibility: Medium to High, Practicality: High).
    - Allocate resources for conditions requiring longer stays (e.g., Schizophrenia) and critical care for PTSD (Feasibility: Medium to High, Practicality: High).
    """)

# Reflection section
elif options == "Reflection":
    st.header("Reflection")
    st.write("""
    During the analysis, challenges such as ensuring synthetic data accurately reflects real-world scenarios were encountered. The insights from this analysis can inform future decisions, improving overall hospital management.
    """)
