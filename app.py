import streamlit as st
import re
import random
import string

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

def generate_password(length=12):
    """Generates a strong password of specified length."""
    if length < 8:
        length = 8  # Minimum length for a strong password

    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    while True: # Loop to ensure password meets all criteria
        password_list = []

        # Ensure at least one of each required character type
        password_list.append(random.choice(string.ascii_lowercase))
        password_list.append(random.choice(string.ascii_uppercase))
        password_list.append(random.choice(string.digits))
        password_list.append(random.choice("!@#$%^&*"))

        # Generate remaining characters
        remaining_length = length - 4
        for _ in range(remaining_length):
            password_list.append(random.choice(characters))

        random.shuffle(password_list) # Shuffle for randomness
        password = "".join(password_list)

        # Double check if generated password meets criteria (optional, but good practice)
        score, _ = check_password_strength(password)
        if score >= 4: # Strong password criteria met
            return password


st.title("🔐 Password Strength Meter & Generator")
st.write("Enter your password to check its strength, or generate a strong password with custom length below.")

# Password Strength Meter Section
st.subheader("Check Password Strength")
password_to_check = st.text_input("Password to Check", type="password", key="password_check") # Unique key

if password_to_check:
    score, feedback = check_password_strength(password_to_check)

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

st.markdown("---") # Separator line

# Password Generator Section
st.subheader("Generate Strong Password with Custom Length")
password_length = st.slider("Password Length", min_value=8, max_value=32, value=12, step=1,
                             help="Choose the desired length for the generated password (minimum 8 characters).")

if st.button("Generate Password"):
    generated_password = generate_password(password_length) # Pass length from slider
    st.success(f"Generated Password (Strong, Length: {password_length}):")
    st.code(generated_password, language=None) # Display in code format for clarity
    st.info("Copy and use this strong password. Consider storing it securely using a password manager.")