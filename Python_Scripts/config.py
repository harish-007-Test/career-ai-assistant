# config.py

from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

# ==========================================
# OLLAMA
# ==========================================

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen3:14b"

# ==========================================
# INPUT FILES
# ==========================================

CSV_PATH = "../Apify_Exports/Naukri_job.csv"

MASTER_RESUME = "../Resume_Master/Resume_Master.md"

# ==========================================
# KNOWLEDGE FOLDERS
# ==========================================

RULES_FOLDER = "../Rules"

SKILLS_FOLDER = "../Skills"

PROMPTS_FOLDER = "../Prompts"

TEMPLATES_FOLDER = "../Templates"

# ==========================================
# OUTPUTS
# ==========================================

REPORT_OUTPUT = (
    f"../Job_Reports/report_{timestamp}.md"
)

OUTPUT_RESUME_FOLDER = "../Output_Resume"

COVER_LETTER_FOLDER = "../Cover_Letters"

DOC_OUTPUT_FOLDER = "../Generated_DOCX"

# ==========================================
# SETTINGS
# ==========================================

TOP_N_JOBS = 20