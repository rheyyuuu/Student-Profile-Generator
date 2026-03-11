import streamlit as st

# Page Configuration
st.set_page_config(page_title="About - Student Profile Generator", page_icon="📝")

st.title("ℹ️ About This App")
st.divider()

# 1. Use-Case: What the app does
st.header("1. Purpose of the App")
st.write("""
The student Profile Generator is a simple web app that helps users create a student profile. It collects basic
information about a student and automatically shows the profile in a clean and organized format on the 
screen.The app make it easier to organize and display student information.
""")

# 2. Target User
st.header("2. Target Users")
st.info("""
The target users of this application are students who want to create their own student profile, as well 
as teachers or school staff who need a quick and easy way to view or generate student information.
""")

# 3. What inputs does the app collect, and what output does it shows 
st.header("2. What inputs does the app collect, and what output does it shows")
st.info("""
The application collects student informations such as name, age, gender , course, skill, hobbies,
and other personal or academic details.After the user submits the information, the app generates
 and displays the complete student profile in a clear and organized format.
""")

# 4. Inputs & Outputs
st.header("3. Data Processing")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Inputs Collected")
    st.markdown("""
    - **Personal:** Name, Age, Gender, Short Bio, hobbies.
    - **Academic:** Course (Major), Year Level.
    - **Technical:** A multi-select list of specialized skills.
    """)

with col2:
    st.subheader("Expected Output")
    st.markdown("""
    - A **formatted summary dashboard** that organizes all inputs into a visual profile.
    - Real-time updates as information is entered.
    """)

st.divider()
st.caption("Developed by Rheymar | Built with Streamlit & Python")