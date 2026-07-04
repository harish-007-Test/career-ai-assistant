import pandas as pd

from utils import (
    read_file,
    read_markdown_folder
)

from llm import generate_response

from config import (
    CSV_PATH,
    RESUME_FOLDER,
    RULES_FOLDER,
    SKILLS_FOLDER,
    PROMPTS_FOLDER,
    TEMPLATE_FOLDER,
    LEARNING_FOLDER,
    REPORT_TEMPLATE_FILE
)

def load_jobs():

    return pd.read_csv(CSV_PATH)

def build_prompt(job_data):

    resume_content = read_markdown_folder(
        RESUME_FOLDER
    )

    rules_content = read_markdown_folder(
        RULES_FOLDER
    )

    skills_content = read_markdown_folder(
        SKILLS_FOLDER
    )

    prompts_content = read_markdown_folder(
        PROMPTS_FOLDER
    )

    template_content = read_markdown_folder(
        TEMPLATE_FOLDER
    )

    learning_content = read_markdown_folder(
        LEARNING_FOLDER
    )

    report_template = read_file(
        REPORT_TEMPLATE_FILE
    )

    prompt = f"""
You are an advanced AI Career Assistant.

You specialize in:
- QA Automation
- Selenium
- API Testing
- Appium
- ATS Optimization
- Resume Tailoring
- Job Ranking
- Technical Interview Preparation

==================================================
RESUME KNOWLEDGE
==================================================

{resume_content}

==================================================
RULES
==================================================

{rules_content}

==================================================
SKILLS
==================================================

{skills_content}

==================================================
PROMPTS
==================================================

{prompts_content}

==================================================
TEMPLATES
==================================================

{template_content}

==================================================
LEARNING CONTEXT
==================================================

{learning_content}

==================================================
REPORT TEMPLATE
==================================================

{report_template}

==================================================
JOB DATA
==================================================

{job_data}

==================================================
TASK
==================================================

Analyze all jobs carefully.

Generate:
- Top ranked jobs
- Match scores
- Apply links
- Missing skills
- ATS keyword improvements
- Resume optimization suggestions
- Tailored cover letters
- Interview preparation guidance

Strictly follow the report template structure.

Prioritize:
- Selenium
- API Testing
- Appium
- Automation Testing
- SDET
- QA Automation

Avoid:
- Manual testing only
- Support roles
- Non-automation jobs
"""

    return prompt

def analyze_jobs():

    df = load_jobs()

    # limit initially for stability
    df = df.head(15)

    job_data = df.to_string(index=False)

    prompt = build_prompt(job_data)

    result = generate_response(prompt)

    return result