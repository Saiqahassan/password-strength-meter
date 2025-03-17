import streamlit as st 
import re

st.set_page_config(page_title="Password strength checker", page_icon="🔐", layout="centered")

st.title("💪 Password strength meter")
st.write("Enter your password below to check its strength")

password = st.text_input("Enter your Password", type="password")

score = 0
feedback = []
  
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both upper and lower case characters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit")

    if re.search(r"!@#$%&*", password):
        score += 1  
    else:
        feedback.append("❌ Password must contain at least one special character (!@#$%&*)") 


    # Display password strength result
    if score == 4:
        feedback.append("✅ Password is strong")
    elif score == 3:
        feedback.append("⚠️ Password is medium")
    else:
        feedback.append("❌ Password is weak. To secure your account, please make it stronger.")

    #feedback
    if feedback:
        st.markdown("### Improvement needed:")
        for message in feedback:
            st.write(message)

else:
    st.info("Please enter your password first!")
 