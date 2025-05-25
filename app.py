
import streamlit as st
import subprocess
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

print("✅ App is starting...")
print("🔧 Python version:", sys.version)
print("📂 Current directory:", os.getcwd())
print("📁 Files in current directory:", os.listdir())
print("🔑 OPENAI:", bool(os.getenv("OPENAI_API_KEY")))
print("🔑 SERPAPI:", bool(os.getenv("SERPAPI_API_KEY")))

def extract_blog(text):
    start = text.find("**Title:")
    if start == -1:
        return text
    return text[start:]

st.title("🤖 AI Research Assistant")

st.markdown("This tool runs autonomous agents to research, analyze, and summarize any topic into a blog article.")

topic = st.text_input("Enter a research topic:", placeholder="e.g. Top AI startups in robotics 2024")

if st.button("Run AI Agents") and topic:
    with st.spinner("Running autonomous workflow... this may take 30–60 seconds"):
        try:
            result = subprocess.check_output(["python3", "research_agent.py", "--topic", topic], text=True, stderr=subprocess.STDOUT)
            article = extract_blog(result)
            st.success("Done!")
            st.markdown("### 🧠 Blog Output")
            st.markdown(article)
        except subprocess.CalledProcessError as e:
            st.error(f"An error occurred: {e.output}")
