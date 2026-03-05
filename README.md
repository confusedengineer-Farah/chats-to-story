# 📖 Chats to Story — WhatsApp Story Bot

Turn your WhatsApp chat screenshots into creative AI-generated stories! 🤖✨

---

## 🌟 Features

- 📸 **Screenshot Input** — Just paste a URL or local image path
- 🔍 **OCR Text Extraction** — Reads text directly from images using Tesseract
- 🧹 **Smart Text Cleaning** — Filters out garbled OCR noise automatically
- 🤖 **AI Story Generation** — Powered by Groq (LLaMA 3.3) for fast, free generation
- 🎭 **4 Story Tones** — Dramatic, Funny, Romantic, or Thriller
- 💾 **Auto Save** — Story is saved to `story.txt` after generation

---

## 🛠️ Tech Stack

- Python 3.11
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Groq API](https://console.groq.com) (LLaMA 3.3 70B)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/confusedengineer-Farah/chats-to-story.git
cd chats-to-story
```

### 2. Install dependencies
```bash
pip install pytesseract pillow requests groq python-dotenv
```

### 3. Install Tesseract Engine
Download and install from:
👉 https://github.com/UB-Mannheim/tesseract/wiki

Then add to PATH:
```
C:\Program Files\Tesseract-OCR
```

### 4. Setup your API key
Create a `.env` file in the project folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at 👉 https://console.groq.com

### 5. Run the bot
```bash
python story_bot.py
```

---

## 📸 How to Use

1. Export or screenshot a WhatsApp chat
2. Run the bot and enter the image path or URL
3. Choose your story tone (Dramatic, Funny, Romantic, Thriller)
4. Get your AI-generated story instantly!
5. Find the saved story in `story.txt`

---

## ⚠️ Important

- Never commit your `.env` file — it's already in `.gitignore` ✅
- Works best with clear, high-resolution screenshots

---

## 👨‍💻 Author

Made with ❤️ by [confusedengineer-Farah](https://github.com/confusedengineer-Farah)

> *"Don't go fast — build dreams slowly and meaningfully."*