# 🎙️ DRAVYA - Voice Emotion Analyzer

## 📜 Description

**DRAVYA** is a **Voice Emotion Analyzer** that processes audio recordings and determines the emotional tone present in the speech. It utilizes **SpeechBrain**, a state-of-the-art deep learning library for speech processing, to extract emotions from voice signals. This tool is useful for applications like sentiment analysis, AI-driven customer support, and emotional intelligence research.

## 🚀 Features

- **Speech-to-Emotion Analysis**: Identifies emotions in voice recordings.
- **Deep Learning Integration**: Uses a **pre-trained SpeechBrain model** for emotion detection.
- **Automated Processing**: Accepts an audio file, extracts features, and predicts the emotional state.
- **Multi-Emotion Classification**: Supports emotions such as *neutral, happy, sad, angry, fearful, and surprised*.
- **Command-Line Interface**: Simple CLI-based interaction for easy execution.

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

3. **Download Required Speech Model**:
   The program will automatically download the necessary SpeechBrain emotion recognition model during its first run.

## 🖥️ Usage

1. **Provide an Audio File**: Ensure your audio file is in **WAV format**.
2. **Run the Program**:
   ```bash
   python dravya.py input_audio.wav
   ```
3. **View Results**: The detected emotion will be displayed in the console output.

### 🌟 Example

```bash
python dravya.py test_audio.wav
```
**Output:**
```
Predicted Emotion: Happy
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please fork the repository and submit a pull request. Ensure that your changes are well-documented.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- [SpeechBrain](https://speechbrain.github.io/) - For the powerful pre-trained models for speech processing.
- [OpenAI](https://openai.com/) - For ongoing inspiration in AI research.
- Open-source community - For continuous support and innovation in AI-driven solutions.

