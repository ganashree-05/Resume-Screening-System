from parser.resume_parser import ResumeParser
from preprocessing.clean_text import TextCleaner

resume_parser = ResumeParser()
cleaner = TextCleaner()

resume_path = r"C:\Users\windows\Downloads\Rooman\data\resumes\GanashreeCN_Resume.pdf"

text = resume_parser.extract_resume_text(resume_path)

cleaned_text = cleaner.clean(text)

print("\n===== CLEANED RESUME =====\n")
print(cleaned_text)