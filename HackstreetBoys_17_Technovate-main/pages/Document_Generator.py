# import streamlit as st
# from reportlab.pdfgen import canvas
# from io import BytesIO
# import requests

# logo_url = "logo.png"
#   # Change this to your image URL or file path

# # Display the logo/image in the top left corner
# st.sidebar.image(logo_url, width=150)

# img_url="legdoc.jpg"
# st.image(img_url, width=500)

# # Function to generate the legal document using the OpenAI API
# def generate_legal_document(template, user_input):
#     prompt = template.format(**user_input)

#     api_url = "https://api.openai.com/v1/chat/completions"
#     api_key = "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"  # Replace with your OpenAI API key

#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#     }

#     data = {
#         "model": "gpt-3.5-turbo",
#         "messages": [
#             {"role": "system", "content": "You are a helpful assistant that generates legal documents."},
#             {"role": "user", "content": prompt},
#         ]
#     }

#     response = requests.post(api_url, json=data, headers=headers)

#     if response.status_code == 200:
#         response_data = response.json()
#         legal_document = response_data['choices'][0]['message']['content']
#         return legal_document
#     else:
#         return f"API request failed with status code {response.status_code}: {response.text}"

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

# # Function to generate PDF from text
# def generate_pdf(text):
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer)
#     p.drawString(100, 750, text)
#     p.save()
#     buffer.seek(0)
#     return buffer

# # Streamlit app
# st.title("Legal Document Generator and Editor")

# # Define legal document templates (prompts)
# legal_document_templates = {
#     "Rental Agreement": "Generate a legal contract for a rental agreement between {landlord_name} and {tenant_name} for the property located at {property_address}. The agreement should include the following terms and conditions: {terms_and_conditions}",
#     "Divorce Agreement": "Generate a divorce agreement between {spouse1_name} and {spouse2_name}. This agreement should outline the division of assets, custody arrangements for children, and any alimony or support payments.",
#     # Add more templates for different types of documents
# }

# # Template selection dropdown
# template_name = st.selectbox("Select a Legal Document Template", list(legal_document_templates.keys()))

# # User input fields
# user_input = {}
# for key in legal_document_templates[template_name].split('{')[1:]:
#     field = key.split('}')[0]
#     user_input[field] = st.text_input(f"{field.replace('_', ' ').title()}", key)

# # Generate the document
# if st.button("Generate Document"):
#     legal_doc = generate_legal_document(legal_document_templates[template_name], user_input)

#     # Display the generated legal document
#     st.subheader("Generated Legal Document:")
#     st.write(legal_doc)

#     # Allow users to edit the document
#     st.session_state.generated_document = legal_doc
#     st.session_state.editing = True

# # Edit the document
# if hasattr(st.session_state, 'editing') and st.session_state.editing:
#     st.subheader("Edit the Generated Document:")
#     edited_doc = st.text_area("Edit Document", st.session_state.generated_document)
#     st.session_state.generated_document = edited_doc

#     # Offer to save/download as PDF
#     if st.button("Save as PDF"):
#         pdf_buffer = generate_pdf(edited_doc)
#         st.write(pdf_buffer)
#         st.download_button("Download PDF", pdf_buffer, key="download_pdf")

# st.info("Disclaimer: The generated document should be reviewed by a legal professional for accuracy and compliance with local laws and regulations.")

import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from io import BytesIO
import requests
import datetime
import time


# Function to generate the legal document using the OpenAI API
def generate_legal_document(template, user_input):
    prompt = template.format(**user_input)

    api_url = "https://api.openai.com/v1/chat/completions"
    api_key = "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"  # Replace with your OpenAI API key

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates legal documents."},
            {"role": "user", "content": prompt},
        ]
    }

    loading_text = "Generating document..."
    with st.spinner(loading_text):
        response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        legal_document = response_data['choices'][0]['message']['content']
        return legal_document
    else:
        return f"API request failed with status code {response.status_code}: {response.text}"
    
logo_url = "logo.png"
  # Change this to your image URL or file path

# Display the logo/image in the top left corner
st.sidebar.image(logo_url, width=150)

img_url="legdoc.jpg"
st.image(img_url, width=500)
    
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

    

    


# Function to generate PDF from text
def generate_pdf(text):
    buffer = BytesIO()

    # Initialize 'doc' within this function
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    styles = getSampleStyleSheet()
    story = []

    # Define custom paragraph style for content
    content_style = ParagraphStyle(name="CustomContentStyle", parent=styles["Normal"])
    content_style.spaceAfter = 12

    # Split text into paragraphs and add to the PDF
    paragraphs = text.split("\n")
    for paragraph in paragraphs:
        p = Paragraph(paragraph, content_style)
        story.append(p)

    # Build the PDF document
    doc.build(story)
    buffer.seek(0)
    return buffer

# Function to reset input fields
def reset_input_fields():
    return {field: "" for field in user_input.keys()}

# Streamlit app
st.title("Legal Document Generator and Editor")
st.write("Effortlessly create legal documents tailored to your needs with SimpliLegal's Document Generator. Save time, reduce errors, and ensure legal compliance in just a few clicks.")

