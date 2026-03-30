# 🧠 AI Text Summarizer Web App

An AI-powered web application that generates concise summaries from long text using **Natural Language Processing (NLP)** and **Hugging Face Transformer models**.

---

## 🚀 Overview

This project focuses on automatic text summarization, a key task in NLP.
It takes large input text and produces a shorter version while preserving the important information.

---

## ✨ Features

* 📄 Summarizes long paragraphs instantly
* 🤖 Uses pretrained transformer models (Hugging Face)
* ⚡ Fast and efficient processing
* 🧾 Simple and clean interface
* 🔍 Maintains key information from input text

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Transformers, Torch
* **AI Model:** Hugging Face (T5-Small)
* **Frontend:** HTML / CSS

---

## 📂 Project Structure

```
text-summarizer-webapp/
│
├── app.py / main.py        # Main application logic
├── templates/             # HTML files
├── static/                # CSS / assets 
└── README.md
```

## 🧠 How It Works

1. User enters input text
2. Text is preprocessed
3. Tokenizer converts text → token IDs
4. Transformer model generates summary
5. Output tokens are decoded into human-readable text

---

## 🧪 Example

**Input:**

> Artificial Intelligence has transformed modern technology by enabling machines to perform human-like tasks.

**Output:**

> AI enables machines to perform human-like tasks.

---

## ⚠️ Limitations

* May miss subtle context
* Output depends on model quality
* Long inputs may be truncated

---

## 🔮 Future Improvements

* 🔹 Add multiple model options (T5, BART)
* 🔹 Improve UI/UX
* 🔹 Add file upload support
* 🔹 Deploy as a live web app

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests!

---

## 📜 License

This project is open-source under the MIT License.

---

## 👨‍💻 Author

**Ajith Reddy**
GitHub: https://github.com/ajithreddy3

---

⭐ Star this repo if you found it useful!
