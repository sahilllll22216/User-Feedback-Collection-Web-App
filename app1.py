import streamlit as st
import pandas as pd

def FeedbackHub(Name, Phone, Email,Review):
    df = pd.read_csv("Feedbacks.csv", encoding="utf-8")
    new_data = {"Name": [Name], "Phone": [Phone], "Email": [Email],"Review":[Review]}
    df = df._append(pd.DataFrame(new_data), ignore_index=True)
    df.to_csv("Feedbacks.csv", encoding="utf-8", index=False)


def main():
    st.title("User Entry Form")

    Name = st.text_input("Name:")
    Phone = st.text_input("Phone:")
    Email = st.text_input("Email:")
    Review = st.text_input("Review:")

    if st.button("Submit"):
        if Name and Phone and Email and Review:
            FeedbackHub(Name, Phone, Email,Review)
            st.success("Entry submitted successfully!")
        else:
            st.warning("Please fill in all the fields correctly.")

if __name__ == "__main__":
    main()

