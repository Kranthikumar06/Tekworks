import streamlit as st
import mysql.connector

def login(conn):
    cursor = conn.cursor()
    login_success = False
    with st.form("login_form"):
        st.header("User Login")
        username=st.text_input("Username")
        password=st.text_input("Password", type="password")
        login_button=st.form_submit_button("Login")
        try:
            if login_button:
                cursor.execute("SELECT * FROM Users WHERE username=%s AND password=%s", (username, password))
                result = cursor.fetchone()
                if result:
                    st.success("Successfully logged in!")
                    login_success = True
                else:
                    st.error("Invalid username or password. Please try again.")
        except:
            st.error("An error occurred during login. Please try again later.")
    return login_success