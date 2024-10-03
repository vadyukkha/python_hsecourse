from PIL import Image

import pytesseract

file_path = "pytesseract/photo.png"

image = Image.open(file_path)

text = pytesseract.image_to_string(image)

with open("pytesseract/result.txt", "w", encoding="utf-8") as file:
    file.write(text)
