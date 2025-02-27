# 🎙️ DRAVYA - Real-Time Voice Emotion Analyzer

## 📜 Description

**DRAVYA** is a **Real-Time Voice Emotion Analyzer** that processes live speech, transcribes it using OpenAI's **Whisper** model, and determines the emotional tone using **SpeechBrain**. It operates in real-time, automatically detecting speech and stopping when silence is detected, making it ideal for AI-driven sentiment analysis, conversational AI, and human-computer interaction.

## 🚀 Features

- **Live Speech-to-Emotion Analysis**: Detects and analyzes speech in real-time.
- **Whisper-Based Transcription**: Converts spoken words into accurate text.
- **Emotion Detection with SpeechBrain**: Identifies emotions like *neutral, happy, sad, angry, fearful, and surprised*.
- **Automated Silence Detection**: Stops recording after 3 seconds of silence.
- **Fully Automated Processing**: No need to manually record or upload files.

## ⚙️ Installation

To set up DRAVYA, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/theasynch/DRAVYA.git
   cd DRAVYA
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Required Speech Models**:
   The Whisper and SpeechBrain models will be automatically downloaded during the first run.

## 🖥️ Usage

1. **Run the Program**:
   ```bash
   python dravya.py
   ```
2. **Start Speaking**: The system will detect your speech and stop automatically after 3 seconds of silence.
3. **View Results**: The program will display the transcribed text along with the detected emotion.

### 🌟 Example

```bash
python dravya.py
```
**Output:**
```
Listening... Speak now.
Transcribed Text: "I am feeling really great today!"
Detected Emotion: Happy
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please fork the repository and submit a pull request. Ensure that your changes are well-documented.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- [OpenAI Whisper](https://openai.com/research/whisper) - For real-time speech recognition.
- [SpeechBrain](https://speechbrain.github.io/) - For powerful emotion detection models.
- Open-source community - For continuous support and innovation in AI-driven solutions.

