# Basic of Streamlit App - Student Info App

import streamlit as st

# st.title("🎓 Student Info App")
st.set_page_config(page_title="Student Info App", page_icon="🎓", layout="centered")

st.header("Enter Your Information")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=150)
city = st.text_input("Enter your city")
email = st.text_input("Enter your email")
course = st.selectbox("Select your course", ["B.Tech", "Arch", "M.tech", "MBA", "PhD"])
branch = st.radio("Select your branch", ["AI","CSE", "ECE", "ME", "CE", "EE"])
year = st.radio("Select your year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
rating = st.slider("Rate your experience at our college", 0, 10)
terms = st.checkbox("I confirm the information is correct")

if st.button("Submit"):
    if terms:
        st.success("Details submitted successfully!")
        st.write("### Your Information:")
        st.write(f"**Name:**", name) # Method 1 ✅
        st.write(f"**Age:**", age)  
        st.write("**City**", city)
        st.write(f"**Email:** {email}") # Method 2 
        st.write(f"**Course:** {course}")
        st.write(f"**Branch:** {branch}")
        st.write(f"**Year:** {year}")
        st.write(f"**Rating:** {rating}")
    else:
        st.warning("Please confirm the information first")