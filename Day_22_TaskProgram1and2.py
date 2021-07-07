from PIL import Image
import PyPDF2
im1 = Image.open(r"C:\\Users\\91882\\Pictures\\Saved Pictures\\SampleImage.jpg")
print("Copied Image.....")
print("Showing image.....")
im2 = im1.copy()
im2.show()
 
def PDFmerge(pdfs, output):
    pdfMerger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        pdfMerger.append(pdf)
    with open(output, 'wb') as f:
        pdfMerger.write(f)
        
pdfs = ['JP LAB SYLLABUS.pdf', 'JP SYLLABUS.pdf']
output = 'combined_pdf.pdf'
print("Reading the PDF.....")
PDFmerge(pdfs=pdfs, output=output)
print("PDF merged succesfully")
 
