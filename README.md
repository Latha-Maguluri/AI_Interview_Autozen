# 🤖 AI Interview Simulation with AutoGen

This project simulates an **AI-powered interview system** using Microsoft's [AutoGen](https://github.com/microsoft/autogen) framework. It features three intelligent agents working together:

- 🧑‍💼 **Interviewer** – Asks structured, role-specific questions  
- 🧑‍🎓 **Candidate** – Simulates a user answering questions  
- 🎓 **Career Coach** – Provides feedback on each candidate's response

---

## 📂 Project Structure

.
├── Ai_interview.py # Main script to run the multi-agent interview
├── .env # (Optional) Store your OpenAI API key securely
├── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 How It Works

1. The **interviewer agent** asks 3 well-structured questions based on the given job role.
2. The **candidate** (you) types responses via the terminal.
3. The **career coach** gives helpful feedback after each response.
4. The session ends when you type **`TERMINATED`**.

---

## ⚙️ Requirements

- Python 3.8+
- OpenAI API Key
- `autogen`, `autogen-ext`, `python-dotenv` (install via pip)

---

## 🛠️ Installation

1. **Clone the repo**:

```bash
git clone https://github.com/Latha-Maguluri/ai-interview-autogen.git
cd ai-interview-autogen
Create and activate a virtual environment:

bash
Copy
Edit
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your API key in a .env file:

env
Copy
Edit
OPENAI_API_KEY=your-openai-api-key
🧠 Tech Stack
AutoGen

OpenAI GPT-4o

Python 3

Asyncio



