import os
from dotenv import load_dotenv
import streamlit as st

from src.video_processing import VideoProcessor
from src.whisper_transcription import WhisperTranscriber
from src.summary_generation import SummaryGenerator

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

    def process_video(self, video_path):
        wav_file = self.video_processor.video_to_wav(video_path)
        transcript = self.whisper_transcriber.transcribe_audio(wav_file)
        return self.summary_generator.summarize_document(transcript)


def main():
    # Create the "uploaded_videos" folder if it doesn't exist
    if not os.path.exists("uploaded_videos"):
        os.makedirs("uploaded_videos")

    video_summarizer = VideoSummarizer()

    # Streamlit code for UI
    st.title("Video Summarizer")

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        save_path = os.path.join("uploaded_videos", uploaded_file.name)
        video_summarizer.save_uploaded_file(uploaded_file, save_path)

        st.success(f"File saved to {save_path}")

        # Process the video and generate the summary
        summary = video_summarizer.process_video(save_path)

        # Display the summary
        st.header("Summary")
        st.write(summary)


if __name__ == "__main__":
    main()