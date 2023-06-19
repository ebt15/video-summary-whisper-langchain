import os
from dotenv import load_dotenv
import streamlit as st

from src.video_processing import VideoProcessor
from src.whisper_transcription import WhisperTranscriber
from src.summary_generation import SummaryGenerator
import base64
from streamlit import components

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


class VideoSummarizer:
    def __init__(self):
        self.video_processor = VideoProcessor()
        self.whisper_transcriber = WhisperTranscriber()
        self.summary_generator = SummaryGenerator()

    @staticmethod
    def save_uploaded_file(uploaded_file, save_path):
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
            
    @staticmethod
    def create_auto_download_link(content, filename):
        b64_content = base64.b64encode(content.encode()).decode()
        js_code = f'''
            function download_transcript() {{
                var link = document.createElement('a');
                link.href = "data:text/plain;base64,{b64_content}";
                link.download = "{filename}";
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }}
        '''
        return f'<script>{js_code}</script><button onclick="download_transcript()">Download Transcript</button>'

    def process_video(self, video_path, progress_bar, progress_text, summary_type):
        progress_text.text("Processing video...")
        wav_file = self.video_processor.video_to_wav(video_path)
        progress_bar.progress(33)

        progress_text.text("Transcribing audio...")
        transcript = self.whisper_transcriber.transcribe_audio(wav_file)
        progress_bar.progress(66)

        progress_text.text("Generating summary...")
        summary = self.summary_generator.summarize_document(transcript, summary_type)
        progress_bar.progress(100)

        return summary, transcript

def main():
    # Hide Streamlit branding
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Create the "uploaded_videos" folder if it doesn't exist
    if not os.path.exists("uploaded_videos"):
        os.makedirs("uploaded_videos")

    video_summarizer = VideoSummarizer()

    # Streamlit code for UI
    st.title("Video Summarizer")
        
    # Add a select box for summary type
    summary_type = st.selectbox("Select Summary Type", ["Detailed", "Concise"])

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        save_path = os.path.join("uploaded_videos", uploaded_file.name)
        video_summarizer.save_uploaded_file(uploaded_file, save_path)

        st.success(f"File saved to {save_path}")

        # Add a progress bar and progress text
        progress_bar = st.progress(0)
        progress_text = st.empty()

        # Process the video and generate the summary
        summary, transcript = video_summarizer.process_video(save_path, progress_bar, progress_text, summary_type)

        # Display the summary
        st.header("Summary")
        st.write(summary)
        progress_text.text("Done!")

        # Provide a feature to download the transcript
        download_link = video_summarizer.create_auto_download_link(transcript, "transcript.txt")
        components.v1.html(download_link, height=50)

if __name__ == "__main__":
    main()