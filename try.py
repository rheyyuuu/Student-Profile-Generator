import streamlit as st

st.title("Student Profile Generator")

st.header("Enter Student Information")

# TEXT INPUT
name = st.text_input("Full Name")

# NUMBER INPUT
age = st.number_input("Age", 10, 60)

# SELECT BOX
course = st.selectbox(
    "Course",
    ["BSIT", "BSCS", "BSIS", "BSEMC", "BSN" "other"]
)

# RADIO BUTTON
gender = st.radio(
    "Gender",
    ["Male", "Female", "Other"]
)

# MULTISELECT
skills = st.multiselect(
    "Skills",
    ["Python", "Networking", "Database", "UI Design" "other"]
)

# TEXT INPUT
hobbies = st.text_input("hobbies")

# SLIDER
year = st.slider("Year Level", 1, 4)

# TEXT AREA
bio = st.text_area("Short Bio")

# FILE UPLOADER
photo = st.file_uploader("Upload Profile Photo")

# BUTTON
generate = st.button("Generate Profile")

# OUTPUT
if generate:

    st.success("Profile Generated!")

    if photo:
        st.image(photo, width=200)

    st.write("### Student Profile")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
    st.write("Gender:", gender)
    st.write("Skills:", skills)
    st.write("Hobbies:", hobbies)
    st.write("Year Level:", year)
    st.write("Bio:", bio)