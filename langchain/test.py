import PyPDF2 #module to read pdf files
import fitz
import pickle
import os

# Load PDF
pdf_file = open('thesis1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Split PDF into pages
pages = []
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    pages.append(page)

# Embed data into first page
data = {"key": "value"}
pages[0].updatePageContent(data)

# Store pages
with open('pages.pkl', 'wb') as f:
    pickle.dump(pages, f)

# Close the PDF file
pdf_file.close()

# Retrieve pages
with open('pages.pkl', 'rb') as f:
    retrieved_pages = pickle.load(f)

# Print the content of the first page
print(retrieved_pages[0].extractText())