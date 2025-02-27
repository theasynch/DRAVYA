import whisper
import numpy as np
import torch
import sounddevice as sd
import torchaudio
from speechbrain.inference import EncoderClassifier

# Load OpenAI Whisper model (small, medium, or large available)
whisper_model = whisper.load_model("small")

# Load SpeechBrain's emotion recognition model
emotion_model = EncoderClassifier.from_hparams(source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP", savedir="tmpdir")

# Parameters
SILENCE_THRESHOLD = 3  # Seconds of silence before stopping recording
SAMPLERATE = 16000

def record_audio():
    """Records audio until 3 seconds of silence are detected."""
    print("Listening... Speak now.")

    audio_buffer = []
    silence_duration = 0

    def callback(indata, frames, time, status):
        """Callback function for non-blocking recording."""
        nonlocal silence_duration
        volume_norm = np.mean(np.abs(indata))  # More accurate silence detection
        
        print(f"Volume: {volume_norm}")  # Debugging print statement
        
        if volume_norm < 0.001:  # Adjusted silence threshold
            silence_duration += 1
            print(f"Silence duration: {silence_duration}")
        else:
            silence_duration = 0  # Reset if speech is detected
            audio_buffer.append(indata.copy())

        if silence_duration >= SILENCE_THRESHOLD:
            raise sd.CallbackStop

    with sd.InputStream(samplerate=SAMPLERATE, channels=1, callback=callback):
        try:
            sd.sleep(100000)  # Keep recording until silence is detected
        except sd.CallbackStop:
            pass

    if len(audio_buffer) == 0:
        print("No audio recorded. Try speaking louder or adjusting the silence threshold.")
        return torch.zeros(1)  # Return dummy tensor to avoid crashes

    audio_data = np.concatenate(audio_buffer, axis=0)
    print(f"Recorded {len(audio_data)} samples.")
    return torch.tensor(audio_data, dtype=torch.float32)

def transcribe_audio(audio_data):
    """Converts recorded audio into text using OpenAI Whisper."""
    print("Processing speech...")
    
    # Save audio as a .wav file before transcribing
    torchaudio.save("temp_audio.wav", audio_data.unsqueeze(0), SAMPLERATE)
    transcription = whisper_model.transcribe("temp_audio.wav")
    return transcription["text"]

def analyze_emotion(audio_data):
    """Uses SpeechBrain's emotion model to analyze the audio file."""
    signal = audio_data.unsqueeze(0)
    embeddings = emotion_model.encode_batch(signal)
    predictions = emotion_model.classify_batch(embeddings)
    
    print(f"Emotion predictions: {predictions}")  # Debugging print
    
    if len(predictions) > 3:  # Ensure index 3 exists
        return predictions[3]
    else:
        return "Unknown"

if __name__ == "__main__":
    audio = record_audio()
    if audio.numel() > 1:  # Ensure valid audio was recorded
        transcript = transcribe_audio(audio)
        print(f"Transcribed Text: {transcript}")

        emotion = analyze_emotion(audio)
        print(f"Detected Emotion: {emotion}")
    else:
        print("No valid audio detected. Exiting...")