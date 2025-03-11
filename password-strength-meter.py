import streamlit as st
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
    score = 5 - sum(errors)  # Jitni kam errors hongi, utna acha score hoga
    return strength_levels[score]

def main():
    st.title("🔒 Password Strength Meter")
    st.write("Enter a password to check its strength")

    password = st.text_input("Enter Password", type="password")
    
    if password:
        strength = check_password_strength(password)
        st.write(f"**Password Strength:** {strength}")

        # Progress bar
        strength_score = {"Very Weak": 0.2, "Weak": 0.4, "Moderate": 0.6, "Strong": 0.8, "Very Strong": 1.0}
        st.progress(strength_score[strength])

if __name__ == "__main__":
    main()
