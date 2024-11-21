# Text-to-Speech Dictation with Playback Speed Control

This project allows you to convert your text into speech with customizable options like playback speed and the ability to add silences between words. The app is built using `gTTS` (Google Text-to-Speech) for speech synthesis, `pydub` for audio manipulation, and `pyrubberband` for altering playback speed. It also features a simple GUI built with `tkinter`.

## Features

- **Text-to-Speech Conversion**: Input any text and have it read aloud.
- **Adjustable Playback Speed**: Control how fast or slow the speech is played.
- **Add Silences Between Words**: Insert a gap between words (adjustable in milliseconds).
- **Automatic Playback**: After generating the speech, it plays automatically.

## How to Use

1. **Run the App**: Simply run the Python script `main.py` to open the GUI.
   
2. **Enter Text**: Type the text you want to convert to speech in the text box.

3. **Adjust Playback Speed**: Use the slider to set how fast or slow you want the speech to be.

4. **Optional - Add Silences**: If you want to add a pause between words, check the "Add silences" box and adjust the duration.

5. **Generate Speech**: Click the "Generate Speech" button, and the app will create the speech with your settings and play it automatically!

## Installation

To get started with this project, you’ll need Python 3.x installed. Then, follow these steps:

1. **Clone the repository** or download the files.

2. **Install the dependencies**:

   pip install gTTS pydub numpy pyrubberband playsound

3. Make sure you have `ffmpeg` or `libav` installed for `pydub` to handle MP3 and WAV files.

   - On **Windows**: Download `ffmpeg` from the [official website](https://ffmpeg.org/download.html) and add it to your system's PATH.
.

## How It Works

- **Text-to-Speech**: You type text into the app, and `gTTS` generates an MP3 file with the speech.
- **Speed Adjustment**: The app lets you control the playback speed by stretching or shrinking the audio using `pyrubberband`.
- **Silence Insertion**: If you choose, the app inserts pauses between words. The length of the pause is adjustable.
- **Playback**: Once the speech is generated and processed, the app plays the resulting audio file automatically.

## Example

Let's say you type the following text:

> "Hello! Welcome to the Text-to-Speech Dictation app."

You can:
- Set the playback speed to 1.5x (faster).
- Enable silences between words and set the gap to 300 milliseconds.

The app will generate the speech, adjust the speed, insert silences between words, and then automatically play the final audio.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Bug reports and feature requests are also welcome!

