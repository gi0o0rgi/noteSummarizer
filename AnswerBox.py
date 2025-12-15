import streamlit as st
from openai import OpenAI

# 1. Setup the page
st.title("5-Second Summarizer")
st.write("Paste your messy lecture notes below, and I'll clean them up.")

# 2. Get the API key (For a real project, use 'secrets', but this works for testing)
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# 3. Create the text box for the user
user_input = st.text_area("Paste notes here:", height=200)

# 4. The Magic Button
if st.button("Summarize It!"):
    if not api_key:
        st.warning("Please enter an API key first!")
    elif not user_input:
        st.warning("Please enter some text to summarize!")
    else:
        # Connect to the Brain
        client = OpenAI(api_key=api_key)
        
        # Send the instruction
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes messy student notes into clean bullet points."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Show the result
        summary = response.choices[0].message.content
        st.success("Here is your summary:")
        st.write(summary)