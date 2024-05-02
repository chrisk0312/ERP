from PyPDF2 import PdfReader
import os
import pickle

# Function to load PDF, split, embed, store, and retrieve text
def process_pdf(pdf_path):
    # Load PDF
    pdf = PdfReader(pdf_path)
    
    # Split, embed, and store text content of each page
    embedded_texts = []
    for page in pdf.pages:
        text = page.extract_text()
        embedded_texts.append(text)
    
    # Store embedded text content
    with open('embedded_texts.pkl', 'wb') as f:
        pickle.dump(embedded_texts, f)
    
    # Retrieve embedded text content when asked a question
    def chatbot(question):
        with open('embedded_texts.pkl', 'rb') as f:
            embedded_texts = pickle.load(f)
        for text in embedded_texts:
            if question in text:
                return text.split(".")[0] + "."
        return "Sorry, I couldn't find any information related to your question."
    
    return chatbot

# Example usage
if __name__ == "__main__":
    pdf_path = "C:\\study\\ERP_chatbot\\thesis1.pdf"
    chatbot = process_pdf(pdf_path)
    
    # Test the chatbot
    question = input("Ask a question about the PDF: ")
    answer = chatbot(question)
    print(answer)