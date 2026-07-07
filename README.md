# Resume Screening and Ranking System Using NLP and Machine Learning

## Overview

This project is an AI-powered Resume Screening and Ranking System developed as part of the Rooman Technologies Junior AI Research Associate 24-Hour AI Agent Challenge.

The system automatically parses resumes, extracts relevant information such as skills, education, and experience, compares each resume with a given Job Description (JD) using Natural Language Processing (NLP), and ranks candidates based on their relevance.

---

## Features

- Parse PDF resumes
- Parse DOCX resumes
- Parse TXT resumes
- Clean and preprocess resume text
- Extract technical skills
- Extract education details
- Extract years of experience
- Generate sentence embeddings using Sentence Transformers
- Compare resumes with Job Description using Cosine Similarity
- Rank multiple candidates
- Export results to CSV and JSON

---

## Technologies Used

- Python 3.11
- Sentence Transformers
- PyTorch
- Scikit-learn
- Pandas
- NumPy
- PyPDF2
- python-docx
- spaCy

---

## Project Structure

```
ResumeScreeningSystem/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── resumes/
│   ├── output/
│   └── job_description.txt
│
├── parser/
│   ├── pdf_parser.py
│   ├── docx_parser.py
│   └── resume_parser.py
│
├── preprocessing/
│   ├── clean_text.py
│   ├── skill_extractor.py
│   ├── experience_extractor.py
│   └── education_extractor.py
│
├── models/
│   ├── embedding_model.py
│   ├── similarity.py
│   └── ranking_model.py
│
└── utils/
```

---

## Installation

### Clone the Repository

```bash
git clone <your-github-repository-url>
cd ResumeScreeningSystem
```

### Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

Download the spaCy model

```bash
python -m spacy download en_core_web_sm
```

---

## Input

### Place resumes inside

```
data/resumes/
```

Supported formats

- PDF
- DOCX
- TXT

### Add Job Description

```
data/job_description.txt
```

---

## Run the Project

```bash
python app.py
```

---

## Output

The application generates

```
data/output/ranking.csv
```

and

```
data/output/ranking.json
```

Each record contains

- Candidate Name
- Similarity Score
- Extracted Skills

---

## Scoring Method

The system performs the following steps:

1. Parse resume
2. Extract text
3. Clean text
4. Extract skills
5. Generate sentence embeddings
6. Compare with Job Description using Cosine Similarity
7. Rank candidates based on similarity score

---

## Sample Output

| Candidate | Score | Skills |
|-----------|------:|--------|
| resume1.pdf | 91.34 | Python, Machine Learning, Flask |
| resume2.pdf | 88.25 | Java, SQL, HTML |
| resume3.pdf | 84.72 | Python, OpenCV, Deep Learning |

---

## Example Workflow

```
Resume

↓

Resume Parser

↓

Text Cleaning

↓

Skill Extraction

↓

Sentence Embedding

↓

Cosine Similarity

↓

Candidate Score

↓

Ranking

↓

CSV / JSON Output
```

---

## Future Improvements

- Weighted skill matching
- Experience-based scoring
- Education matching
- Named Entity Recognition (NER)
- OCR support for scanned resumes
- Web interface using Flask
- Database integration
- Explainable AI ranking
- Batch processing with multiprocessing

---

## Limitations

- Works best with text-based PDFs.
- OCR is not implemented for scanned resumes.
- Skill extraction is keyword-based.
- Experience extraction uses simple pattern matching.
- Similarity depends on the quality of the Job Description.

---

## Author

Ganashree C N

Bachelor of Engineering

Computer Science and Engineering

K. S. School of Engineering and Management

---

## License

This project is developed for educational and assessment purposes as part of the Rooman Technologies AI Agent Challenge.