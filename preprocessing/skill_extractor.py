"""
Skill Extractor
Extracts technical skills from resume text.
"""

import re


class SkillExtractor:

    def __init__(self):

        self.skills = [
            "python",
            "java",
            "c",
            "c++",
            "html",
            "css",
            "javascript",
            "react",
            "nodejs",
            "mysql",
            "sqlite",
            "sql",
            "mongodb",
            "flask",
            "django",
            "git",
            "github",
            "machine learning",
            "deep learning",
            "computer vision",
            "nlp",
            "opencv",
            "tensorflow",
            "keras",
            "pytorch",
            "torchvision",
            "numpy",
            "pandas",
            "scikit-learn",
            "cnn",
            "rnn",
            "lstm",
            "transformers",
            "yolo",
            "yolov8",
            "rest api",
            "docker",
            "aws",
            "azure",
            "linux"
        ]

    def extract(self, text):

        found = []

        text = text.lower()

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):
                found.append(skill.title())

        return sorted(list(set(found)))


if __name__ == "__main__":

    sample = """
    Python Java Machine Learning Flask PyTorch SQL HTML CSS
    """

    extractor = SkillExtractor()

    print(extractor.extract(sample))