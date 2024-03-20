from flask import Flask, request, jsonify
from celery import Celery
from datetime import datetime
import csv


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name)
celery.conf.update(app.config)

MEETINGS_FILE = 'meetings.csv'


@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
    """
    Endpoint to schedule a new meeting.
    Expects JSON payload with meeting details.
    """
    data = request.json

    if data is not None:
        meeting_id = data.get('meeting_id')
        password = data.get('password')
        time = data.get('time')
        date = data.get('date')
        duration = data.get('duration')

        # Save meeting details to CSV file
        with open(MEETINGS_FILE, 'a', newline='') as csvfile:
            fieldnames = ['meeting_id', 'password', 'time', 'date', 'duration']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:  # Check if file is empty
                writer.writeheader()
            writer.writerow({
                'meeting_id': meeting_id,
                'password': password,
                'time': time,
                'date': date,
                'duration': duration
            })

        # Schedule task to start meeting container
        # start_meeting_container.apply_async(args=[meeting_id, data], eta=datetime.strptime(
        #     date + ' ' + time, '%d %H:%M'))

        return jsonify({'message': 'Meeting scheduled successfully'}), 201

    else:
        return jsonify({'error': 'Invalid JSON payload'}), 400


@celery.task
def start_meeting_container(meeting_id, meeting_details):
    """
    Task to start Docker container for a meeting.
    """
    # Logic to start Docker container for meeting
    print(f'Starting Docker container for meeting {meeting_id}')
    print('Meeting Details:', meeting_details)
    # Replace this with your Docker container startup logic


if __name__ == '__main__':
    app.run(debug=True)
