# WhatsApp Story Bot

This project converts WhatsApp/Inatagram chat screenshots/any url into creative short stories using OCR and AI.

## Features
- Extracts text from WhatsApp chat screenshots (local file or URL)
- Cleans and fixes garbled OCR text
- Generates a story in your chosen tone (Dramatic, Funny, Romantic, Thriller)
- Saves the story to `story.txt`

## How It Works
1. **OCR**: Uses Tesseract to extract text from images
2. **Text Cleaning**: Removes noise and unreadable lines
3. **Story Generation**: Uses Groq LLM to turn chat into a story

## Requirements
- Python 3.8+
- Tesseract OCR (Install from https://github.com/tesseract-ocr/tesseract)
- API key for Groq (set in `.env` as `GROQ_API_KEY`)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Tesseract and set its path in `story_bot.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
3. Add your Groq API key to `.env`:
   ```env
   GROQ_API_KEY=your_key_here
   ```

## Usage
Run the bot:
```bash
python story_bot.py
```
- Enter the image path or URL when prompted
- Choose the story tone
- The generated story will be saved to `story.txt`

## Example
![Example Screenshot](example.png)

## License
MIT License
