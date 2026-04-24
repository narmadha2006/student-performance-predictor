import streamlit as st
import pickle
import numpy as np
import pandas as pd


model = pickle.load(open("model.pkl", "rb"))


def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

st.title("🎓 Student Performance Predictor")


student_name = st.text_input("Enter Student Name")


attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=75)
study_hours = st.number_input("Study Hours per Day", min_value=0, max_value=10, value=3)
internal_marks = st.number_input("Internal Marks", min_value=0, max_value=100, value=60)
assignments = st.number_input("Assignment Score", min_value=0, max_value=100, value=70)

if st.button("Predict"):

    # Check name
    if student_name.strip() == "":
        st.error("Please enter student name")
    else:
        input_data = np.array([[attendance, study_hours, internal_marks, assignments]])
        prediction = model.predict(input_data)

        predicted_marks = prediction[0]
        grade = get_grade(predicted_marks)

        st.success(f"Student: {student_name}")
        st.success(f"Predicted Marks: {predicted_marks:.2f}")
        st.info(f"Grade: {grade}")

        # Save report
        new_data = {
            "Student Name": student_name,
            "Attendance": attendance,
            "Study Hours": study_hours,
            "Internal Marks": internal_marks,
            "Assignments": assignments,
            "Predicted Marks": predicted_marks,
            "Grade": grade
        }

        df = pd.DataFrame([new_data])

        try:
            old = pd.read_csv("reports.csv")
            df = pd.concat([old, df], ignore_index=True)
        except:
            pass

        df.to_csv("reports.csv", index=False)

        st.success("Report saved successfully!")

        #  Show saved data
        st.subheader("📊 Saved Reports")
        st.dataframe(df)