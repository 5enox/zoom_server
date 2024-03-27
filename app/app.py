from flask import Flask, request, jsonify
from .tasks import start_zoom_recorder

from datetime import datetime
import csv

app = Flask(__name__)
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
        start_zoom_recorder.apply_async(args=[meeting_id, password, duration], eta=datetime.strptime(
            date + ' ' + time, '%Y-%m-%d %H:%M:%S'))

        return jsonify({'message': 'Meeting scheduled successfully'}), 201

    else:
        return jsonify({'error': 'Invalid JSON payload'}), 400


if __name__ == '__main__':
    app.run(debug=True)
