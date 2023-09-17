import streamlit as st

# Change the page name in the sidebar
st.set_page_config(page_title="Connect To Lawyer")

logo_url = "logo.png"
  # Change this to your image URL or file path

# Display the logo/image in the top left corner
st.sidebar.image(logo_url, width=150)

img_urll="lawyer.jpg"
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

# Your Streamlit app code goes here
st.title("Connect To Lawyer")
st.write("SimpliLawyers simplifies the search for legal experts. Whether it's family law, business contracts, or estate planning, we connect clients with the right lawyers swiftly. Your legal solutions, simplified.")

# Rest of your app
import streamlit as st

# Dummy lawyer data (you can replace this with real data)
# Dummy lawyer data (you can replace this with real data)
# Dummy lawyer data with Indian names
lawyers = [
    {
        "name": "Amit Kumar",
        "specialty": "Criminal Defense",
        "contact_info": "Phone: 987-654-3210\nEmail: amit@example.com",
        "bio": "Amit Kumar is a passionate criminal defense attorney dedicated to justice."
    },
    {
        "name": "Sneha Verma",
        "specialty": "Personal Injury",
        "contact_info": "Phone: 555-123-4567\nEmail: sneha@example.com",
        "bio": "Sneha Verma specializes in personal injury cases, seeking justice for victims."
    },
    {
        "name": "Divya Singh",
        "specialty": "Family Law",
        "contact_info": "Phone: 111-222-3333\nEmail: divya@example.com",
        "bio": "Divya Singh is a family law attorney committed to helping families in difficult times."
    },
    {
        "name": "Rahul Sharma",
        "specialty": "Real Estate Law",
        "contact_info": "Phone: 444-555-6666\nEmail: rahul@example.com",
        "bio": "Rahul Sharma handles real estate transactions with precision and expertise."
    },
    {
        "name": "Priya Gupta",
        "specialty": "Estate Planning",
        "contact_info": "Phone: 888-777-9999\nEmail: priya@example.com",
        "bio": "Priya Gupta provides comprehensive estate planning services to secure your future."
    },
    {
        "name": "Ajay Patel",
        "specialty": "Immigration Law",
        "contact_info": "Phone: 777-666-5555\nEmail: anjali@example.com",
        "bio": "Anjali Kapoor assists clients with immigration matters, ensuring a smooth process."
    },
    {
        "name": "Vikram Menon",
        "specialty": "Intellectual Property",
        "contact_info": "Phone: 555-888-1111\nEmail: vikram@example.com",
        "bio": "Vikram Menon protects your intellectual property rights with diligence."
    },
    {
        "name": "Nisha Sharma",
        "specialty": "Employment Law",
        "contact_info": "Phone: 777-888-9999\nEmail: nisha@example.com",
        "bio": "Nisha Sharma fights for employee rights and fair workplace practices."
    },
    {
        "name": "Rajesh Kumar",
        "specialty": "Environmental Law",
        "contact_info": "Phone: 111-222-3333\nEmail: rajesh@example.com",
        "bio": "Rajesh Kumar is a dedicated environmental lawyer working for a sustainable future."
    }
]


    # Add more lawyer profiles
    # ...


# Create a Streamlit app
st.title("Lawyer Profiles")

# Search functionality
search_query = st.text_input("Search by keywords:")

# Reset button
reset_button_clicked = st.button("Reset")

# Display lawyer profiles based on search query
for lawyer in lawyers:
    if (not search_query or
            any(keyword.lower() in lawyer["name"].lower() or
                keyword.lower() in lawyer["specialty"].lower() or
                keyword.lower() in lawyer["bio"].lower()
                for keyword in search_query.split())) or reset_button_clicked:
        st.subheader(lawyer["name"])
        st.write(f"Specialty: {lawyer['specialty']}")
        st.write(f"Contact Information:\n{lawyer['contact_info']}")
        st.write(f"Bio:\n{lawyer['bio']}")
        st.markdown("---")  # Add a separator between profiles