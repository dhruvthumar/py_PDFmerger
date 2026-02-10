# PDF Merger Application

This is a simple PDF Merger application built using Python and Tkinter.

    Features:
        - Select multiple PDF files to merge.
        - Choose the output location and filename for the merged PDF.

    How to Use:
        1. Run the application.
        2. Click the "Merge PDFs" button.
        3. Select the PDF files you want to merge.
        4. Choose the location and name for the merged PDF file.
        5. Click "Save" to complete the merging process.

    Requirements:
        - Python 3.x
        - PyPDF2 library
        - Tkinter library (usually included with Python)

    Installation:
        1. Install Python 3.x from the official website: https://www.python.org/downloads/
        2. Install the required libraries using pip:
            ```
            pip install PyPDF2
            ```
        3. Run the application:
            ```
            python pM.py
            ```

    Creating an Executable:
        To create an executable file from this script using PyInstaller, run the following command in your terminal or command prompt:
        ```pyinstaller --onefile --windowed pM.py```
        This command will generate a single executable file without a console window. The resulting executable will be found in the "dist" directory created by PyInstaller.

    License: 
        This project is licensed under the MIT License - see the LICENSE file for details.

