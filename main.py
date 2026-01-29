# import streamlit as st
# import mysql.connector
# import login
# import register
# import dashboard
# from dotenv import load_dotenv
# import os
# load_dotenv()
# conn= mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=os.getenv("pass"),
#     database=os.getenv("data")
# )

# # Use session state to track login
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False

# if st.session_state['logged_in']:
#     dashboard.dashboard()
# else:
#     st.sidebar.title("Navigation")
#     options = ["Home", "Login", "Register"]
#     selection = st.sidebar.radio(" ", options)
#     if selection == "Home":
#         st.title("Welcome to the Home Page")
#         st.write("This is the home page of the Streamlit application.")
#         st.markdown(
#             """
#             <style>
#             .main {
#             background-color: #f0f2f6;
#             }
#             .stButton>button {
#             color: white;
#             background: #ff4b4b;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
#         st.info("Use the sidebar to Login or Register.")
        
#     if selection == "Login":
#         if login.login(conn) == True:
#             st.session_state['logged_in'] = True
#             st.rerun()
#     if selection == "Register":
#         register.register(conn)
st.write("welcome to streamlit")
import streamlit as st
st.header("Kranthi") #header

st.title("Student management system") #title

st.subheader("Welcome to the student management system of Anurag University") #subheader

st.markdown("----------------------")

st.text("This is a simple student management system built using Streamlit.") #text

st.write("You can use this system to manage student records, view student details, and perform various operations related to student management.") #write

st.write({"Features": ["Add Student", "View Students", "Update Student", "Delete Student"]}) #write with dictionary

st.write(["Easy to use", "Fast", "Reliable"]) #write with list

st.markdown("### Get Started")

st.markdown("**Bold**") #markdown

st.markdown("*italic text*") #markdown italic

st.markdown("1. Kranthi \n2. Anurag \n3. Sai") #markdown with numbered list

st.markdown("- sherlin\n- shusu\n- sheru") #markdown with bullet list

st.markdown("----------------------")

st.markdown("<h3 style='color:blue'>Contact Us</h3>", unsafe_allow_html=True) #html in markdown

st.write("----------------")

#to display code snippet
st.code(
    """ 
def add_student(a,b):
    return a + b 
    """ ,language='python'
)

#to display mathematical equation
st.latex(r""" e=mc^2 """   )

#visual horizontal line
st.divider()

#button'
if st.button("Click Me"):
    st.balloons()
    st.success("Button Clicked!")
else:
    st.info("Click the button to see the magic!")
if st.button("snow"):
    st.snow()

#text input method
name = st.text_input("Enter your name:")
if name=="":
    st.warning("Please enter your name.")
elif name.isnumeric():
    st.error("Name should only contain alphabets.")
else:
    st.success(f"Hello, {name}! Welcome to Anurag University.")

a=st.text_area("Enter your address:")
st.write("Your address is:",a)

st.checkbox("I agree to the terms and conditions.")

st.radio("select your gender:",("Male", "Female", "Other"))

st.selectbox("Select your course:",["CSE","ECE","IT","MECH","CIVIL"])

st.multiselect("Select your hobbies:",["Reading","Traveling","Gaming","Cooking","Sports"])

st.slider("Select your age:",0,100,25)

st.date_input("Select your date of birth:")

st.file_uploader("Upload your profile picture:",type=["jpg","png","jpeg"])


#form example
with st.form("student_form"):
    name=st.text_input("Enter your name:")
    age=st.number_input("Enter your age:",0,100)
    submit= st.form_submit_button("Submit")

if submit:
    st.write(name,age)
st.divider()
#login form example
with st.form("login_form"):
    username=st.text_input("Username:")
    password=st.text_input("Password:",type="password")
    login=st.form_submit_button("Login")
if login:
    st.success("successfully logged in!")

st.divider()
#columns method
col1,col2,col3=st.columns(3)
with col1:
    st.header("Column 1")
    st.text("This is column 1")
with col2:
    st.header("Column 2")
    st.text("This is column 2") 
with col3:
    st.header("Column 3")
    st.text("This is column 3")

st.divider()
#container method
container=st.container()
container.write("This is inside the container")
container.button("Click Me Too")

st.divider()

#table
data={
    "Name":["Kranthi","Anurag","Sherlin"],
    "Age":[21,22,20],
    "Course":["CSE","ECE","IT"]
}
st.table(data)

#sidebar method
st.sidebar.header("Menu")
option=st.sidebar.radio("Select an option:",["Home","Add Student","View Students","Update Student","Delete Student"])

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxnJCMYGY8Go8yoBJS7tbcMh6wohX2gN68uQ&s",width=300)

@st.cache_data
def load_data():
    return [1,2,3,4,5]
data=load_data()
st.write("Cached data:",data)
