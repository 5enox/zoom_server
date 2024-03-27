from celery import Celery
import docker

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

# Docker client
docker_client = docker.from_env()

# Celery task definition


@app.task
def start_zoom_recorder(meeting_id, meeting_password, duration):
    try:
        # Define environment variables for the Docker container
        environment = {
            'MEETING_ID': meeting_id,
            'MEETING_PASSWORD': meeting_password,
            'DURATION': duration
        }

        # Start the Docker container
        container = docker_client.containers.run(
            '5enox/zoom_recorder',
            detach=True,
            environment=environment,
            # You can specify additional Docker container options here
            # e.g., volumes, network settings, etc.
        )

        # Print container ID for debugging
        # print(f"Started Docker container: {container.id}")
        print(f"Started Docker container")

        # return f"Started Docker container: {container.id}"
        return f"Started Docker container"
    except Exception as e:
        # Handle any exceptions gracefully
        print(f"An error occurred: {str(e)}")
        return None

# Example usage:
# start_zoom_recorder.delay("1234567890", "password123", "60")
