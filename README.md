# TalentScout – Intelligent Hiring Assistant

An AI-powered hiring assistant chatbot built using **Streamlit** and **LLaMA (via Ollama)** to streamline the initial candidate screening process. This assistant gathers essential candidate details and dynamically generates technical questions based on their declared tech stack.

---

## 🚀 Features

- ✅ Conversational UI using Streamlit
- ✅ Collects candidate details: Name, Email, Phone, Experience, etc.
- ✅ Accepts tech stack input (e.g., Python, React, Django)
- ✅ Uses LLaMA (via Ollama) to generate tech-specific interview questions
- ✅ Handles conversation flow and context
- ✅ Optional simulated responses for cloud deployment

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend Model:** LLaMA 3.1 via Ollama (local)
- **Language:** Python 3.10+

---

## 📦 Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install streamlit requests
   ```

2. **Install and Run Ollama**:
   - [Download Ollama](https://ollama.com)
   - Pull the model:
     ```bash
     ollama pull llama3.1
     ```
   - Start the Ollama server:
     ```bash
     ollama serve
     ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run hiring_assistant_chatbot.py
   ```

---

## 🌐 Optional: Cloud Deployment

Since Streamlit Cloud doesn’t support Ollama, set:
```python
LOCAL_MODE = False
```
This enables simulated responses so the app works online.

---

## 🧠 Prompt Design

Prompts are generated dynamically like:
```
Generate 3 technical interview questions for a candidate skilled in Python.
```
These are sent to the LLM for each declared tech in the stack.

---

## 🔐 Data Privacy

All data is handled in-session (not stored permanently). Placeholder methods for secure handling are included. No external APIs are used.

---

## 📹 Demo

If deploying to the cloud isn't possible, record a short video demo using [Loom](https://loom.com) showing:
- App startup
- Chat flow from greeting → form → tech stack → question generation → thank you

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|----------|----------|
| LLMs can’t run on Streamlit Cloud | Added simulated responses for cloud mode |
| Need for dynamic prompt generation | Designed modular prompt engine per tech input |
| Local model API calls | Integrated Ollama via local REST API |

---

## 📁 File Structure

```
├── hiring_assistant_chatbot.py   # Main Streamlit app
├── README.md                     # Project documentation
```

---

## ✍️ Author

**[Your Name Here]**

---

## ✅ Submission Checklist

- [x] Streamlit chatbot implemented
- [x] LLaMA model used via Ollama (local)
- [x] Modular code structure
- [x] Readme completed
- [x] Deployment-ready (local or cloud)
- [x] Optional: Loom demo created

---

## 📎 Links

- [Streamlit Docs](https://docs.streamlit.io/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Ollama](https://ollama.com/)
- [GDPR Compliance](https://gdpr.eu/)

---

> "This assistant is designed to improve the efficiency of tech recruitment through LLM-powered smart interactions."

