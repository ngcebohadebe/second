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
    file_path_resume = "C:/Users/Ngcebo.Hadebe/OneDrive - Ctrack (PTY) Ltd/Desktop/second/NTH_text.txt"
    file_path_job = "C:/Users/Ngcebo.Hadebe/OneDrive - Ctrack (PTY) Ltd/Desktop/second/job_text.txt"

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
        

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ResumeBuilder().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResumeBuilder().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        ResumeBuilder().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
