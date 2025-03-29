import streamlit as st

st.title("👨‍💻 My Portfolio")

menu = st.sidebar.radio("📌 Menu", ["Home", "Projects", "Contact"])

if menu == "Home":
    st.header("Welcome!")
    st.write("I'm a developer skilled in Python, Streamlit, and more. 🚀")

elif menu == "Projects":
    st.header("🛠️ Projects")
    st.write("- **AI Chatbot** 🤖")
    st.write("- **E-commerce Website** 🛒")
    st.write("- **Data Dashboard** 📊")

elif menu == "Contact":
    st.header("📬 Contact Me")
    st.write("📧 Email: example@email.com")
    st.write("📱 [LinkedIn](https://linkedin.com)")
