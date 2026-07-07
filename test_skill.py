from parser.resume_parser import ResumeParser
from preprocessing.clean_text import TextCleaner
from preprocessing.skill_extractor import SkillExtractor

resume = ResumeParser()
cleaner = TextCleaner()
skills = SkillExtractor()

resume_path = r"C:\Users\windows\Downloads\Rooman\data\resumes\GanashreeCN_Resume.pdf"

text = resume.extract_resume_text(resume_path)

cleaned = cleaner.clean(text)

detected = skills.extract(cleaned)

print("\nDetected Skills:\n")

for skill in detected:
    print("✓", skill)