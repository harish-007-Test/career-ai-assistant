# main.py

from pathlib import Path

from job_loader import load_jobs

from job_analyzer import analyze_job

from ranking_engine import (
    extract_score,
    extract_ats_score,
    rank_jobs
)

from report_generator import generate_report

from resume_generator import generate_resume

from cover_letter_generator import (
    generate_cover_letter
)

from doc_generator import markdown_to_docx

from config import (
    OUTPUT_RESUME_FOLDER,
    COVER_LETTER_FOLDER,
    DOC_OUTPUT_FOLDER,
    TOP_N_JOBS
)


def safe_filename(text):

    if not text:
        return "Unknown"

    return (
        str(text)
        .replace("/", "_")
        .replace("\\", "_")
        .replace(" ", "_")
        .replace(":", "_")
        .replace("|", "_")
        .replace(",", "_")
        .replace("*", "_")
        .replace("?", "_")
        .replace('"', "_")
        .replace("<", "_")
        .replace(">", "_")
    )


def main():

    print("\n===================================")
    print(" AI JOB ANALYSIS STARTED ")
    print("===================================\n")

    jobs = load_jobs()

    # Remove empty rows
    jobs = [
        job for job in jobs
        if str(
            job.get(
                "Job Title",
                ""
            )
        ).strip()
    ]

    print(
        f"Total Jobs Loaded: {len(jobs)}\n"
    )

    analyzed_jobs = []

    # ==========================================
    # ANALYZE JOBS
    # ==========================================

    for idx, job in enumerate(
        jobs[:TOP_N_JOBS]
    ):

        print(
            f"Analyzing Job {idx+1}/{TOP_N_JOBS}"
        )

        analysis = analyze_job(job)

        score = extract_score(
            analysis
        )

        ats_score = extract_ats_score(
            analysis
        )

        analyzed_jobs.append({

            "job": job,

            "analysis": analysis,

            "score": score,

            "ats_score": ats_score

        })

        print(
            f"Match Score: {score} | ATS Score: {ats_score}"
        )

    # ==========================================
    # SORT BY SCORE
    # ==========================================

    ranked_jobs = rank_jobs(
        analyzed_jobs
    )

    # ==========================================
    # OUTPUT FOLDERS
    # ==========================================

    Path(
        OUTPUT_RESUME_FOLDER
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    Path(
        COVER_LETTER_FOLDER
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    Path(
        DOC_OUTPUT_FOLDER
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    # ==========================================
    # GENERATE FILES
    # ==========================================

    print(
        "\nGenerating resumes and cover letters...\n"
    )

    for idx, item in enumerate(
        ranked_jobs
    ):

        job = item["job"]

        analysis = item["analysis"]

        company = safe_filename(

            job.get("Company")

            or f"Company_{idx}"

        )

        role = safe_filename(

            job.get("Job Title")

            or f"Role_{idx}"

        )

        file_name = (
            f"{idx+1}_{company}_{role}"
        )

        print(
            f"\nProcessing: {file_name}"
        )

        # ======================================
        # RESUME
        # ======================================

        resume_md = generate_resume(
            job,
            analysis
        )

        resume_md_path = (
            f"{OUTPUT_RESUME_FOLDER}/"
            f"{file_name}_Resume.md"
        )

        with open(
            resume_md_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                resume_md
            )

        resume_docx_path = (
            f"{DOC_OUTPUT_FOLDER}/"
            f"{file_name}_Resume.docx"
        )

        markdown_to_docx(
            resume_md,
            resume_docx_path
        )

        print(
            "Resume Generated"
        )

        # ======================================
        # COVER LETTER
        # ======================================

        cover_letter = generate_cover_letter(
            job,
            analysis
        )

        cover_letter_md_path = (
            f"{COVER_LETTER_FOLDER}/"
            f"{file_name}_CoverLetter.md"
        )

        with open(
            cover_letter_md_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                cover_letter
            )

        cover_letter_docx_path = (
            f"{DOC_OUTPUT_FOLDER}/"
            f"{file_name}_CoverLetter.docx"
        )

        markdown_to_docx(
            cover_letter,
            cover_letter_docx_path
        )

        print(
            "Cover Letter Generated"
        )

    # ==========================================
    # FINAL REPORT
    # ==========================================

    report_path = generate_report(
        ranked_jobs
    )

    print("\n===================================")

    print(" PIPELINE COMPLETED ")

    print("===================================\n")

    print(
        f"Report Saved:\n{report_path}\n"
    )


if __name__ == "__main__":
    main()