'''
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
'''
from pytube import YouTube
import os
import sys

filetypes = {
    'mp4': False,
    'mp3': True,
    'wav': True
}

class YouTubeStreamConverterFunctions:
    def __init__(self):
        pass

    def download_video(self, video_url, audio_format):
        youtube_video = YouTube(video_url)
        if filetypes[audio_format]:
            video_stream = youtube_video.streams.get_audio_only()
        else:
            video_stream = youtube_video.streams.get_highest_resolution()

        # output_folder = filedialog.askdirectory(initialdir=os.getcwd(), title="Select output folder")
        output_folder = './'
        if not output_folder:
            return None

        default_video_name = f"{youtube_video.title}.{audio_format}"
        video_path = os.path.join(output_folder, default_video_name)
        video_stream.download(output_path=output_folder, filename=default_video_name)
        # messagebox.showinfo("Download Completed", f"Video downloaded successfully.\nSaved at: {video_path}")
        return video_path
    
'''
class YouTubeStreamConverterUI:
    def __init__(self, master, functions):
        self.master = master
        self.functions = functions
        master.title("YouTube Video Converter")
        master.geometry("500x300")

        style = ttk.Style()
        style.configure('TLabel', font=('Segoe UI', 12))
        style.configure('TButton', font=('Segoe UI', 12))
        style.configure('TCheckbutton', font=('Segoe UI', 12))
        style.configure('TEntry', font=('Segoe UI', 12))

        self.url_label = ttk.Label(master, text="Video Link:")
        self.url_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.url_entry = ttk.Entry(master, width=40)
        self.url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        self.convert_to_wav_var = tk.IntVar()
        self.convert_to_wav_checkbox = ttk.Checkbutton(master, text="Convert to MP3", variable=self.convert_to_wav_var)
        self.convert_to_wav_checkbox.grid(row=1, column=0, columnspan=3, pady=5)

        self.start_button = ttk.Button(master, text="Start", command=self.start_conversion)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10)

    def start_conversion(self):
        youtube_video_url = self.url_entry.get().strip()
        audio_format = 'mp3' if bool(self.convert_to_wav_var.get()) else 'mp4'

        if not youtube_video_url:
            messagebox.showerror("Error", "Invalid link.")
            return

        try:
            self.functions.download_video(youtube_video_url, audio_format)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
'''
def main():
    functions = YouTubeStreamConverterFunctions()
    if len(sys.argv) > 2:
        return functions.download_video(sys.argv[1], sys.argv[2])
    
    else:
        return "Usage: youtube.exe https://www.youtube.com/watch?v=your_video_id filetype"
    '''
        root = tk.Tk()
        app = YouTubeStreamConverterUI(root, functions)
        root.mainloop()
    '''
    return 0

if __name__ == "__main__":
    print(main())
