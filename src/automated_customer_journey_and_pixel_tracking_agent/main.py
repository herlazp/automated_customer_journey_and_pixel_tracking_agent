#!/usr/bin/env python
import os
import sys
from automated_customer_journey_and_pixel_tracking_agent.crew import AutomatedCustomerJourneyAndPixelTrackingAgentCrew

# Disable CrewAI telemetry
os.environ["CREWAI_TELEMETRY_ENABLED"] = "False"

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'website_url': 'https://www.caixabank.es/',
        'specific_flow': 'Hipotecas',
        'tracking_platforms': 'Adobe Analytics',
        'expected_pixels': '',
        'max_clicks_per_view': 3 # Added new input for max clicks
    }
    AutomatedCustomerJourneyAndPixelTrackingAgentCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'website_url': 'sample_value',
        'specific_flow': 'sample_value',
        'tracking_platforms': 'sample_value',
        'expected_pixels': 'sample_value',
        'max_clicks_per_view': 3
    }
    try:
        AutomatedCustomerJourneyAndPixelTrackingAgentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AutomatedCustomerJourneyAndPixelTrackingAgentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'website_url': 'sample_value',
        'specific_flow': 'sample_value',
        'tracking_platforms': 'sample_value',
        'expected_pixels': 'sample_value',
        'max_clicks_per_view': 3
    }
    try:
        AutomatedCustomerJourneyAndPixelTrackingAgentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
