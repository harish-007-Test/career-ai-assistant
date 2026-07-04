# job_analyzer.py

from llm import ask_llm

from utils import (
    read_file,
    read_markdown_folder
)

from config import (
    MASTER_RESUME,
    RULES_FOLDER,
    SKILLS_FOLDER,
    PROMPTS_FOLDER
)

resume = read_file(MASTER_RESUME)

rules = read_markdown_folder(
    RULES_FOLDER
)

skills = read_markdown_folder(
    SKILLS_FOLDER
)

prompts = read_markdown_folder(
    PROMPTS_FOLDER
)


def analyze_job(job):

    prompt = f"""
You are a Senior QA Automation Career Advisor,
ATS Resume Reviewer,
and AI Career Coach.

==================================================
MASTER RESUME
==================================================

{resume}

==================================================
RULES
==================================================

{rules}

==================================================
SKILLS
==================================================

{skills}

==================================================
PROMPTS
==================================================

{prompts}

==================================================
TARGET JOB
==================================================

{job}

==================================================
CRITICAL TRUTH POLICY
==================================================

You MUST use ONLY:

1. MASTER RESUME
2. TARGET JOB

NEVER invent:

- projects
- companies
- education
- certifications
- experience
- skills
- achievements
- percentages
- responsibilities

If something is missing,
state it as missing.

NEVER fabricate information.

==================================================
ANALYSIS OBJECTIVES
==================================================

Evaluate:

- ATS compatibility
- Technical match
- Career growth
- QA automation alignment
- AI testing alignment
- Salary attractiveness
- Learning opportunity
- Long-term career value

==================================================
MATCH SCORE
==================================================

Calculate realistic score out of 10.

Examples:

Match Score: 8.5
Match Score: 7.2
Match Score: 9.1

==================================================
ATS SCORE
==================================================

Calculate ATS score based on:

- keyword match
- tool match
- framework match
- experience match

Example:

ATS Score: 84%

==================================================
RETURN FORMAT
==================================================

# Job Analysis

## Match Score
Match Score: X.X

## ATS Score
ATS Score: XX%

## Why Strong Match

Explain:

- matching technologies
- matching frameworks
- matching testing experience
- alignment with career goals

## Missing Skills

List only genuine gaps.

## ATS Keywords

Provide keywords found in job description.

## Resume Improvements

ONLY improvements based on existing resume.

DO NOT suggest fake projects.

DO NOT suggest fake experience.

DO NOT suggest fake certifications.

## Tailored Resume Suggestions

Mention:

- existing projects to emphasize
- existing skills to move higher
- existing technologies to highlight

ONLY use real information from resume.

## Interview Preparation

Provide:

- important technical topics
- likely interview questions
- framework discussion areas
- API testing discussion areas
- AI-related preparation

## Career Alignment

Explain alignment with:

- QA Automation
- SDET
- AI Testing
- Python Learning Path

## Final Recommendation

Choose ONLY ONE:

HIGH PRIORITY APPLY

GOOD APPLY

OPTIONAL APPLY

LOW PRIORITY

==================================================
SPECIAL FOCUS
==================================================

Focus heavily on:

- Selenium
- REST Assured
- API Testing
- Appium
- Jenkins
- CI/CD
- Automation Frameworks
- Python Learning
- AI Testing
- LLM Workflows

==================================================
OUTPUT RULES
==================================================

Return ONLY Job Analysis.

No introduction.

No disclaimer.

No markdown code block.
"""

    return ask_llm(prompt).strip()