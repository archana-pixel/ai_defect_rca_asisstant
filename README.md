# 🤖 AI Defect RCA Assistant

**AI-Powered Root Cause Analysis (RCA) System using RAG Architecture**

This project is an AI-driven system that automatically generates structured Root Cause Analysis (RCA) for software defects. It leverages a **Retrieval-Augmented Generation (RAG)** pipeline with OpenAI embeddings, vector similarity search, and LLM-based reasoning to provide:

- Root Cause
- Impact
- Suggested Fix
- 5-Why Analysis

The system also provides a **Streamlit UI** for easy input of failure logs and visualization of AI-generated RCA. Optional Jira integration allows automatic updates to issue tickets.

---

## 🏗 Architecture

The system follows a modular RAG architecture:
[User Failure Log]
↓
[Embedding Service] → Generates vector representation
↓
[Vector Store] → Retrieves similar historical defects
↓
[Context Builder] → Prepares input context for LLM
↓
[LLM Service] → Generates structured RCA with 5-Why analysis
↓
[Structured RCA Output] → Display in Streamlit UI (or update Jira)

You can also see the diagram in `architecture.png`.

---

## 🚀 Features

- Embedding-based retrieval of similar defect logs
- AI-powered structured RCA generation
- 5-Why analysis for deeper root cause insights
- Optional Jira API integration for automated issue updates
- Cost tracking for AI API usage
- Streamlit interactive interface
- Modular architecture for future scalability

---

## 🛠 Tech Stack

- **Python** – Core logic
- **OpenAI API** – Embeddings and LLM completions
- **Vector Store** – In-memory or persistent FAISS/Pinecone
- **Streamlit** – Web interface
- **Jira REST API** – Optional automation integration
- **dotenv** – Environment variable management

---

## 📦 Project Structure
ai-defect-rca-assistant/
│
├── app/
│ ├── init.py
│ ├── rca_engine.py
│ ├── embedding_service.py
│ ├── vector_store.py
│ └── llm_service.py
│
├── app.py # Streamlit app
├── requirements.txt
├── .env.example # Example environment variables
├── README.md
├── architecture.png # RAG architecture diagram
└── demo.png # Optional UI screenshot


---

## ▶ Running the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Configure environment variables

Create a .env file based on .env.example:

OPENAI_API_KEY=your_openai_key
JIRA_URL=https://yourcompany.atlassian.net
JIRA_EMAIL=your_email
JIRA_API_TOKEN=your_token

Note: Jira integration is optional. The project works fully without it.

3️⃣ Launch the Streamlit app
streamlit run app.py

Enter failure log in the text area

Click Analyze Failure to generate AI RCA

Optional: Enter Jira issue key and click Generate RCA & Update Jira to push results

🎯 Future Enhancements

Persistent vector database (FAISS / Pinecone) for historical defects

Webhook-based Jira auto-trigger

RCA analytics dashboard with metrics

AI quality scoring for RCA suggestions

Prompt injection protection for enterprise usage

👩‍💻 Author

Archana V
AI-Driven QA & Automation Engineer
GitHub