# Define legal document templates (prompts)
legal_document_templates = {
    "Rental Agreement": "Generate a legal contract for a rental agreement between {landlord_name} and {tenant_name} for the property located at {property_address}. The agreement should include the following terms and conditions:\n\n"
                        "1.  Agreement Date: {agreement_date}\n"
                        "2. Rent Amount: ${rent_amount} per month\n"
                        "3. Lease Term: {lease_term} months\n "
                        "4.Security Deposit: ${security_deposit}\n",  
                        
    "Divorce Agreement": "Generate a divorce agreement between {husband_name} and {spouse_name}. This agreement should outline the division of assets, custody arrangements for children, and any alimony or support payments.Alimony: {alimony_details}\n"
                         "1.  Agreement Date: {agreement_date}\n",
    "Employment Contract": "This Employment Contract is entered into between {employer_name} (the 'Employer') and {employee_name} (the 'Employee').\n\n"
                           "1. Position: {job_title}\n"
                           "2. Employment Start Date: {employment_start_date}\n"
                           "3. Salary: ${salary} per annum\n"
                           "4. Job Responsibilities: {job_responsibilities}\n",
    "Non-Disclosure Agreement": "Generate a non-disclosure agreement between {disclosing_party} and {receiving_party}...\n"
                            "1.  Agreement Date: {agreement_date}\n"
                            "2. Purpose of the Agreement: {purpose}\n"
                            "3. Duration of the Agreement: {duration} months\n"
    # Add more templates for different types of documents
}

# Sidebar for template selection
template_name = st.selectbox("Select a Legal Document Template", list(legal_document_templates.keys()))

# User input fields
user_input = st.session_state.get("user_input", {})

if st.button("Reset Input Fields"):
    user_input = reset_input_fields()

# for key in legal_document_templates[template_name].split('{')[1:]:
#     field = key.split('}')[0]
#     user_input[field] = st.text_input(f"{field.replace('_', ' ').title()}", user_input.get(field, ""))

for key in legal_document_templates[template_name].split('{')[1:]:
    field = key.split('}')[0]
    if field == 'agreement_date':
        selected_date = st.date_input(f"{field.replace('_', ' ').title()}", user_input.get(field, datetime.date.today()))
        user_input[field] = selected_date
    elif field == 'employment_start_date':
        selected_date = st.date_input(f"{field.replace('_', ' ').title()}", user_input.get(field, datetime.date.today()))
        user_input[field] = selected_date
    elif field == 'rent_amount':
        user_input[field] = st.slider(f"{field.replace('_', ' ').title()} (per month)", min_value=0, max_value=200000, step=5000)
    elif field == 'duration':
        lease_term_options = [1, 6, 12, 24, 36]  
        user_input[field] = st.selectbox(f"{field.replace('_', ' ').title()} (months)", lease_term_options, index=lease_term_options.index(user_input.get(field, 12)))
    elif field == 'salary':
        user_input[field] = st.slider(f"{field.replace('_', ' ').title()} (per annum)", min_value=0, max_value=3000000, step=50000)
    elif field == 'lease_term':
        lease_term_options = [1, 6, 12, 24, 36]  
        user_input[field] = st.selectbox(f"{field.replace('_', ' ').title()} (months)", lease_term_options, index=lease_term_options.index(user_input.get(field, 12)))
    elif field == 'security_deposit':
        user_input[field] = st.text_input(f"{field.replace('_', ' ').title()}", user_input.get(field, ""))
    else:
        user_input[field] = st.text_input(f"{field.replace('_', ' ').title()}", user_input.get(field, ""))

# Generate the document
if st.button("Generate Document"):
    legal_doc = generate_legal_document(legal_document_templates[template_name], user_input)

    # Display the generated legal document
    st.subheader("Generated Legal Document:")
    st.write(legal_doc)

    # Allow users to edit the document
    st.session_state.generated_document = legal_doc
    st.session_state.editing = True

# Edit the document
if hasattr(st.session_state, 'editing') and st.session_state.editing:
    st.subheader("Edit the Generated Document:")
    
    # Increase the height of the text area
    edited_doc = st.text_area("Edit Document", st.session_state.generated_document, height=300)
    st.session_state.generated_document = edited_doc

    # Offer to save/download as PDF
    if st.button("Save as PDF"):
    # Create a PDF document
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)

    # Define custom paragraph style for content
        styles = getSampleStyleSheet()
        content_style = ParagraphStyle(name="CustomContentStyle", parent=styles["Normal"])
        content_style.spaceAfter = 12

    # Split text into paragraphs and add to the PDF
        paragraphs = st.session_state.generated_document.split("\n")
        story = []

        image_path = "pasted_image_0_(3).png"  # Replace with your image file path
        img = Image(image_path, width=6 * inch, height=3 * inch)  # Adjust width and height as needed

        story.append(Spacer(1, 12))
        story.append(img)
        story.append(Spacer(1, 12))
        
        for paragraph in paragraphs:
            p = Paragraph(paragraph, content_style)
            story.append(p)

    # Load the image to be added to the PDF (adjust the file path)
   

    # Add the image to the PDF (you can adjust the position)
    

    # Build the PDF document
    doc.build(story)

    # Set the buffer position to the beginning
    pdf_buffer.seek(0)

    # Download the PDF with a custom file name
    st.write(pdf_buffer)
    st.download_button("Download PDF", pdf_buffer, key="download_pdf", file_name="generated_document.pdf")

st.info("Disclaimer: The generated document should be reviewed by a legal professional for accuracy and compliance with local laws and regulations.")


# Store the user_input in session_state
st.session_state.user_input = user_input
