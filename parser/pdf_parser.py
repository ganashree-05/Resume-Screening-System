"""
PDF Resume Parser
Extracts text from PDF resumes using PyPDF2.
"""

from PyPDF2 import PdfReader


class PDFParser:
    """Class to parse PDF resumes."""

    def __init__(self):
        pass

    def extract_text(self, pdf_path):
        """
        Extract text from a PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: Extracted text.
        """

        text = ""

        try:
            reader = PdfReader(pdf_path)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        except Exception as e:
            print(f"[ERROR] Unable to read PDF: {pdf_path}")
            print(e)

        return text


if __name__ == "__main__":

    parser = PDFParser()

    file_path = input("Enter PDF file path: ")

    extracted_text = parser.extract_text(file_path)

    print("\n===== Extracted Resume Text =====\n")
    print(extracted_text)