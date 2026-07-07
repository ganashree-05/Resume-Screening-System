from parser.resume_parser import ResumeParser
from preprocessing.clean_text import TextCleaner
from models.embedding_model import EmbeddingModel
from models.similarity import SimilarityCalculator

# Read Resume
resume = ResumeParser()
cleaner = TextCleaner()

resume_text = resume.extract_resume_text(
    r"C:\Users\windows\Downloads\Rooman\data\resumes\GanashreeCN_Resume.pdf"
)

resume_text = cleaner.clean(resume_text)

# Read JD
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd = file.read()

jd = cleaner.clean(jd)

# Load AI Model
model = EmbeddingModel()

resume_vector = model.encode(resume_text)
jd_vector = model.encode(jd)

similarity = SimilarityCalculator()

score = similarity.calculate(
    resume_vector,
    jd_vector
)

print("\nResume Match Score")
print("===================")
print(score, "%")