#MAKE gui to select pdf files and merge them
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

