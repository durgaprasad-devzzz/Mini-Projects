import streamlit as st

st.set_page_config(page_title="Streamlit Demo")
st.title("Streamlit Demo")

color_text = st.text_input("What's your favorite color?")
go_button = st.button("Go", type="primary")

if go_button:
    st.write(f"I like {color_text} too!")
