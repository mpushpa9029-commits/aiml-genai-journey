# Day 26 - PDF Text Extraction

from PyPDF2 import PdfReader


pdf_path = "day26/sample.pdf"


reader = PdfReader(pdf_path)

print("----- PDF INFORMATION -----")
print("Number of pages:", len(reader.pages))


print("\n----- PDF TEXT -----")

for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text()

    print(f"\n--- Page {page_number} ---")

    if text:
        print(text)
    else:
        print("No text found on this page.")