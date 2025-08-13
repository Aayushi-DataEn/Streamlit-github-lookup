import streamlit as st
st.image("intellipaat.jpeg")
import time as t

st.set_page_config(page_title = "Intellipaat Lookup")

 
# title = It is used to add the titile for the web app
st.title("Welcome to Intellipaat")

# header
st.header("Machine Learning")

# sub header
st.subheader ("Linear Regression")

# To give information
st.info("Information details of a user")

# warning message
st.warning("Come on time or else you will be marked absent")

# Error message
st.error("Wrong Password")

# success message
st.success("Congrats! You have got A-grade")

# Write function (to write text along with any code)
st.write("Employee name")
st.write(range(50))

# Markdown
st.markdown("# Intellipaat")
st.markdown("## Intellipaat")
st.markdown("### Intellipaat")
st.markdown(":smiley:")

st.text("Intelipaat learners")

# Caption
st.caption("Caption is here")

# Latex func= to diplay mathemtical operations/equation
st.latex(r''' a+b x^2+c''')

# Widgets

# checkbox
st.checkbox("Login")

# button
st.button("click")

# radio = display a radio button
st.radio("Pick your gender", ["Male", "Female", "Other"])

# select box (Only one)
st.selectbox("Pick your course", ["ML","Cloud", "Cyber Security"])

# multi select
st.multiselect("Choose the Department", ["Content", "Sales", "Accounts", "Marketing"])

# select sliders
st.select_slider("Rating", ["Bad", "Average", "Good", "Excellent", "Outstanding"])

# slider
st.slider("Enter your number", 0,30)

# number_input
st.number_input("Pick a number", 0,100)

# text_input
st.text_input("Enter your email address")

# date_input
st.date_input("Date of Birth")

st.time_input("Hey what's the timing")

# text_area = to print a text in more than one line , Description
st.text_area("Welcome to the Intellipaat Website. Hello Learners ")

# file_uploader = to uplaod a file
st.file_uploader("Upload your document")

st.color_picker("Color")

# progress
st.progress(90)

# spinner = display a temporary waiting message during execution
with st.spinner("Just wait:"):
    t.sleep(2)

# balloon = to display balloons for celebration
st.balloons()

# sidebar = to pinned the element to the left side
st.sidebar.title("Intellipaat")
st.sidebar.text_input("Enter your Email")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert",["Student", "Working"])

# Data Visualisation
import pandas as pd
import numpy as np
st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50,2), columns=["x", "y"])
st.bar_chart(data)

st.title("Line Chart")
st.line_chart(data)

st.title("Area Chart")
st.area_chart(data)



