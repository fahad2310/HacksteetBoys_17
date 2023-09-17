# import streamlit as st
# from PIL import Image

# st.set_page_config(
#     page_title="Multipage App",
#     page_icon="👋",
# )

# page_bg_img = '''
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
# background-size: 180%;
# background-position: top left;
# background-repeat: no-repeat;
# background-attachment: local;
# }}

# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}

# [data-testid="stToolbar"] {{
# right: 2rem;
# }}
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

# st.title("Main Page")
# # st.sidebar.success("Select a page above.")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# st.image=Image.open("space.jpg")
# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)


import streamlit as st
from PIL import Image
# import login
# import signup
st.set_page_config(
    page_title="SimpliLegal",
    page_icon="🧑‍⚖️",
)


st.title("Home")
st.write("Welcome to SimpliLegal – Your Legal Companion. Navigate the complexities of the legal world effortlessly with our intuitive platform. From document analysis to expert consultations, we simplify law for you")

# Add your logo/image file path or URL here
logo_url = "logo.png"
  # Change this to your image URL or file path

# Display the logo/image in the top left corner
st.sidebar.image(logo_url, width=150)

page_bg_img = '''
<style>
section.main.css-uf99v8.ea3mdgi5 {
    background-image: url("https://images.unsplash.com/photo-1589216532372-1c2a367900d9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80");
    background-size: 100%;
    opacity:0.8;
    background-position: top;
    background-repeat: no-repeat;
    background-attachment: local;
}

/* Provide a valid URL for the sidebar background image */
[data-testid=stSidebar]{
   /* background-image: url("https://images.unsplash.com/photo-1634632109601-bcfd0a649a07?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1887&q=80");*/
    background-size: 50%;
    background-position: left; 
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.css-j7qwjs.eczjsme7{
      display: flex;
      flex-direction: row; /* Arrange buttons horizontally */
      align-items: center;
      background-color: transparent; /* Transparent background */
      font-color: white; /* White text */
      border: 1px solid white; /* White border */
      border-radius: 20px; /* Rounded corners */
      padding: 5px 5px; /* Padding for button size */
      cursor: pointer; /* Change cursor on hover */
      transition: background-color 0.3s, color 0.3s;
      margin-bottom: 20px; /* Add right margin between buttons */ 
      width:200px;
      display: inline-block;
      font-size: 14px;
      text-align:center;
      margin-left:20px;
}

.css-j7qwjs.eczjsme7:hover {
      background-color: grey; /* White background on hover */
      text-color: black; /* Dark text on hover */
    }

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# st.title("Main Page")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")

# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered:", my_input)

    
from login import main as login_page
from signup import main as signup_page
# from Home import main as home_page


# Create a Streamlit subpage
with st.subheader("Navigation"):
    page = st.radio("Go to:", ["Login", "Sign Up"])

# Display the selected page content
# if page == "Home":
#     home_page()
if page == "Login":
    login_page()
elif page == "Sign Up":
    signup_page()   
