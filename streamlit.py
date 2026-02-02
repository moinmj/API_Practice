import streamlit as st
import time as t
#ALL THE FUNCTIONS
st.image("zoro.jpg")
#title - It is used to add the title of an app
st.title("welcome to streamlit")
#Header
st.header("Machine Learning")
#sub header
st.subheader("Linear regression")
#To give information
st.info("Information details for a user")
#warning message
st.warning("Come on time or else you will be marked absent")
#error message
st.error('Wrong passsword')
#write
st.write("Employee name")
st.write(range(0,50))
#markdown
st.markdown("# streamlit")
st.markdown("## streamlit")
st.markdown("### streamlit")
st.markdown(":moon:")
#text
st.text("Streamlit learning")
# To write a caption
st.caption("Caption is here")
#To display a mathematical equation
st.latex(r''' a+b x^2+c''')

#ALL THE WIDGETS

#checkbox
st.checkbox("login")
#button
st.button("click")
#radio widget
st.radio("Pick your gender",["Male","Female","other"])
#select box
st.selectbox("Pick your course",["ML","cloud","Cyber security"])
#multiselect
st.multiselect("choose the dept",["content","sales","marketting"])
#selectslider
st.select_slider("rating",["bad","good","excellent","outstanding"])
#slider
st.slider("Enter your number",0,100)
#number_input
st.number_input("pick a number",0,100)
#text input
st.text_input("Enter your email address")
#date input
st.date_input("opening ceremony")
#time input
st.time_input("hey what's the time")
#text area-For writing a discription
st.text_area("Welcome to streamlit website")
#File uploader
st.file_uploader("upload your file/folder")
#color
st.color_picker("color")
#progress
st.progress(90)
#spinner
with st.spinner("just wait"):
    t.sleep(1)
#ballons
st.balloons()
#side bar
st.sidebar.title("welcome to streamlit")
st.sidebar.text_input("mail_address")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.radio("Professional Expert",["Student","Working","Others"])
#DATA VISUALIZATION
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)

 
