from celery import Celery
from datetime import datetime
import csv
import Docker
import subprocess

celery = Celery(__name__)


@celery.task
def start_meeting_container(meeting_id, meeting_details):
    """
    Task to start Docker container for a meeting.
    """
    # Logic to start Docker container for meeting
    print(f'Starting Docker container for meeting {meeting_id}')
    print('Meeting Details:', meeting_details)

    # Command to start the Docker container
    command = f"docker run -d --name {
        meeting_id} 5enox/zoom_recorder {meeting_details}"

    # Execute the command
    subprocess.run(command, shell=True)
