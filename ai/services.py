import google.generativeai as genai
from django.conf import settings
import os
from PIL import Image
import pytesseract
import fitz  # PyMuPDF

class AIService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        # Set tesseract path for Windows
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def extract_text_from_document(self, file_path):
        """Extract text from various document types using file extension."""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
            # Handle image files using OCR
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
        elif ext == '.pdf':
            # Handle PDF files using PyMuPDF
            text = ""
            with fitz.open(file_path) as pdf:
                for page in pdf:
                    text += page.get_text()
        else:
            # Handle text files
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

        return text

    def answer_question(self, question, document_content):
        """Answer questions based on document content using Gemini."""
        prompt = f"""Based on the following document content, please answer the question.\n        Document content: {document_content}\n        Question: {question}\n        Please provide a clear and concise answer based only on the information in the document."""

        response = self.model.generate_content(prompt)
        return response.text 