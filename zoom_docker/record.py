import sounddevice as sd
import numpy as np
import imageio
import threading
import time
import wave

# Function to record audio


def record_audio(file_name, duration, samplerate=44100, channels=2):
    print("Recording audio...")
    audio_data = sd.rec(int(duration * samplerate),
                        samplerate=samplerate, channels=channels, blocking=True)
    print("Finished recording audio.")
    sd.wait()
    wavefile = wave.open(file_name, 'wb')
    wavefile.setnchannels(channels)
    wavefile.setsampwidth(2)
    wavefile.setframerate(samplerate)
    wavefile.writeframes(audio_data.tobytes())
    wavefile.close()

# Function to record video


def record_video(file_name, duration):
    print("Recording video...")
    frames = []
    start_time = time.time()
    while (time.time() - start_time) < duration:
        # Capture frame-by-frame
        # Assuming cv2 is not available, we'll use a placeholder image
        frame = np.random.randint(0, 256, size=(480, 640, 3), dtype=np.uint8)
        frames.append(frame)
        time.sleep(1/20)  # Simulate a frame rate of 20 frames per second

    # Save frames as a video file using imageio
    imageio.mimsave(file_name, frames, fps=20)

    print("Finished recording video.")

# Main function


def record():
    # Set the recording duration
    record_duration = 10  # in seconds

    # Start recording audio and video concurrently
    audio_thread = threading.Thread(
        target=record_audio, args=('output_audio.wav', record_duration))
    video_thread = threading.Thread(
        target=record_video, args=('output_video.avi', record_duration))

    audio_thread.start()
    video_thread.start()

    audio_thread.join()
    video_thread.join()

    print("Recording finished.")


if __name__ == "__main__":
    record()
