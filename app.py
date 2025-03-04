import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength.")

password = st.text_input("Password", type="password") # Password input field

if password: # Check if the user has entered a password
    score, feedback = check_password_strength(password)

    st.subheader("Strength Evaluation:")

    if score >= 4:
        st.success("✅ Strong Password! 💪")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features. 🤔")
    elif score >= 1:
        st.error("❌ Weak Password - Improve it using the suggestions below! 😞")
    else:
        st.error("❌ Very Weak Password - Needs significant improvement! 😞")

    if feedback:
        st.subheader("Suggestions for Improvement:")
        for message in feedback:
            st.write(message)
else:
    st.info("Enter a password to evaluate its strength.")