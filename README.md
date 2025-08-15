# 🚀 AI Projects Collection – NLP, Resume Feedback & Image Classification

This repository contains **three AI-powered applications** built using **Streamlit**, **Google Gemini API**, and other Python libraries.  
Each project demonstrates a different area of AI — **natural language processing**, **resume analysis**, and **computer vision**.

---

## 📂 Projects Overview

### 1️⃣ AI Agent Chat
An interactive AI assistant that uses **Google Gemini API** + **LangChain** to understand user queries and perform tasks with custom tools.

**Features:**
- Streams responses as they are generated.
- Supports custom tools (e.g., number addition).
- Built using `langgraph` and `LangChain`.

---

### 2️⃣ AI Resume Critiquer
Upload a PDF or TXT resume and receive **structured feedback** from an AI career advisor.

**Features:**
- Analyzes resume content and provides:
  - Overall Impression
  - Strengths
  - Weaknesses / Gaps
  - ATS Optimization Suggestions
  - Role-Specific Tips (if provided)
  - Grammar & Formatting Feedback
- Built with **Google Gemini API** & **Streamlit**.

---

### 3️⃣ AI Image Classifier
Classifies uploaded images using **MobileNetV2** pretrained on ImageNet.

**Features:**
- Top-3 predictions with confidence scores.
- Supports `.jpg` and `.png` formats.
- Uses **TensorFlow/Keras**, **OpenCV**, and **PIL**.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – Web app framework
- **Google Gemini API** – LLM-powered intelligence
- **LangChain** – AI agent workflows
- **TensorFlow/Keras** – Deep learning models
- **OpenCV** – Image processing
- **PIL** – Image handling
- **PyPDF2** – PDF text extraction
- **python-dotenv** – Secure API key management

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt
