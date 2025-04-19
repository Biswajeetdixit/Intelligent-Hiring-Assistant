# hiring_assistant_chatbot.py



import streamlit as st
import requests
import json


LOCAL_MODE = True
OLLAMA_MODEL = "llama3.1"

# Call local Ollama model
def generate_llama_response(prompt):
    if LOCAL_MODE:
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            )
            result = response.json()
            return result.get("response", "[No response from model]")
        except Exception as e:
            return f"[Error calling LLaMA model: {e}]"
    else:
        
        if "python" in prompt.lower():
            return "1. What are Python decorators?\n2. Explain list comprehensions.\n3. What is the difference between a list and a tuple?"
        return "Here are some general questions based on your tech stack."

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 'greeting'
    st.session_state.candidate_info = {}
    st.session_state.tech_stack = []

# Greeting screen
if st.session_state.stage == 'greeting':
    st.title("TalentScout Hiring Assistant")
    st.write("👋 Hello! I'm your virtual hiring assistant. Let's begin with a few details about you.")
    if st.button("Start Interview"):
        st.session_state.stage = 'info_gathering'
        st.rerun()

# Candidate Info Form
elif st.session_state.stage == 'info_gathering':
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.candidate_info = {
            "Full Name": full_name,
            "Email": email,
            "Phone": phone,
            "Experience": experience,
            "Position": position,
            "Location": location
        }
        st.session_state.stage = 'tech_stack'
        st.rerun()

# Tech Stack Input
elif st.session_state.stage == 'tech_stack':
    st.write("Awesome! Please enter the technologies you're skilled in.")
    tech_input = st.text_area("Enter your tech stack (e.g., Python, React, Django, SQL)")
    if st.button("Generate Questions"):
        st.session_state.tech_stack = [tech.strip() for tech in tech_input.split(',')]
        st.session_state.stage = 'generate_questions'
        st.rerun()

# Generate Technical Questions
elif st.session_state.stage == 'generate_questions':
    st.subheader("Here are your technical questions:")
    for tech in st.session_state.tech_stack:
        prompt = f"Generate 3 technical interview questions for a candidate skilled in {tech}."
        questions = generate_llama_response(prompt)
        st.markdown(f"**{tech}:**\n{questions}")
    if st.button("Finish Interview"):
        st.session_state.stage = 'end_convo'
        st.rerun()

# End Conversation
elif st.session_state.stage == 'end_convo':
    st.success("🎉 Thank you for your time! We’ll get back to you with the next steps.")
    st.markdown("You can now close this tab. Have a great day!")
