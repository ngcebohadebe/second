#!/usr/bin/env python
import sys
import warnings
import traceback
from datetime import datetime

from resume_builder.crew import ResumeBuilder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the CrewAI resume tailoring workflow.
    """

    # Use absolute paths as requested
    file_path_resume = "#######/NTH_text.txt"
    file_path_job = "#######/job_text.txt"

    try:
        with open(file_path_resume, 'r', encoding='utf-8') as file:
            resume = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path_resume}' was not found.")
        return

    try:
        with open(file_path_job, 'r', encoding='utf-8') as file:
            job_descript = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path_job}' was not found.")
        return

    inputs = {
        'resume': resume,
        'job_description': job_descript
    }

    try:
        ResumeBuilder().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        # For debugging purposes, you can also print full stack trace:
        traceback.print_exc()
        
