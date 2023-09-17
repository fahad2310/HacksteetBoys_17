import openai
import streamlit as st
from streamlit_chat import message
from apikey import apikey
import pyperclip  # Import pyperclip for copying text to the clipboard

# Define API key
openai.api_key = "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"

logo_url = "logo.png"
  # Change this to your image URL or file path

# Display the logo/image in the top left corner
st.sidebar.image(logo_url, width=150)

imp_url="ailaw.png"
st.image(imp_url, width=500)

page_bg_img = '''
<style>
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

# Define chatbot responses
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

st.title("SimpliAI is here to help you!")
st.write("SimpliAI is a versatile AI-powered legal assistant designed to simplify and enhance various aspects of the legal world. It offers users comprehensive support with legal documentation, providing context-aware suggestions and explanations, automating time-consuming tasks, ensuring data privacy, and even facilitating access to legal professionals for consultation and review. With its intuitive interface and educational resources, SimpliAI empowers users to navigate complex legal matters with confidence and efficiency.")

if 'generated' not in st.session_state: 
    st.session_state['generated'] = []

if 'past' not in st.session_state: 
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You:", "Hello, how are you?", key="input")
    return input_text

user_input = get_text()

# Send button and Copy Solution button
if st.button("Send"):
    if user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

        # Copy Solution button for each generated message
        if st.button(f"Copy Solution {i}"):
            copy_to_clipboard(st.session_state["generated"][i])
            st.write("Solution copied to clipboard!")




