import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to download the video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    # Prompt user to select a folder
    folder_path = filedialog.askdirectory(title="Select Download Folder")
    if not folder_path:
        messagebox.showwarning("Warning", "No folder selected. Download cancelled.")
        return

    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': f'{folder_path}/%(title)s.%(ext)s',  # Save with video title and extension in the chosen folder
        'quiet': False,  # Set to True to hide download progress
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'Unknown Title')
            messagebox.showinfo("Success", f"Video '{video_title}' downloaded successfully to:\n{folder_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main tkinter window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# Add an icon or logo
try:
    logo_label = tk.Label(root, text="🎥 YouTube Downloader", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#ff0000")
    logo_label.pack(pady=10)
except Exception:
    pass

# URL Label
url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12), bg="#f0f4f7", fg="#333333")
url_label.pack(pady=5)

# URL Entry Box
url_entry = tk.Entry(root, width=50, font=("Arial", 12), highlightbackground="#cce5ff", highlightthickness=2)
url_entry.pack(pady=10)

# Download Button
download_button = tk.Button(
    root,
    text="Download Video",
    font=("Arial", 14, "bold"),
    bg="#28a745",
    fg="white",
    activebackground="#218838",
    activeforeground="white",
    command=download_video,
)
download_button.pack(pady=20)

# Footer
footer_label = tk.Label(
    root,
    text="Developed by Sanskar © 2024",
    font=("Arial", 10),
    bg="#f0f4f7",
    fg="#555555"
)
footer_label.pack(side="bottom", pady=10)

# Run the tkinter main loop
root.mainloop()
