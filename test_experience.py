from parser.resume_parser import ResumeParser
from preprocessing.clean_text import TextCleaner
from preprocessing.experience_extractor import ExperienceExtractor

resume = ResumeParser()
cleaner = TextCleaner()
experience = ExperienceExtractor()

resume_path = r"C:\Users\windows\Downloads\Rooman\data\resumes\GanashreeCN_Resume.pdf"

text = resume.extract_resume_text(resume_path)

cleaned = cleaner.clean(text)

years = experience.extract(cleaned)

print("\nExperience Found:")
print(years, "Years")