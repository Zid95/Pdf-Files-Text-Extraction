import PyPDF2

pdf_file_object = open('filename.pdf','rb')

pdf_reader = PyPDF2.PdfReader(pdf_file_object)

print(f'The number of pages in this book is:{len(pdf_reader.pages)} pages')

len_pdffile_pages = len(pdf_reader.pages)
user_input = int(input(f"Please enter a page number from 1 to {len_pdffile_pages}: ").strip())

if user_input > len_pdffile_pages:
    print(f"Out of range! Please enter a page number from 1 to {len_pdffile_pages}")

else:
    page_object = pdf_reader.pages[user_input]
    print(page_object.extract_text())

pdf_file_object.close()