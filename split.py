# pdf_splitter.py

import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

path = sys.argv[1]
numPagesPDF1 = int(sys.argv[2])

fname = os.path.splitext(os.path.basename(path))[0]

pdf = PdfFileReader(path)
pdf_writer1 = PdfFileWriter()
pdf_writer2 = PdfFileWriter()

for page in range(pdf.getNumPages()):
    if page < numPagesPDF1:
        pdf_writer1.addPage(pdf.getPage(page))
    if page == numPagesPDF1 - 1:
        output_filename = '{}_{}.pdf'.format(
            fname, 1)
        with open(output_filename, 'wb') as out:
            pdf_writer1.write(out)
            print('Created: {}'.format(output_filename))
    if page > numPagesPDF1 - 1:
        pdf_writer2.addPage(pdf.getPage(page))

output_filename = '{}_{}.pdf'.format(fname, 2)
with open(output_filename, 'wb') as out:
    pdf_writer2.write(out)
    print('Created: {}'.format(output_filename))


