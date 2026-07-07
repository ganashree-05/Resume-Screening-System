"""
Experience Extractor
Extracts years of experience from resume text.
"""

import re


class ExperienceExtractor:

    def extract(self, text):

        text = text.lower()

        patterns = [
            r'(\d+)\+?\s+years',
            r'(\d+)\+?\s+year',
            r'(\d+)\s+yrs',
            r'(\d+)\s+yr'
        ]

        experience = []

        for pattern in patterns:

            matches = re.findall(pattern, text)

            for match in matches:
                experience.append(int(match))

        if experience:
            return max(experience)

        return 0


if __name__ == "__main__":

    sample = """
    Worked as Software Engineer for 3 years.
    Experience: 5 years.
    """

    extractor = ExperienceExtractor()

    print(extractor.extract(sample))