# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Zoom
RUN wget https://zoom.us/client/latest/zoom_amd64.deb
RUN dpkg -i zoom_amd64.deb

# Set the entrypoint command to run Zoom
ENTRYPOINT ["zoom"]
