"""
Universal Resume Parser
Supports PDF, DOCX, and TXT resumes.
"""

import os

from parser.pdf_parser import PDFParser
from parser.docx_parser import DOCXParser


class ResumeParser:

    def __init__(self):
        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()

    def extract_resume_text(self, file_path):
        """
        Detect file type and extract text.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self.pdf_parser.extract_text(file_path)

        elif extension == ".docx":
            return self.docx_parser.extract_text(file_path)

        elif extension == ".txt":
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        else:
            raise ValueError(
                "Unsupported file type. Only PDF, DOCX, and TXT are supported."
            )


if __name__ == "__main__":

    parser = ResumeParser()

    file_path = input("Enter resume path: ")

    try:
        text = parser.extract_resume_text(file_path)

        print("\n==============================")
        print("Extracted Resume")
        print("==============================\n")

        print(text)

    except Exception as e:
        print(e)