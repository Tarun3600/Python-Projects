import tkinter
import customtkinter
from pytube import YouTube
import threading

# Function to start downloading the video
def startDownload():
    try:
        # Get the YouTube link from the input field
        ytLink = link.get()
        
        # Create a YouTube object
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        
        # Get the highest resolution progressive stream with mp4 format
        video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Update title and clear previous messages
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        
        # Start downloading the video
        video.download()
        
        # Notify user that the download is finished
        finishLabel.configure(text="Downloaded!")
    except Exception as e:
        # Handle any errors during download
        finishLabel.configure(text=f"Download Error: {str(e)}", text_color="red")

# Function to update progress during the download
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    # Update the percentage label
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

# Function to start the download in a new thread
def startDownloadThread():
    download_thread = threading.Thread(target=startDownload)
    download_thread.start()

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create the main application window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements

# Label for entering YouTube link
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

# Input field for the YouTube link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Label to display download status
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Label to display progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Progress bar to show download progress
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Button to start the download
download = customtkinter.CTkButton(app, text="Download", command=startDownloadThread)
download.pack(padx=10, pady=10)

# Run the application
app.mainloop()
