# AI-Powered-GitHub-Issue-Assistant
An AI-powered web app that analyzes GitHub issues using LLMs and generates structured summaries to help teams classify, prioritize, and understand issues faster.

## Features

-  Accepts a **public GitHub repository URL** and **issue number**
-  Fetches issue title, body, and comments using the GitHub API
-  Uses an **LLM (Large Language Model)** to analyze the issue
-  Generates a **structured JSON summary** including:
  - Issue summary
  - Issue type (bug, feature request, documentation, etc.)
  - Priority score with justification
  - Suggested GitHub labels
  - Potential user impact
-  Clean and simple **Streamlit-based UI**

---

##  Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **APIs**:
  - GitHub REST API
  - Hugging Face Inference API
- **AI Model**: Mistral-7B-Instruct (via Hugging Face)
- **Environment Management**: python-dotenv

---

##  Project Structure

```
ai-github-issue-assistant/
│
├── app.py
├── github_client.py
├── llm_service.py
├── requirements.txt
├── .env.example
└── README.md
```

---

##  Setup & Run (Under 5 Minutes)

### 1️ Clone the Repository
```bash
git clone <your-github-repo-url>
cd ai-github-issue-assistant
```

---

### 2️ Create Virtual Environment (Optional)
```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

---

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️ Environment Variables

Create a `.env` file in the root directory:

```env
HF_API_TOKEN=your_huggingface_api_token
```

Get your token from:  
https://huggingface.co/settings/tokens

---

### 5️ Run the Application
```bash
streamlit run app.py
```

---

##  Example Usage

**Input**
- Repository URL: `https://github.com/facebook/react`
- Issue Number: `35577`

**Output**
```json
{
  "summary": "ESLint react-hooks rule incorrectly flags optional chaining usage in dependency arrays.",
  "type": "bug",
  "priority_score": "3 - Causes developer confusion but has a workaround.",
  "suggested_labels": ["bug", "eslint", "react-hooks"],
  "potential_impact": "May slow adoption of React Compiler optimizations."
}
```

---

##  Design Notes

- LLM layer is **provider-agnostic**
- Clean separation of UI, API, and AI logic
- Handles issues with missing comments
- Built with speed, clarity, and maintainability in mind

---

##  Future Improvements

- Copy JSON button
- Response caching
- Private repo support
- Enhanced UI formatting

---

##  Author

**Udaykumar G**  
B.Tech – Computer Science Engineering (AI & ML)  
Ballari Institute of Technology and Management

---

##  Note

This project demonstrates AI-native full-stack engineering, focusing on practical problem-solving, clean architecture, and rapid delivery.
