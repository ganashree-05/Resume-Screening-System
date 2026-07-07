"""
DOCX Resume Parser
Extracts text from Microsoft Word (.docx) resumes.
"""

from docx import Document


class DOCXParser:
    """Class to parse DOCX resumes."""

    def __init__(self):
        pass

    def extract_text(self, docx_path):
        """
        Extract text from a DOCX file.

        Args:
            docx_path (str): Path to the DOCX file.

        Returns:
            str: Extracted text.
        """

        text = ""

        try:
            document = Document(docx_path)

            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"

        except Exception as e:
            print(f"[ERROR] Unable to read DOCX: {docx_path}")
            print(e)

        return text


if __name__ == "__main__":

    parser = DOCXParser()

    file_path = input("Enter DOCX file path: ")

    extracted_text = parser.extract_text(file_path)

    print("\n===== Extracted Resume Text =====\n")
    print(extracted_text)