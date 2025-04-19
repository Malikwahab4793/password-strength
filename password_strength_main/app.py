import streamlit as st
def check_password(password):
    tips = []
    score = 0

    if len(password)>= 8:
        score +=1
    else:
        tips.append("🔴use at least 8 character.")
    if any(c.isupper() for c in password):
        score +=1
    else:
        tips.append("🟠Include upper latter")

    if any(c.islower() for c in password):
        score +=1
    else:
        tips.append("🟠Include lower latter")

    if any(c.isdigit() for c in password):
        score +=1
    else:
        tips.append("🟡Include Add number (0,9)")
    if any(c in "!@#$%^&*" for c in password):
        score +=1
    else:
        tips.append("🔺use a special character(!@#$%^&*)")
    return score, tips

def main():
    st.title("🔐Password Strength Meter!")
    password= st.text_input("Enter Password 🔑", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("Strong Password! Secure & Save✅")
        elif score == 3 or score == 4:
            st.warning("❌Moderate Password! Improve it.")
        else:
            st.error("weak-password! Follow these steps")
        for tip in tips:
            st.write(tip)
    st.markdown("<hr style='border:1px solid #aaa;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; color: gray;'>© Malik Wahab</p>", unsafe_allow_html=True)

    


main()