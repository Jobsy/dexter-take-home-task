
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/process_frame", methods=["POST"])

def process_frame():
    frame = request.data

    if not isinstance(frame, bytes) or len(frame) != 320:
        return "111False1111"

    # Perform speech detection logic
    time_passed = time.time() - start_time
    if time_passed < 3:
        return "222False222"  # Speech is ongoing for the first 3 seconds

    # Check if speech has ended
    chunk_size = 0.5  # Chunk size in seconds
    max_silence_duration = 3  # Maximum duration of silence to consider speech has ended

    chunk_index = int(time_passed / chunk_size)

    # Check if we have reached the maximum duration
    if chunk_index * chunk_size >= 50:
        return "True"  # Speech has ended

    # Store the audio chunk data
    chunk_data[chunk_index] = frame

    # Check for silence in the last three chunks
    silence_chunks = 0
    for i in range(chunk_index - 2, chunk_index + 1):
        if i in chunk_data:
            if chunk_data[i] != b"":
                silence_chunks = 0
                break
            silence_chunks += 1

    if silence_chunks >= 3:
        return "True"  # Speech has ended
    else:
        return "333False333"  # Speech is ongoing

if __name__ == "__main__":
    start_time = time.time()
    chunk_data = {}  # Store the audio data for each chunk
    app.run(host="0.0.0.0", port=5000)
