import fitz  # PyMuPDF library

def pdf_erase_line(input_pdf, output_pdf, search_text):
    # Open the PDF file
    #TODO: check for file not found err
    doc = fitz.open(input_pdf)
    
    # Initialize a flag to track if any replacements were made
    replaced = False
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_instances = page.search_for(search_text)
        
        # If search_text is found on the page, iterate over found instances
        if text_instances:
            replaced = True
            for inst in reversed(text_instances):  # Reverse to avoid affecting index after modification
                # Calculate rectangle to redraw over the text instance
                x0, y0, x1, y1 = inst[:4]
                #rect = fitz.Rect(0, y0, page.bound().x1, y1) 
                rect = fitz.Rect(0, y0, x1, y1)

                # Redraw the rectangle
                page.add_redact_annot(rect)
                page.apply_redactions()
    
    # Save the modified PDF to a new file
    doc.save(output_pdf)
    doc.close()
    
    if replaced:
        print(f"Text '{search_text}' found and replaced in '{input_pdf}'.")
    else:
        print(f"Text '{search_text}' not found in '{input_pdf}'.")
