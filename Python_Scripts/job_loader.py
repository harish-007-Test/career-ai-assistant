# job_loader.py

import pandas as pd

from config import CSV_PATH

def load_jobs():

    df = pd.read_csv(CSV_PATH)

    df = df.fillna("")

    return df.to_dict(orient="records")