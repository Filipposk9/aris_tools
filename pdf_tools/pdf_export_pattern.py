import re
import PyPDF2
from openpyxl import Workbook

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            temp = page.extract_text()
            text += temp
    return text

# Function to find barcodes in the extracted text
def find_barcodes(text):
    # Regex pattern for barcode: 2 letters followed by digits and ending with 2 letters
    pattern = r'\b(?:UC|LL|RE|CP)\s\d{3}\s\d{3}\s\d{3}\sGR\b'
    barcodes = re.findall(pattern, text)
    barcodes = [barcode.replace(" ", "") for barcode in barcodes]

    #TODO: inform the user with count of barcodes found    	
    
    return barcodes

# Function to export barcodes to an XLSX file
def export_barcodes_to_xlsx(barcodes, output_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Barcodes"

    # Write headers
    sheet.append(["Barcode"])

    # Write barcodes
    for barcode in barcodes:
        sheet.append([barcode])

    # Save the workbook
    workbook.save(output_path)

# Main function to extract barcodes and export them to an XLSX file
def pdf_export_pattern(pdf_path, output_xlsx_path):
    text = extract_text_from_pdf(pdf_path)
    barcodes = find_barcodes(text)
    export_barcodes_to_xlsx(barcodes, output_xlsx_path)
    print(f"Barcodes have been exported to {output_xlsx_path}")
