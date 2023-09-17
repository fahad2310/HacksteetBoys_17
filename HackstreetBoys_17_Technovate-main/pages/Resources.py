import streamlit as st
import streamlit.components.v1 as components

logo_url = "logo.png"
  # Change this to your image URL or file path

# Display the logo/image in the top left corner
st.sidebar.image(logo_url, width=150)

img_urll="resour.jpg"
st.image(img_urll, width=500)

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


# Title of the help page
st.title("Legal Help Page")

# Introduction
st.markdown("""
Welcome to our **Legal Help Page**. Here, you can find educational materials and resources to enhance your understanding of legal concepts and implications.
""")

# Educational Materials
st.header("Educational Materials")
st.write("Explore the following educational resources to learn more:")

# Link to Legal Glossary
st.subheader("Legal Glossary")
st.write("Check our comprehensive legal glossary to understand legal terms and definitions.")
legal_glossary_link = "[Legal Glossary](https://example.com/legal-glossary)"
st.markdown(legal_glossary_link, unsafe_allow_html=True)

# Link to Articles
st.subheader("Articles")
st.write("Read articles on various legal topics to gain insights and knowledge.")
articles_link = "[Legal Articles](https://example.com/legal-articles)"
st.markdown(articles_link, unsafe_allow_html=True)

# Interactive Quiz
st.header("Interactive Quiz")
st.write("Test your legal knowledge with our interactive quiz.")

# Define quiz questions and correct answers
quiz_questions = [
    {
        "question": "What does 'pro bono' mean in legal terms?",
        "options": ["For the good of all", "In private", "Provisional order", "Legal fees"],
        "correct_option": "For the good of all"
    },
    {
        "question": "What is a 'subpoena' used for in legal proceedings?",
        "options": ["To order a drink at a bar", "To request a court appearance", "To file a lawsuit", "To draft legal documents"],
        "correct_option": "To request a court appearance"
    },
    {
        "question": "What does 'habeas corpus' refer to?",
        "options": ["A legal principle", "A type of contract", "A form of currency", "A petition to challenge unlawful detention"],
        "correct_option": "A petition to challenge unlawful detention"
    }
]

# Initialize score
score = 0

# Iterate through quiz questions
for i, quiz in enumerate(quiz_questions, start=1):
    st.subheader(f"Question {i}: {quiz['question']}")
    selected_option = st.radio(f"Select an option:", quiz["options"])
    
    # Check if the selected option is correct
    if selected_option == quiz["correct_option"]:
        st.success(f"Correct! '{selected_option}' is the right answer.")
        score += 1
    else:
        st.error(f"Sorry, that's incorrect. The correct answer is '{quiz['correct_option']}'.")

# Display the final score
st.subheader("Quiz Results")
st.write(f"You scored {score} out of {len(quiz_questions)} questions.")

# Additional Resources
st.header("Additional Resources")
st.write("Explore more resources to dive deeper into legal concepts:")

# Link to Legal Books
st.subheader("Legal Books")
st.write("Discover recommended legal books and publications.")
books_link = "[Legal Books](https://example.com/legal-books)"
st.markdown(books_link, unsafe_allow_html=True)

# Link to Legal Courses
st.subheader("Legal Courses")
st.write("Enroll in online legal courses to expand your knowledge.")
courses_link = "[Legal Courses](https://example.com/legal-courses)"
st.markdown(courses_link, unsafe_allow_html=True)

# Disclaimer
st.warning("Please note that the information provided here is for educational purposes only and should not be considered legal advice. Consult with a legal professional for specific legal matters.")

# Footer
st.text("© 2023 SimpliLegal. All rights reserved.")

