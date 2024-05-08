from pdfrw import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

def add_text_to_pdf(input_pdf_path, output_pdf_path, text):
    # Create a new PDF with Reportlab
    c = canvas.Canvas('temp.pdf')
    c.drawString(100, 750, text)
    c.save()

    # Read the original PDF
    original_pdf = PdfReader(input_pdf_path)

    # Read the new PDF
    new_pdf = PdfReader('temp.pdf')

    # Add the page from the new PDF to the original PDF
    original_pdf.pages.append(new_pdf.pages[0])

    # Write the result to a new PDF
    PdfWriter().write(output_pdf_path, original_pdf)

# Usage:
add_text_to_pdf('thesis1.pdf', 'thesis1_with_text.pdf', 'This is a test.')