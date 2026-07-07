import os

from flask import Flask, render_template, request, send_file

from models.ranking_model import CandidateRanker

app = Flask(__name__)

print("APP.PY LOADED")

# ===========================
# Folder Configuration
# ===========================

UPLOAD_FOLDER = "uploads"
JD_FOLDER = os.path.join(UPLOAD_FOLDER, "jd")
RESUME_FOLDER = os.path.join(UPLOAD_FOLDER, "resumes")
OUTPUT_FOLDER = "data/output"

os.makedirs(JD_FOLDER, exist_ok=True)
os.makedirs(RESUME_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ===========================
# Home Page
# ===========================

@app.route("/")
def home():
    return render_template("index.html")


# ===========================
# Rank Candidates
# ===========================

@app.route("/rank", methods=["POST"])
def rank():
    print("RANK BUTTON CLICKED")
    # --------------------------
    # Save Job Description
    # --------------------------

    jd_file = request.files["job_description"]

    jd_path = os.path.join(
        JD_FOLDER,
        jd_file.filename
    )

    jd_file.save(jd_path)

    # --------------------------
    # Delete Previous Resumes
    # --------------------------

    for file in os.listdir(RESUME_FOLDER):

        file_path = os.path.join(
            RESUME_FOLDER,
            file
        )

        if os.path.isfile(file_path):
            os.remove(file_path)

    # --------------------------
    # Save Uploaded Resumes
    # --------------------------

    resumes = request.files.getlist("resumes")

    for resume in resumes:

        resume.save(
            os.path.join(
                RESUME_FOLDER,
                resume.filename
            )
        )

    # --------------------------
    # Read Job Description
    # --------------------------

    from parser.resume_parser import ResumeParser

    parser = ResumeParser()

    job_description = parser.extract_resume_text(jd_path)

    # --------------------------
    # AI Ranking
    # --------------------------

    ranker = CandidateRanker()

    print("=" * 50)
    print("Job Description Length:", len(job_description))
    print("Resume Folder:", RESUME_FOLDER)
    print("Files:", os.listdir(RESUME_FOLDER))
    print("=" * 50)

    df = ranker.rank_candidates(
        RESUME_FOLDER,
        job_description
    )

    # --------------------------
    # Save Results
    # --------------------------

    csv_path = os.path.join(
        OUTPUT_FOLDER,
        "ranking.csv"
    )

    json_path = os.path.join(
        OUTPUT_FOLDER,
        "ranking.json"
    )

    df.to_csv(
        csv_path,
        index=False
    )

    df.to_json(
        json_path,
        orient="records",
        indent=4
    )

    # --------------------------
    # Display Results
    # --------------------------

    return render_template(
        "result.html",
        results=df.to_dict(
            orient="records"
        )
    )


# ===========================
# Download CSV
# ===========================

@app.route("/download/csv")
def download_csv():

    return send_file(
        os.path.join(
            OUTPUT_FOLDER,
            "ranking.csv"
        ),
        as_attachment=True
    )


# ===========================
# Download JSON
# ===========================

@app.route("/download/json")
def download_json():

    return send_file(
        os.path.join(
            OUTPUT_FOLDER,
            "ranking.json"
        ),
        as_attachment=True
    )


# ===========================
# Run Application
# ===========================

if __name__ == "__main__":

    app.run(
        debug=True
    )