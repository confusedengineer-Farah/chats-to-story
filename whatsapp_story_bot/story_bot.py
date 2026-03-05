import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import requests
from io import BytesIO
from groq import Groq
import re
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(img):
    # Convert to grayscale
    img = img.convert("L")
    # Sharpen the image
    img = img.filter(ImageFilter.SHARPEN)
    # Increase contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    return img

def extract_text_from_image(source):
    if source.startswith("http://") or source.startswith("https://"):
        response = requests.get(source)
        img = Image.open(BytesIO(response.content))
    else:
        img = Image.open(source)
    
    # Preprocess before OCR
    img = preprocess_image(img)
    text = pytesseract.image_to_string(img)
    return text

def clean_text(text):
    # Remove lines that are too short or look like garbage
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        line = line.strip()
        # Keep lines with at least 3 real words
        words = [w for w in line.split() if len(w) > 1]
        if len(words) >= 2:
            cleaned.append(line)
    return "\n".join(cleaned)

def generate_story(chat_text, tone):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": f"""Below is a WhatsApp chat conversation extracted from a screenshot. 
Some words may be slightly garbled due to OCR — please intelligently guess and fix them.

Chat:
{chat_text}

Now turn this into a {tone} short story. 
- Use the sender names as characters
- Make it creative, engaging and fun
- Ignore any unreadable or nonsense words
- Write at least 3 paragraphs"""}
        ]
    )
    return response.choices[0].message.content

# Main
source = input("Enter image path or URL: ")
raw_text = extract_text_from_image(source)
cleaned_text = clean_text(raw_text)

print("\n--- Cleaned Chat Text ---")
print(cleaned_text)

print("\nChoose story tone:")
print("1. Dramatic 🎭")
print("2. Funny 😂")
print("3. Romantic 💕")
print("4. Thriller 😱")
choice = input("Enter 1-4: ")

tones = {"1": "dramatic", "2": "funny", "3": "romantic", "4": "thriller"}
tone = tones.get(choice, "dramatic")

print("\n⏳ Generating your story...")
story = generate_story(cleaned_text, tone)

print("\n--- YOUR STORY ---")
print(story)

with open("story.txt", "w", encoding="utf-8") as f:
    f.write(story)
print("\n✅ Story saved to story.txt!")