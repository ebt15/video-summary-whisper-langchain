import whisper

class WhisperTranscriber:
    def __init__(self, model_name="small.en"):
        self.model = whisper.load_model(model_name)

    def transcribe_audio(self, audio_file, output_file=None):
        result = self.model.transcribe(audio_file)
        text = result["text"]

        if output_file:
            with open(output_file, "w") as f:
                f.write(text)

        return text

if __name__ == "__main__":
    # Usage example:
    transcriber = WhisperTranscriber()
    transcription = transcriber.transcribe_audio("test.wav", output_file="output_file.txt")