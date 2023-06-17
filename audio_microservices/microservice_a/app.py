import requests
import wave
import struct

MICROSERVICE_B_URL = 'http://microservice-b:5000/process_frame'


def check_audio_format(filepath):
    # Check audio file format (WAV file, sample rate 16 kHz, mono audio)
    with wave.open(filepath, 'rb') as audio:
        sample_width = audio.getsampwidth()
        channels = audio.getnchannels()
        sample_rate = audio.getframerate()

        if sample_width != 2 or channels != 1 or sample_rate != 16000:
            raise ValueError("Incorrect audio format. Expected WAV file with sample rate 16 kHz and mono audio.")


def cut_audio_into_frames(filepath):
    frames = []
    frame_size = 640  # 20 ms frame size for 16 kHz sample rate (16 kHz * 2 bytes/sample * 0.02 seconds = 640 bytes)

    with wave.open(filepath, 'rb') as audio:
        sample_width = audio.getsampwidth()

        while True:
            data = audio.readframes(frame_size)
            if not data:
                break
            frames.append(data)

    return frames


def send_frame_to_microservice(frame):
    response = requests.post(MICROSERVICE_B_URL, data=frame)

    if response.status_code == 200:
        return response.text.strip() == "True"
    else:
        raise ValueError("Error communicating with Microservice B")


def process_audio_file(filepath):
    check_audio_format(filepath)
    frames = cut_audio_into_frames(filepath)

    for frame in frames:
        result = send_frame_to_microservice(frame)
        print(result)


if __name__ == "__main__":
    audio_file_path = "/app/audio_files/assignment_audio.wav"
    process_audio_file(audio_file_path)