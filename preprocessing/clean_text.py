"""
Text Cleaning Module
Prepares resume text for NLP processing.
"""

import re


class TextCleaner:

    def __init__(self):
        pass

    def clean(self, text: str) -> str:
        """
        Clean extracted resume text.

        Steps:
        1. Convert to lowercase
        2. Remove URLs
        3. Remove email addresses
        4. Remove phone numbers
        5. Remove special characters
        6. Remove extra spaces
        """

        if not text:
            return ""

        # Lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"http\S+|www\S+", " ", text)

        # Remove email addresses
        text = re.sub(r"\S+@\S+", " ", text)

        # Remove phone numbers
        text = re.sub(r"\+?\d[\d\s\-]{8,}\d", " ", text)

        # Keep only letters and numbers
        text = re.sub(r"[^a-z0-9\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()


if __name__ == "__main__":

    sample = """
    Name: John Doe
    Email: john@gmail.com
    Phone: 9876543210
    Skills: Python, Java, SQL
    https://linkedin.com/in/johndoe
    """

    cleaner = TextCleaner()

    print(cleaner.clean(sample))