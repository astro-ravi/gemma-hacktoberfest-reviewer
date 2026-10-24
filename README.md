🎃 Gemma Reviewer — Hacktoberfest AI Code Assistant
A local, privacy-first developer assistant powered by Google's Gemma and Streamlit. Designed for Hacktoberfest to help open-source contributors and maintainers write standardized commit messages, generate PR summaries, and perform quick code reviews—entirely on-device.

🌟 Key Features
⚡ Conventional Commits: Generates clean, standardized commit messages (feat:, fix:, docs:) directly from code or diffs.

🛡️ Code & Quality Review: Highlights bugs, security risks, and optimization opportunities in a structured 3-point format.

📝 PR Description Generator: Summarizes code changes concisely for GitHub pull requests.

🔒 100% Private & Offline: Runs locally via Ollama with zero external API calls, ensuring complete source-code confidentiality.

🛠️ Tech Stack
Model: Google Gemma (gemma:2b)

Inference Engine: Ollama (Local Metal / GPU accelerated)

Frontend / UI: Streamlit

Language: Python 3.9+

🚀 Quickstart
1. Start Ollama with Gemma
Ensure Ollama is installed, then pull and run the model:

Bash
ollama run gemma:2b
2. Set Up the Project
Bash
# Clone the repository
git clone https://github.com/astro-ravi/gemma-hacktoberfest-reviewer.git
cd gemma-hacktoberfest-reviewer

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Run the Application
Bash
streamlit run app.py
Access the application in your browser at http://localhost:8501.

🤝 Open Source & Ethics
Responsible AI: Uses Gemma's open weights locally without transmitting proprietary or user code to third-party endpoints.

Hacktoberfest Spirit: Promotes clean commit hygiene and constructive peer reviews across open-source repositories.

📄 License
Distributed under the MIT License.
