import streamlit as st
import ollama

# Set page configuration
st.set_page_config(page_title="Gemma Hacktoberfest AI Reviewer", page_icon="🎃", layout="wide")

st.title("🎃 Hacktoberfest AI Code Assistant (Powered by Gemma)")
st.caption("A local developer assistant for git commit messages, code reviews, and bug fixes.")

# Sidebar options
st.sidebar.header("Task Selection")
task = st.sidebar.radio(
    "Choose a feature:",
    ["Generate Conventional Commit Message", "Quick Code & Security Review", "Explain Code for PR Description"]
)

# Main input area
code_input = st.text_area("Paste your code snippet or git diff here:", height=200, placeholder="def add(a, b):\n    return a + b")

if st.button("Run with Gemma 🚀"):
    if not code_input.strip():
        st.warning("Please enter some code or a git diff first!")
    else:
        # Construct prompt based on selection
        if task == "Generate Conventional Commit Message":
            prompt = f"Write a clean, standard git commit message following conventional commits format (e.g., feat:, fix:, docs:) based on this code:\n\n{code_input}"
        elif task == "Quick Code & Security Review":
            prompt = f"Analyze this code. Provide 3 bullet points: 1) Potential bugs, 2) Performance or security flaws, 3) Suggested clean code improvements:\n\n{code_input}"
        else:
            prompt = f"Explain what this code does in 2 concise sentences suitable for an open-source Pull Request description:\n\n{code_input}"

        with st.spinner("Gemma is analyzing..."):
            try:
                response = ollama.chat(
                    model='gemma:2b',  # Adjust to your downloaded model tag
                    messages=[{'role': 'user', 'content': prompt}]
                )
                
                st.subheader("Results:")
                st.markdown(response['message']['content'])
            except Exception as e:
                st.error(f"Error connecting to Ollama: {e}")