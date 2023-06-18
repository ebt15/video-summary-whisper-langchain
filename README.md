# Video Summarizer App

This Video Summarizer App uses LangChain and Whisper libraries to transcribe and summarize video content. The app transcribes the video to text using the Whisper model from OpenAI, and then generates a summary using the gpt-3.5-turbo model API. The app is built with Streamlit for the UI/Web App interface and deployed on AWS Elastic Beanstalk using Docker containers.

## Features

- Transcribe video to text using the Whisper model from OpenAI
- Summarize the transcript using the gpt-3.5-turbo model API
- Handle context limitations using the 'refine' chain in the LangChain library
- Streamlit UI/Web App interface
- Deployment on AWS Elastic Beanstalk using Docker containers

## Technologies

- LangChain
- Whisper
- OpenAI
- Tiktoken
- Streamlit
- AWS Elastic Beanstalk
- Docker

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Docker
- AWS CLI
- An OpenAI API key

### Installation

1. Clone the repository:

```
git clone https://github.com/ebt15/video-summary-whisper-langchain.git
cd video-summary-whisper-langchain
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

3. Install the required packages:

```
pip install -r requirements.txt
pip install git+https://github.com/openai/whisper.git
```

4. Set up your OpenAI API key:

```
export OPENAI_API_KEY=your_api_key  # For Linux/Mac
set OPENAI_API_KEY=your_api_key  # For Windows
```

### Running the App

1. Start the Streamlit app:

```
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501` to access the app.

### Running the Video Summarizer App using Docker

This section will guide you on how to run the Video Summarizer App using Docker. Docker allows you to package the application along with its dependencies into a container, making it easy to run the app on any system with Docker installed.

### Prerequisites

Before you proceed, make sure you have the following installed on your system:

1. [Docker](https://www.docker.com/products/docker-desktop): Download and install the appropriate version of Docker for your operating system.

2. An OpenAI API key: You will need an API key from OpenAI to use the video summarizer. You can obtain one by signing up at [OpenAI](https://beta.openai.com/signup/).

### Steps to run the app

1. Clone the repository or download the source code of the Video Summarizer App to your local machine.

2. Open a terminal or command prompt and navigate to the root directory of the Video Summarizer App.

3. Build the Docker image by running the following command:

   ```
   docker build -t video-summarizer .
   ```

   This command will create a Docker image named `video-summarizer` using the Dockerfile in the current directory.

4. Run the Docker container using the following command:

   ```
   docker run -d -p 8501:8501 --env OPENAI_API_KEY=<your_openai_api_key> video-summarizer
   ```

   Replace `<your_openai_api_key>` with your actual OpenAI API key. This command will run the `video-summarizer` image in a detached mode, mapping the host's port 8501 to the container's port 8501, and setting the `OPENAI_API_KEY` environment variable.

5. Open your web browser and navigate to `http://localhost:8501`. You should now see the Video Summarizer App running.

6. To stop the running container, first find the container ID by running:

   ```
   docker ps
   ```

   This command will list all running containers along with their IDs.

7. Stop the container by running:

   ```
   docker stop <container_id>
   ```

   Replace `<container_id>` with the actual container ID from the previous step.

That's it! You have successfully run the Video Summarizer App using Docker.

### Deployment

1. Build the Docker container:

```
docker build -t video-summarizer .
```

2. Deploy the app to AWS Elastic Beanstalk:

```
eb init -p docker video-summarizer
eb create video-summarizer-env
```

3. Set the OpenAI API key in the Elastic Beanstalk environment:

```
eb setenv OPENAI_API_KEY=your_api_key
```

4. Open the app in your browser using the provided Elastic Beanstalk URL.
