"""
Resume Similarity Calculator
"""

from sklearn.metrics.pairwise import cosine_similarity


class SimilarityCalculator:

    def calculate(self, resume_embedding, jd_embedding):

        score = cosine_similarity(
            [resume_embedding],
            [jd_embedding]
        )[0][0]

        return round(score * 100, 2)