import ffmpeg

class VideoProcessor:
    def __init__(self):
        pass

    def video_to_wav(self, src, wave_dst="test.wav"):
        """
        This function is used to convert the video to wave file.
        :src: the video file path
        :wave_dst: the wave file path, default is "test.wav"
        :return: wave_dst or None
        """
        video = ffmpeg.input(src)
        audio = video.audio
        audio = audio.output(wave_dst, acodec='pcm_s16le', ac=1, ar='16000')
        audio.run(overwrite_output=True)
        return wave_dst

    def get_audio_length(self, wave_dst):
        """
        This function is used to get the audio length from the wave file.
        :wave_dst: the wave file path
        :return:
        audio_length: the audio length
        """
        return ffmpeg.probe(wave_dst)['format']['duration']
    
if __name__ == "__main__":
    vp = VideoProcessor()
    print(vp.video_to_wav("C:/Users/ebin/Downloads/test_video.mp4"))