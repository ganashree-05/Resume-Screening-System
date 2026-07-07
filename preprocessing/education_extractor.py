"""
Education Extractor
Extracts educational qualifications from resume text.
"""

class EducationExtractor:

    def __init__(self):

        self.degrees = [
            "bachelor",
            "bachelor of engineering",
            "be",
            "b.e",
            "computer science",
            "master",
            "mtech",
            "mca",
            "bca",
            "bsc",
            "msc",
            "phd",
            "diploma",
            "puc",
            "sslc"
        ]

    def extract(self, text):

        text = text.lower()

        found = []

        for degree in self.degrees:

            if degree in text:
                found.append(degree.title())

        return sorted(list(set(found)))


if __name__ == "__main__":

    sample = """
    Bachelor of Engineering in Computer Science
    PUC
    SSLC
    """

    extractor = EducationExtractor()

    print(extractor.extract(sample))