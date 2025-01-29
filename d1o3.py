import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text):
    if not os.path.exists('PDF_INVOICE'):
        os.makedirs('PDF_INVOICE')
    
    pdf_path = 'PDF_INVOICE/output.pdf'

    c = canvas.Canvas(pdf_path, pagesize=letter)

    c.setFont("Helvetica", 12)
    
    c.drawString(100, 750, text)
    
    c.save()

    print(f"PDF succesvol gegenereerd en opgeslagen als: {pdf_path}")

user_input = input("Voer de tekst in voor de PDF: ")

generate_pdf(user_input)