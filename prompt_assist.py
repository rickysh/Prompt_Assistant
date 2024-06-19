from openai import OpenAI
import streamlit as st


client = OpenAI()

left_col, right_col = st.columns(2)
with left_col:
    st.title("English Prompt Assistant")
with right_col:
    st.image("icon.jpg", width=150)

st.text("Write your prompt:")
user_prompt = st.text_input("user_prompt", label_visibility="hidden")
rephrased_prompt = ""
if user_prompt:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are an English teacher, skilled in rephrasing and correcting misspellings and typos of students and non-English speakers."},
        {"role": "user", "content": user_prompt + " ** Please rephrase this text."}
    ]
    )

    rephrased_prompt = completion.choices[0].message.content

st.text("")
st.text("")
st.text("")
st.text("Let's re-write it better:")
st.text("")
st.text("")
st.code(rephrased_prompt, language="markdown")
