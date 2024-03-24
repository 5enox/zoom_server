# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /flask

# Copy the  files to the working directory
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command to run Zoom
ENTRYPOINT ["python3 app/app.py"]