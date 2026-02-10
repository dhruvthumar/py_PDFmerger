
# This code creates a simple GUI application using Tkinter that allows users 
#        to select multiple PDF files and merge them into a single PDF file. 
# The user can choose the output location and filename for the merged PDF.

import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfMerger

def merge_pdfs():
    pdfs = filedialog.askopenfilenames(title="Select PDF files to merge", filetypes=[("PDF files", "*.pdf")])
    
    if not pdfs:
        return
    
    merger = PdfMerger()
    
    for pdf_file in pdfs:
        merger.append(PdfReader(pdf_file))
    
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    
    if save_path:
        merger.write(save_path)
        merger.close()
        tk.messagebox.showinfo("Success", "PDF files merged successfully!")
    else:
        tk.messagebox.showwarning("Cancelled", "Merge cancelled. No file selected to save.")
root = tk.Tk()
root.title("PDF Merger")
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=100, padx=100)
root.mainloop()

# To create an executable file from this script using PyInstaller, 
#     you can run the following command in your terminal or command prompt:
# pyinstaller --onefile --windowed pM.py
# This command will generate a single executable file without a console window. 
#   The resulting executable will be found in the "dist" directory created by PyInstaller.

