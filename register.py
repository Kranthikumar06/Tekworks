import streamlit as st
import mysql.connector
def register(conn):
    cursor = conn.cursor()
    with st.form("registration_form"):
        st.header("User Registration")
        username=st.text_input("Username")
        email=st.text_input("Email")
        password=st.text_input("Password", type="password")
        confirm_password=st.text_input("Confirm Password", type="password")
        submit_button=st.form_submit_button("Register",width=300)
        clear_on_submit=True
        try:
            if submit_button:
                if password == confirm_password:
                    cursor.execute("INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
                    conn.commit()
                    st.success("User registered successfully!")
                else:
                    st.error("Passwords do not match. Please try again.")
        except:
            st.error("username or email already exists. Please try again with different credentials.")
    return cursor