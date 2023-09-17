import streamlit as st


# Create an empty dictionary to store user registration data
user_data = {}

# Streamlit UI


def main():
    st.title("Registration Page")
    # Use st.form to create a registration form
    with st.form("registration_form"):
        st.write("Please fill out the registration form:")
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        confirm_password = st.text_input("Confirm Password:", type="password")

        if password != confirm_password:
            st.error("Passwords do not match.")

        submit_button = st.form_submit_button("Register")

    # Process registration data when the form is submitted
    if submit_button:
        if username and password and password == confirm_password:
            # Store user registration data (insecure for demonstration purposes)
            user_data['username'] = username
            user_data['password'] = password
            st.success("Registration successful!")

            # In a real application, you would typically store the data in a database.

        else:
            st.error("Please fill out all fields and ensure the passwords match.")