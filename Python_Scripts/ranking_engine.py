import re


def extract_score(text):

    match = re.search(
        r"Match Score[:\s]*([0-9]+(?:\.[0-9]+)?)",
        text,
        re.IGNORECASE
    )

    if match:
        return float(match.group(1))

    return 0.0


def extract_ats_score(text):

    match = re.search(
        r"ATS Score[:\s]*([0-9]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return 0


def rank_jobs(jobs):

    return sorted(
        jobs,
        key=lambda x: (
            x["score"],
            x.get("ats_score", 0)
        ),
        reverse=True
    )