# 🤖 FAQ Chatbot

An AI-powered FAQ chatbot built with **Python**, **NLP (TF-IDF + Cosine Similarity)**, and **Streamlit** for real-time question answering. This project allows users to ask questions and get answers from a pre-defined CSV dataset of FAQs.

---

## 📝 Features

* Natural Language Processing with **NLTK**
* FAQ knowledge stored in **CSV dataset**
* **TF-IDF vectorization** for question similarity
* **Cosine similarity** to select the best answer
* Interactive **Streamlit UI**
* Chat history saved during session
* Automatic input clearing after submitting a question
* Lightweight, easy to deploy and extend

---

## 💻 Project Structure

```
codealpha_chatbot_FAQ/
│
├── client/
│   └── app.py                  # Streamlit frontend
│
├── server/
│   ├── __init__.py
│   ├── model.py                # NLP backend and FAQ logic
│   └── dataset/
│         └── faq_dataset.csv   # FAQ knowledge base
│
├── assets/
│   └── chatbot.png             # Project icon / screenshot
│
├── venv/                       # Virtual environment
└── README.md
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd codealpha_chatbot_FAQ
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run client/app.py
```

* Ask a question in the input box
* Press **Enter** or click **Send**
* The bot will answer based on the CSV dataset
* Input box clears automatically for the next question
* Chat history is displayed above the input box

---

## 🖼️ Screenshot

![Chat Screen](./assets/chatbot.png)

---

## 🛠️ Backend Logic

* `server/model.py` handles all NLP operations
* Uses **TF-IDF vectorizer** to encode questions
* **Cosine similarity** finds the most similar question in the dataset
* Returns the corresponding answer to the frontend

---

## ✅ Future Improvements

* Add **ChatGPT-style chat bubbles**
* Fixed bottom input bar
* Typing animation for bot responses
* Dynamic CSV upload to add new FAQs
* Deploy online using **Streamlit Cloud** or **Heroku**

---

## 📄 License

This project is open-source under the MIT License.
