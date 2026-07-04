from utils import save_file
from config import REPORT_OUTPUT


def generate_report(job_reports):

    content = "# Daily AI Job Report\n\n"

    content += """
# Executive Summary

Generated from current job market analysis.

---

# Top 20 Ranked Jobs

"""

    for idx, item in enumerate(job_reports):

        job = item["job"]

        analysis = item["analysis"]

        score = item["score"]

        title = job.get(
            "Job Title",
            "Not Available"
        )

        company = job.get(
            "Company",
            "Not Available"
        )

        location = job.get(
            "Location",
            "Not Available"
        )

        experience = job.get(
            "Experience",
            "Not Available"
        )

        salary = job.get(
            "Salary",
            "Not Available"
        )

        apply_link = job.get(
            "Link",
            "Not Available"
        )

        work_type = "Not Specified"

        location_lower = str(location).lower()

        if "remote" in location_lower:
            work_type = "Remote"

        elif "hybrid" in location_lower:
            work_type = "Hybrid"

        elif "onsite" in location_lower:
            work_type = "Onsite"

        content += f"""
# Rank {idx+1}

### Job Title
{title}

### Company
{company}

### Match Score
{score}/10

### Experience Match
{experience}

### Salary Information
{salary}

### Work Type
{work_type}

### Location
{location}

### Apply Link
{apply_link}

---

{analysis}

---

"""

    save_file(
        REPORT_OUTPUT,
        content
    )

    return REPORT_OUTPUT