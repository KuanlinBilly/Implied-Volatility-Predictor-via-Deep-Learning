import streamlit as st
import hashlib
from predictor_app import * 

# Function to set the background image
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            -webkit-background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            background-size: cover;
        }}
        .stApp .stMarkdown h1, .stApp .stMarkdown h2, .stApp .stMarkdown p {{
            color: black;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
def reset_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: none;
        }}
        .stApp .stMarkdown h1, .stApp .stMarkdown h2, .stApp .stMarkdown p {{
            color: inherit;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to verify the user's password (you should replace this with your actual authentication method)
def verify_password(stored_password, provided_password):
    return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

# Define a function to display the login page
def show_login_page(placeholders):
    # Set the background image here
    picture_url = "https://i.postimg.cc/t45ryBwW/Adobe-Stock-328664888.jpg"
    set_background_image(picture_url)  # Change the URL to your custom image

    my_username = "ndhu"
    my_password = "1234"
    placeholders[0].title("Welcome!")
    placeholders[1].markdown("**This is an Implied Volatility Predictor**")
    placeholders[2].write("Please enter your username and password:")

    username = placeholders[3].text_input("Username", value = my_username ) #為了方便，先預設填入帳密
    password = placeholders[4].text_input("Password", type="password", value= my_password)

    if placeholders[5].button("Login"):
        # You should replace these credentials with your actual username and password
        stored_username = my_username
        stored_password = hashlib.sha256(my_password.encode()).hexdigest()

        if username == stored_username and verify_password(stored_password, password):
            for placeholder in placeholders:
                placeholder.empty()
            return True
        else:
            placeholders[6].error("Incorrect username or password")
            return False
    # Add a new placeholder for the GitHub hyperlink
    placeholders[7].markdown(
        f'<p style="text-align: center; color: black; margin-top: 15px;"><a href="https://github.com/KuanlinBilly/Implied-Volatility-Predictor" target="_blank">Click here</a> to see the source code on GitHub</p>',
        unsafe_allow_html=True,
    )

# Define a function to display the main content of the web app
def show_main_content():
    reset_background()  # Add this line to reset the background
    implied_volatility_predictor()

# Main function to display the login page or the main content depending on the login status
def main():
    if "login_status" not in st.session_state:
        st.session_state.login_status = False

    if not st.session_state.login_status:
        placeholders = [st.empty() for _ in range(8)]
        st.session_state.login_status = show_login_page(placeholders)

    if st.session_state.login_status:
        show_main_content()

if __name__ == "__main__":
    main()
