# AI Career Assistant

An AI-powered Career Assistant built using **Python**, **Ollama**, and **Qwen3:14B** that automatically analyzes job postings, ranks them based on resume compatibility, generates tailored resumes, creates personalized cover letters, and produces a complete job analysis report.

---

# Features

- Analyze multiple job postings automatically
- Calculate Match Score for every job
- Calculate ATS Score
- Rank jobs by suitability
- Generate AI-tailored resumes
- Generate personalized cover letters
- Produce a detailed Job Report
- Export Resume and Cover Letter to DOCX
- Works completely offline using Ollama
- No OpenAI API required

---

# Technologies Used

- Python 3.13
- Ollama
- Qwen3:14B
- pandas
- requests
- python-docx
- pathlib

---

# Project Structure

```
CareerAssistant
│
├── Apify_Exports
│   └── Naukri_job.csv
│
├── Resume_Master
│   └── Resume_Master.md
│
├── Rules
│   └── Job_Rules.md
│
├── Skills
│   ├── Selenium.md
│   ├── API_Testing.md
│   ├── Appium.md
│   └── AI_Learning.md
│
├── Prompts
│   ├── Resume_Tailoring_Prompt.md
│   ├── Cover_Letter_Prompt.md
│   └── Job_Ranking_Prompt.md
│
├── Templates
│
├── Output_Resume
│
├── Cover_Letters
│
├── Generated_DOCX
│
├── Job_Reports
│
└── Python_Scripts
    ├── main.py
    ├── config.py
    ├── llm.py
    ├── job_loader.py
    ├── job_analyzer.py
    ├── ranking_engine.py
    ├── resume_generator.py
    ├── cover_letter_generator.py
    ├── report_generator.py
    ├── doc_generator.py
    └── utils.py
```

---

# Workflow

```
CSV Jobs
      │
      ▼
Load Jobs
      │
      ▼
Analyze Every Job
      │
      ▼
Generate

• Match Score
• ATS Score
• Missing Skills
• Resume Suggestions
• Interview Preparation
      │
      ▼
Rank Jobs
      │
      ▼
Generate

20 Tailored Resumes

20 Tailored Cover Letters

1 Job Report
      │
      ▼
Convert Markdown
      │
      ▼
DOCX Files
```

---

# How It Works

## Step 1

Load jobs from

```
Apify_Exports/Naukri_job.csv
```

---

## Step 2

For every job the AI:

- reads the Master Resume
- compares it with the Job Description
- calculates

- Match Score
- ATS Score

- identifies

- strengths
- missing skills
- ATS keywords
- interview preparation
- resume improvements

---

## Step 3

Jobs are ranked according to

- Match Score
- ATS Score

---

## Step 4

For every ranked job the system generates

- Tailored Resume (.md)
- Tailored Resume (.docx)

- Tailored Cover Letter (.md)
- Tailored Cover Letter (.docx)

---

## Step 5

Generate a Job Report containing

- Company Name
- Job Title
- Location
- Experience
- Salary
- Apply Link
- Match Score
- ATS Score
- Missing Skills
- Resume Suggestions
- Interview Preparation
- Career Alignment
- Final Recommendation

---

# Configuration

Configuration is managed in

```
config.py
```

Example

```python
MODEL = "qwen3:14b"

TOP_N_JOBS = 20

CSV_PATH = "../Apify_Exports/Naukri_job.csv"

MASTER_RESUME = "../Resume_Master/Resume_Master.md"
```

---

# Running the Project

## Start Ollama

```
ollama serve
```

---

## Activate Virtual Environment

```
source .venv/bin/activate
```

---

## Run

```
python main.py
```

---

# Generated Outputs

## Job Reports

```
Job_Reports/

report_2026-06-10_09-58.md
```

---

## Resumes

```
Output_Resume/

Company_Resume.md
```

---

## Cover Letters

```
Cover_Letters/

Company_CoverLetter.md
```

---

## DOCX Files

```
Generated_DOCX/

Resume.docx

CoverLetter.docx
```

---

# AI Model

The project uses

```
Ollama

↓

Qwen3:14B
```

Completely offline.

No cloud API required.

---

# Current Capabilities

✔ Analyze multiple jobs

✔ Calculate Match Score

✔ Calculate ATS Score

✔ Rank jobs automatically

✔ Generate tailored resumes

✔ Generate tailored cover letters

✔ Generate professional Job Reports

✔ Convert Markdown to DOCX

✔ Offline LLM support

✔ Uses only information available in the Master Resume

✔ Prevents fabrication of fake projects, experience, education, or certifications

---

# Example Output

For every analyzed job the system provides:

- Match Score
- ATS Score
- Strong Matching Skills
- Missing Skills
- Resume Improvements
- ATS Keywords
- Interview Questions
- Career Alignment
- Final Recommendation
- Apply Link

---

# Future Enhancements

- PDF Resume Generation
- AI Resume Scoring
- LinkedIn Profile Optimization
- Company Research
- Interview Question Generator
- Email Application Generator
- Multi-Resume Support
- AI Learning Dashboard
- Job Tracker Dashboard
- Desktop GUI Application
- AI Agent Automation
- Automatic Daily Job Monitoring

---

# Author

**Harish Kumar Gautam**

QA Automation Engineer

Career Assistant Project

Built using Python, Ollama and Qwen3:14B.
