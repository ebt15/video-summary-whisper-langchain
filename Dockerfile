# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install the whisper package from GitHub
RUN pip install git+https://github.com/openai/whisper.git

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV OPENAI_API_KEY None

# Run main.py when the container launches
CMD ["streamlit", "run", "main.py"]