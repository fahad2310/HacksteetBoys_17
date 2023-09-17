# import streamlit as st
# import openai
# import pdfplumber

# # Set your OpenAI API key here
# openai.api_key = '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'

# logo_url = "logo.png"
#   # Change this to your image URL or file path

# # Display the logo/image in the top left corner
# st.sidebar.image(logo_url, width=150)

# page_bg_img = '''
# <style>
# /* Provide a valid URL for the sidebar background image */
# [data-testid=stSidebar]{
#    /* background-image: url("https://images.unsplash.com/photo-1634632109601-bcfd0a649a07?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1887&q=80");*/
#     background-size: 50%;
#     background-position: left; 
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }

# .css-j7qwjs.eczjsme7{
#       display: flex;
#       flex-direction: row; /* Arrange buttons horizontally */
#       align-items: center;
#       background-color: transparent; /* Transparent background */
#       font-color: white; /* White text */
#       border: 1px solid white; /* White border */
#       border-radius: 20px; /* Rounded corners */
#       padding: 5px 5px; /* Padding for button size */
#       cursor: pointer; /* Change cursor on hover */
#       transition: background-color 0.3s, color 0.3s;
#       margin-bottom: 20px; /* Add right margin between buttons */ 
#       width:200px;
#       display: inline-block;
#       font-size: 14px;
#       text-align:center;
#       margin-left:20px;
# }

# .css-j7qwjs.eczjsme7:hover {
#       background-color: grey; /* White background on hover */
#       text-color: black; /* Dark text on hover */
#     }

# [data-testid="stHeader"] {{
#     background: rgba(0,0,0,0);
# }}

# [data-testid="stToolbar"] {{
#     right: 2rem;
# }}
# </style>
# '''
# st.markdown(page_bg_img, unsafe_allow_html=True)

# st.title("Simplifying Complex Legal PDFs!")
# st.write("SimpliTeacher is your personal guide to understanding legal documents. Upload your PDFs, and let our AI analyze and explain complex legal terms. Gain clarity and confidence in your legal matters with simplified explanations right at your fingertips.")

# # # Upload PDF file
# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file:
#     # Read the PDF file
#     pdf = pdfplumber.open(uploaded_file)
#     text = ""
    
#     # Extract text from PDF
#     for page in pdf.pages:
#         text += page.extract_text()
    
#     # Close the PDF file
#     pdf.close()
    
#     st.subheader("Extracted Text from PDF")
#     st.write(text)
    
#     # Split the text into paragraphs
#     paragraphs = text.split('\n\n')
    
#     st.subheader("Legal Terms Detected")
    
#     legal_terms = []  # To store legal terms found
    
#     # Define a function to find legal terms using OpenAI
#     def find_legal_terms(text):
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=f"Find legal terms in the following text:\n{text}",
#             max_tokens=50,
#             stop=None,
#             temperature=0.7,
#         )
#         return response.choices[0].text.strip()
    
#     # Find and display legal terms
#     for paragraph in paragraphs:
#         legal_term = find_legal_terms(paragraph)
#         if legal_term:
#             legal_terms.append(legal_term)
#             st.write(f"- {legal_term}")
    
#     if legal_terms:
#         st.subheader("Explanation of Legal Terms")
        
#         for term in legal_terms:
#             explanation = openai.Completion.create(
#                 engine="text-davinci-002",
#                 prompt=f"Explain the legal term: {term}",
#                 max_tokens=100,
#                 stop=None,
#                 temperature=0.7,
#             )
#             st.write(f"*{term}:* {explanation.choices[0].text.strip()}")
#     else:
#         st.write("No legal terms found in the document.")

import streamlit as st
import openai
import pdfplumber

# Set your OpenAI API key here
openai.api_key = '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'

# logo_url = "logo.png"
#   # Change this to your image URL or file path

# # Display the logo/image in the top left corner
# st.sidebar.image(logo_url, width=150)

imp_url="lawteach.jpg"
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

st.title("Simplifying Complex Legal PDFs!")
st.write("SimpliTeacher is your personal guide to understanding legal documents. Upload your PDFs, and let our AI analyze and explain complex legal terms. Gain clarity and confidence in your legal matters with simplified explanations right at your fingertips.")


# Display the logo/image in the top left corner
logo_url = "logo.png"
st.sidebar.image(logo_url, width=150)

# ... (Same background styling and title as before) ...

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf = pdfplumber.open(uploaded_file)
    text = ""

    # Extract text from PDF and split into paragraphs
    for page in pdf.pages:
        text += page.extract_text() + "\n\n"

    pdf.close()

    st.subheader("Extracted Text from PDF")
    st.write(text)

    # Split text into smaller chunks (paragraphs)
    paragraphs = text.split("\n\n")

    st.subheader("Legal Terms Detected")

    legal_terms = []

    for paragraph in paragraphs:
        # Find legal terms in each paragraph
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Find legal terms in the following text:\n{paragraph}",
            max_tokens=50,
            stop=None,
            temperature=0.7,
        )

        legal_term = response.choices[0].text.strip()

        if legal_term:
            legal_terms.append(legal_term)
            st.write(f"- {legal_term}")

    if legal_terms:
        st.subheader("Explanation of Legal Terms")

        for term in legal_terms:
            # Explain each legal term
            explanation = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"Explain the legal term: {term}",
                max_tokens=100,
                stop=None,
                temperature=0.7,
            )

            st.write(f"*{term}:* {explanation.choices[0].text.strip()}")
    else:
        st.write("No legal terms found in the document.")
