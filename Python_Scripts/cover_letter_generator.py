# cover_letter_generator.py

from llm import ask_llm

from utils import (
    read_file,
    read_markdown_folder
)

from config import (
    MASTER_RESUME,
    SKILLS_FOLDER,
    RULES_FOLDER,
    PROMPTS_FOLDER
)

resume_content = read_file(
    MASTER_RESUME
)

skills_content = read_markdown_folder(
    SKILLS_FOLDER
)

rules_content = read_markdown_folder(
    RULES_FOLDER
)

prompts_content = read_markdown_folder(
    PROMPTS_FOLDER
)


def generate_cover_letter(job, analysis):

    prompt = f"""
You are an elite recruiter-focused cover letter writer.

==================================================
MASTER RESUME
==================================================

{resume_content}

==================================================
SKILLS
==================================================

{skills_content}

==================================================
RULES
==================================================

{rules_content}

==================================================
PROMPTS
==================================================

{prompts_content}

==================================================
TARGET JOB
==================================================

{job}

==================================================
JOB ANALYSIS REPORT
==================================================

{analysis}

==================================================
ABSOLUTE TRUTH ENFORCEMENT
==================================================

You are STRICTLY FORBIDDEN from inventing
ANY information not explicitly available
inside MASTER RESUME.

If education details are missing:
DO NOT invent degrees or universities.

NEVER invent:
- fake achievements
- fake metrics
- fake percentages
- fake company names
- fake tools
- fake experience

If information is missing:
DO NOT mention it.

NEVER use:
- [Your Name]
- [Email]
- [Phone]
- placeholders

==================================================
MANDATORY HEADER
==================================================

Cover letter MUST include:
- Full Name
- Email
- Phone
- Address
- Current Date

using ONLY real details from MASTER RESUME.

==================================================
WRITING STYLE
==================================================

- ATS optimized
- recruiter friendly
- concise
- professional
- confident
- realistic

Mention ONLY relevant technologies
already present in MASTER RESUME.

==================================================
OUTPUT FORMAT
==================================================

Return ONLY final cover letter.
"""

    return ask_llm(prompt).strip()