import docker

# Initialize the Docker client
client = docker.from_env()

# Define the paths of the file on the host and inside the container
host_file_path = "req.txt"
container_file_path = "docerk/req.txt"

# Start a container
container = client.containers.run(
    "ubuntu:latest", detach=True, tty=True, name="my-container")

# Copy the file into the container
with open(host_file_path, 'rb') as file:
    container.put_archive(container_file_path, file)

# Stop and remove the container
container.stop()
container.remove()
