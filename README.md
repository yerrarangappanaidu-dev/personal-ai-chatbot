# Personal AI Chatbot 🤖

A locally running AI chatbot built with Python, Ollama, Gemma 3 1B, and Streamlit.

## Features

- Chat with a locally running AI model.
- Use a browser-based chat interface.
- Maintain conversation history during the current session.
- Guide responses using a system prompt.
- Clear the conversation with a button.
- Handle errors when the AI cannot respond.

## Technologies Used

- Python
- Ollama
- Gemma 3 1B
- Streamlit

## Requirements

- Python
- Ollama
- Gemma 3 1B model

## Installation and Setup

### 1. Download the AI model

Install Ollama, open a terminal, and run:

```bash
ollama pull gemma3:1b
```

### 2. Install Python dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install -r requirements.txt
```

### 3. Start the chatbot

Run:

```bash
python -m streamlit run app.py
```

Open this URL in your browser:

http://localhost:8501

## How It Works

1. The user enters a message in the Streamlit interface.
2. Python sends the conversation to Ollama.
3. Ollama runs the Gemma 3 1B model.
4. The model generates a response.
5. Streamlit displays the response.

## Project Files

- `app.py` — Web-based chatbot interface.
- `chatbot.py` — Terminal chatbot.
- `test_connection.py` — Python–Ollama connection test.
- `requirements.txt` — Python package dependencies.
- `README.md` — Project documentation.

## Future Improvements

- Add RAG for answering questions from PDF documents.
- Add document upload and search.
- Add automated tests.
- Add AI agent tools.

## Learning Objective

This project demonstrates Python programming, local LLM integration, prompt design, and AI application development.
