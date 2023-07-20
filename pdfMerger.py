import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    # Check if PDF
    if file.endswith(".pdf"):
        merger.append(file)
# Creates combined file
merger.write("Combined.pdf")

