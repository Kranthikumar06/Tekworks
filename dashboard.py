import streamlit as st
def dashboard():
    st.title("Dashboard")
    st.write("Welcome to the Dashboard! You have successfully logged in.")  
    st.write("Here you can access various features of the application.")

    st.button("Logout", on_click=logout)
def logout():
    st.session_state['logged_in'] = False
    