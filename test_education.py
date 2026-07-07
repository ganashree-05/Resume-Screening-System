from parser.resume_parser import ResumeParser
from preprocessing.clean_text import TextCleaner
from preprocessing.education_extractor import EducationExtractor

resume = ResumeParser()
cleaner = TextCleaner()
education = EducationExtractor()

resume_path = r"C:\Users\windows\Downloads\Rooman\data\resumes\GanashreeCN_Resume.pdf"

text = resume.extract_resume_text(resume_path)

cleaned = cleaner.clean(text)

degrees = education.extract(cleaned)

print("\nEducation Found:\n")

for degree in degrees:
    print("✓", degree)