import streamlit as st
import mysql.connector
import login
import register
import dashboard

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="S&Kranthi@0626",
    database='registration_db'
)

# Use session state to track login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    dashboard.dashboard()
else:
    st.sidebar.title("Navigation")
    options = ["Home", "Login", "Register"]
    selection = st.sidebar.radio(" ", options)
    if selection == "Home":
        st.title("Welcome to the Home Page")
        st.write("This is the home page of the Streamlit application.")
    if selection == "Login":
        if login.login(conn) == True:
            st.session_state['logged_in'] = True
            st.rerun()
    if selection == "Register":
        register.register(conn)