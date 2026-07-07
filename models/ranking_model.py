"""
Candidate Ranking Model
Ranks multiple resumes based on similarity score.
"""

import os
import pandas as pd

from parser.resume_parser import ResumeParser
from preprocessing.clean_text import TextCleaner
from preprocessing.skill_extractor import SkillExtractor
from models.embedding_model import EmbeddingModel
from models.similarity import SimilarityCalculator


class CandidateRanker:

    def __init__(self):

        self.resume_parser = ResumeParser()
        self.cleaner = TextCleaner()
        self.skill_extractor = SkillExtractor()

        self.embedding = EmbeddingModel()
        self.similarity = SimilarityCalculator()

    def rank_candidates(self, resume_folder, job_description):

        print("=" * 70)
        print("STARTING CANDIDATE RANKING")
        print("=" * 70)

        # ----------------------------
        # Clean Job Description
        # ----------------------------

        jd = self.cleaner.clean(job_description)

        print("\nJob Description Length:", len(jd))

        # ----------------------------
        # Generate JD Embedding
        # ----------------------------

        jd_vector = self.embedding.encode(jd)

        results = []

        # ----------------------------
        # Check Resume Folder
        # ----------------------------

        if not os.path.exists(resume_folder):

            print("Resume folder not found!")

            return pd.DataFrame(
                columns=["Candidate", "Score", "Skills"]
            )

        files = os.listdir(resume_folder)

        print("\nFound Resume Files:")
        print(files)

        # ----------------------------
        # Process Each Resume
        # ----------------------------

        for file in files:

            if not file.lower().endswith((".pdf", ".docx", ".txt")):
                continue

            path = os.path.join(resume_folder, file)

            print("\n" + "=" * 60)
            print("Processing Resume:", file)
            print("=" * 60)

            try:

                # Read Resume

                text = self.resume_parser.extract_resume_text(path)

                if text is None or text.strip() == "":
                    print("Resume is empty.")
                    continue

                print("Resume Text Length:", len(text))

                # Clean Resume

                cleaned = self.cleaner.clean(text)

                print("Cleaned Text Length:", len(cleaned))

                # Extract Skills

                skills = self.skill_extractor.extract(cleaned)

                print("Extracted Skills:", skills)

                # Generate Embedding

                resume_vector = self.embedding.encode(cleaned)

                print("Embedding Generated Successfully")

                # Calculate Similarity

                score = self.similarity.calculate(
                    resume_vector,
                    jd_vector
                )

                score = round(float(score), 2)

                print("Similarity Score:", score)

                # Store Result

                results.append({
                    "Candidate": file,
                    "Score": score,
                    "Skills": ", ".join(skills)
                })

                print("Candidate Added Successfully")

            except Exception as e:

                print("\nERROR while processing:", file)
                print(type(e).__name__)
                print(e)

        print("\n" + "=" * 70)
        print("ALL RESULTS")
        print("=" * 70)

        print(results)

        # ----------------------------
        # Empty Results
        # ----------------------------

        if len(results) == 0:

            print("No candidates were processed.")

            return pd.DataFrame(
                columns=[
                    "Candidate",
                    "Score",
                    "Skills"
                ]
            )

        # ----------------------------
        # DataFrame
        # ----------------------------

        df = pd.DataFrame(results)

        print("\nDataFrame Columns:")
        print(df.columns.tolist())

        print("\nDataFrame:")
        print(df)

        # ----------------------------
        # Sort
        # ----------------------------

        if "Score" in df.columns:

            df = df.sort_values(
                by="Score",
                ascending=False
            )

            df.reset_index(
                drop=True,
                inplace=True
            )

        print("\nFINAL RANKING")
        print(df)

        return df