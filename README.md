# Video Summarizer App

This Video Summarizer App uses LangChain and Whisper libraries to transcribe and summarize video content. The app transcribes the video to text using the Whisper model from OpenAI, and then generates a summary using the gpt-3.5-turbo-16k model API. The app is built with Streamlit for the UI/Web App interface and deployed on AWS Elastic Beanstalk using Docker containers.

## Features

- Transcribe video to text using the Whisper model from OpenAI
- Summarize the transcript using the gpt-3.5-turbo-16k model API
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
git clone https://github.com/yourusername/video-summarizer.git
cd video-summarizer
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

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
