import PyPDF2
from PyPDF2 import PdfReader
import re
import os
import numpy as np
import sqlite3
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

def load_pdf(file_path):
    """
    Load PDF from file path.
    """
    # Load PDF
    pdf = PdfReader(file_path)

    # Extract text from each page
    text = ''
    if pdf.pages:
        for page in pdf.pages:
            text += page.extract_text()

    return text

def search_pdf(text, keyword):
    """
    Search PDF text for a specific keyword.
    """
    matches = re.findall(keyword, text, re.IGNORECASE)
    return matches

def process_command(command, args, text):
    if command == 'search':
        keyword = args[0]
        matches = search_pdf(text, keyword)
        if matches:
            return f"Found {len(matches)} matches for '{keyword}'"
        else:
            return f"No matches found for '{keyword}'"
    elif command == 'merge':
        # Merge two PDFs
        output = PdfWriter()
        for filename in args:
            pdf = PdfReader(filename)
            for page in pdf.pages:
                output.add_page(page)
        with open("merged.pdf", "wb") as outputStream:
            output.write(outputStream)
        return "Merged PDFs into merged.pdf"
    elif command == 'add_text':
        # Add text to a PDF
        c = canvas.Canvas("new.pdf")
        c.drawString(100, 750, args[0])
        c.save()
        return "Added text to new.pdf"
    else:
        return "I don't understand that command."

# Load PDF
pdf_text = load_pdf("C:\\study\\ERP_chatbot\\thesis1.pdf")

# Simulate a chat
while True:
    user_input = input("You: ")
    command, *args = user_input.split()
    response = process_command(command, args, pdf_text)
    print("Bot:", response)
