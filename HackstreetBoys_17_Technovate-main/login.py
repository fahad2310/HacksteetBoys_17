import streamlit as st

def main():
# Define a dictionary to store user credentials (insecure for demonstration purposes)
# In practice, you should use a secure authentication system.
    user_credentials = {
        'username': 'user',
        'password': 'password123'
    }

    # Define a function to check user credentials
    def check_credentials(username, password):
        if username == user_credentials['username'] and password == user_credentials['password']:
            return True
        else:
            return False


    # Streamlit UI
    st.title("Login Page")

    # Use st.session_state to manage user sessions
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

        if st.button("Login"):
            if check_credentials(username, password):
                st.session_state.authenticated = True
                st.success("Logged in successfully!")
            else:
                st.error("Incorrect username or password. Please try again.")
    else:
        st.title("Welcome to the Dashboard")
        st.write("You are logged in!")

        # Add your dashboard content here
        st.write("This is your dashboard content.")

        if st.button("Logout"):
            st.session_state.authenticated = False
            st.success("Logged out successfully!")