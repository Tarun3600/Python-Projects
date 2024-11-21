from gtts import gTTS
import tkinter as tk
from pydub import AudioSegment
import os
import pyrubberband as pyrb
import numpy as np
import wave

def window():
    # Create the main window for the GUI
    root = tk.Tk()
    root.title("Dictation")
    root.geometry("800x600")
    root.config(bg="#f0f0f0")

    # Label for the title of the application
    title_label = tk.Label(root, text="Text-to-Speech Dictation", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
    title_label.pack(pady=20, anchor="center")

    # Textbox for user to input their text
    entry = tk.Text(root, font=("Helvetica", 18), width=40, height=5, bd=2, relief="solid")
    entry.pack(pady=20, anchor="center")

    # Label and slider for adjusting playback speed
    slider_label = tk.Label(root, text="Set Playback Speed", font=("Helvetica", 12), bg="#f0f0f0")
    slider_label.pack(pady=10, anchor="center")

    slider = tk.Scale(root, from_=1.0, to=3.0, orient="horizontal", resolution=0.1, length=300)
    slider.set(1.0)  # Set default speed to 1.0
    slider.pack(pady=10, anchor="center")

    # Checkbox to decide if silences should be added between words
    silence_var = tk.BooleanVar()
    silence_checkbox = tk.Checkbutton(root, text="Add silences between words (in ms)", font=("Helvetica", 12), bg="#f0f0f0", variable=silence_var)
    silence_checkbox.pack(pady=10, anchor="center")
    
    # Slider to control the length of the silence between words
    silence_slider = tk.Scale(root, from_=0, to=10000, orient="horizontal", resolution=10, length=300)
    silence_slider.set(300)  # Default gap of 300ms
    silence_slider.pack(pady=10, anchor="center")

    # Button to generate the speech from the entered text
    button = tk.Button(
        root, text="Generate Speech", font=("Helvetica", 14), bg="#4CAF50", fg="white",
        relief="raised", command=lambda: generate_speech(entry, slider.get(), silence_var.get(), silence_slider.get())
    )
    button.pack(pady=20, anchor="center")

    root.mainloop()

def audio_manipulation(playback_speed):
    # Load the text-to-speech MP3 file
    audio = AudioSegment.from_file("text.mp3")
    
    # Export the MP3 to WAV format for pyrubberband manipulation
    audio.export("temp.wav", format="wav")

    # Read the WAV file to manipulate it
    with wave.open("temp.wav", 'rb') as f:
        rate = f.getframerate()  # Get the sample rate (number of samples per second)
        frames = f.readframes(f.getnframes())  # Read the raw audio data
    
    # Convert the byte data to a NumPy array for pyrubberband processing
    audio_data = np.frombuffer(frames, dtype=np.int16)
    # Stretch or shrink the audio based on the selected playback speed
    manipulated_data = pyrb.time_stretch(audio_data, rate, playback_speed)
    
    # Write the manipulated audio to a new WAV file
    manipulated_audio = wave.open("faster_example.wav", 'wb')
    manipulated_audio.setnchannels(1)  # Set the audio to mono (1 channel)
    manipulated_audio.setsampwidth(2)  # Set sample width to 2 bytes (16-bit audio)
    manipulated_audio.setframerate(rate)  # Set the sample rate to the original rate
    manipulated_audio.writeframes(manipulated_data.tobytes())  # Save the manipulated audio to the file
    manipulated_audio.close()

    # Clean up by deleting the temporary WAV file
    os.remove("temp.wav")
    print(f"Successfully manipulated audio with playback speed: {playback_speed}")

def generate_speech(entry, playback_speed, silence_var, silence_slider):
    # Get the text from the user input box
    text = entry.get("1.0", "end-1c")
    language = 'en'  # Language set to English

    words = text.split()  # Split the text into individual words
    audio_segments = []  # Store the generated speech segments

    if silence_var:  # If the user wants silences between words
        # Generate speech for each word and add silence after each
        for word in words:
            speech = gTTS(text=word, lang=language, slow=False)
            speech.save(f"{word}.mp3")
            word_audio = AudioSegment.from_file(f"{word}.mp3")

            silence = AudioSegment.silent(duration=silence_slider)  # Create silence for the gap
            audio_segments.append(word_audio + silence)  # Combine word and silence

            os.remove(f"{word}.mp3")  # Delete the temporary word audio file
        
        # Combine all the word + silence segments
        final_audio = sum(audio_segments)
        final_audio.export("text.mp3", format="mp3")
    else:  # If no silences are needed, generate the speech for the entire text
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("temp.mp3")
        final_audio = AudioSegment.from_file("temp.mp3")
        final_audio.export("text.mp3", format="mp3")
        os.remove("temp.mp3")  # Clean up temporary file

    # Print confirmation of speech generation
    if silence_var:
        print("Speech generated with silences successfully.")
    else:
        print("Speech generated without silences successfully.")

    # Manipulate the audio (change playback speed)
    audio_manipulation(playback_speed)

# Run the main window
window()
