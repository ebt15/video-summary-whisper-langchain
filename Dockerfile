# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Update the package list, install Git and ffmpeg, and clean up
RUN apt-get update && \
    apt-get install -y git ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install the whisper package from GitHub
RUN pip install git+https://github.com/openai/whisper.git 

# Copy the rest of the current directory contents into the container at /app
COPY . /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV OPENAI_API_KEY None

# Run main.py when the container launches
CMD ["streamlit", "run", "app.py"]