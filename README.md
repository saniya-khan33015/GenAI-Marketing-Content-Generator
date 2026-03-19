# 🚀 GenAI Marketing Content Generator

## 📌 Overview
The GenAI Marketing Content Generator is a web-based application that uses OpenAI's ChatGPT API to automatically generate marketing content such as social media posts, advertisements, emails, and product descriptions.

This tool helps users create high-quality, engaging, and customized content quickly by providing simple inputs like topic, tone, and content type.

---

## 🎯 Features
- AI-powered content generation using ChatGPT API
- User-friendly interface (Streamlit)
- Supports multiple content types (ads, captions, emails, blogs)
- Prompt engineering for better output
- Retrieval-Augmented Generation using FAISS
- Save and download generated content

---

## 🏗️ Tech Stack
- Frontend: Streamlit
- Backend: Python
- AI Model: OpenAI ChatGPT API
- Vector Database: FAISS
- Libraries: LangChain, OpenAI, Streamlit

---

## ⚙️ System Architecture
User → Streamlit UI → Prompt Engineering → FAISS → ChatGPT API → Output → Save/Download

---

## 📂 Project Structure
```
project/
│── app.py
│── prompt_engine.py
│── llm_handler.py
│── vector_db.py
│── output_handler.py
│── requirements.txt
│── README.md
```

---

## 🚀 How It Works
1. User enters input (topic, tone, content type)
2. Input is processed through Streamlit UI
3. Prompt is generated using prompt engineering
4. Relevant data is retrieved from FAISS
5. Final prompt is sent to ChatGPT API
6. AI generates content
7. Output is displayed and can be downloaded

---

## 🔑 API Used
- OpenAI ChatGPT API (for content generation)
---

## 📌 Future Enhancements
- Multi-language support
- Voice input
- Content analytics
- Image generation integration

