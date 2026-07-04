# resume_generator.py

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


def generate_resume(job, analysis):

    prompt = f"""
You are an elite ATS resume tailoring system.

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
JOB ANALYSIS REPORT
==================================================

{analysis}

==================================================
TARGET JOB
==================================================

{job}

==================================================
ABSOLUTE TRUTH ENFORCEMENT
==================================================

You are STRICTLY FORBIDDEN from inventing
ANY information not explicitly available
inside MASTER RESUME.

If information is missing:
- OMIT IT
- NEVER create placeholders
- NEVER fabricate details

If education details are missing:
DO NOT invent degrees or universities.

DO NOT invent:
- company names
- certifications
- fake projects
- fake achievements
- fake metrics
- fake percentages
- fake education
- fake dates
- fake locations
- fake tools
- fake experience

If LinkedIn/GitHub are unavailable:
DO NOT mention them.

DO NOT output:
- [Your Name]
- [Company Name]
- [Email]
- [Phone]
- placeholder text

==================================================
TAILORING STRATEGY
==================================================

Use JOB ANALYSIS only for:
- ATS keyword optimization
- skill prioritization
- section ordering
- emphasizing relevant existing skills

You MAY:
- improve wording
- improve ATS optimization
- improve formatting
- improve recruiter readability
- strengthen relevant existing experience

You MUST NOT:
- add fake skills
- add fake projects
- add fake certifications
- add fake experience

If a skill is missing:
mention ONLY as:
- currently learning
- foundational knowledge

==================================================
MANDATORY HEADER
==================================================

Resume MUST begin with:

- Full Name
- Email
- Phone
- Address

using ONLY real details from MASTER RESUME.

==================================================
OUTPUT FORMAT
==================================================

Return ONLY the final ATS optimized resume.
"""

    return ask_llm(prompt).strip()