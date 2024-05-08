import PyPDF2
from PyPDF2 import PdfReader
import re
import os
import numpy as np
import sqlite3

# Load PDF
pdf = PdfReader("C:\\study\\ERP_chatbot\\thesis1.pdf")

# Extract text from each page
text = ''
for page in pdf.pages:
    text += page.extract_text()

# Continue with your code...

def load_pdf(file_path):
    """
    Load PDF from file path.
    """
    # Load PDF
    pdf = PdfReader(file_path)

    # Extract text from each page
    text = ''
    for page in pdf.pages:
        text += page.extract_text()

    return text

from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

# Create a new PDF with Reportlab
c = canvas.Canvas("new.pdf")
c.drawString(100, 750, "This is the text I want to add.")
c.save()

# Merge the new PDF with the existing one using PyPDF2
output = PdfWriter()
input1 = PdfReader(open("thesis1.pdf", "rb"))

# Add all pages from the original PDF to the output
for i in range(len(input1.pages)):
    output.add_page(input1.pages[i])

# Add the new page to the output
input2 = PdfReader(open("new.pdf", "rb"))
output.add_page(input2.pages[0])

# Write the output to a file
with open("merged.pdf", "wb") as outputStream:
    output.write(outputStream)
    
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas

def process_command(command, args):
    if command == 'merge':
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
        return "thesis1.pdf"
    else:
        return "I don't understand that command."

# Simulate a chat
while True:
    user_input = input("Enter a command: ")
    command, *args = user_input.split()
    response = process_command(command, args)
    print(response)