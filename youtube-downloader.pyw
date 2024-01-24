import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
import os
import sys
filetypes = {

    '.amv':True,
    '.asf':True,
    '.avi':True,
    '.drc':True,
    '.f4a':True,
    '.f4b':True,
    '.f4p':True,
    '.f4v':True,
    '.flv':True,
    '.flv':True,
    '.flv':True,
    '.gif':True,
    '.gifv':True,
    '.M2TS':True,
    '.m2v':True,
    '.m4p':True,
    '.m4v':True,
    '.m4v':True,
    '.mkv':True,
    '.mng':True,
    '.mov':True,
    '.mp2':True,
    '.mp4':True,
    
    '.mov':False,
    '.mp2':False,
    '.mp4':False,
    '.amv':False,
    '.asf':False,
    '.avi':False,
    '.drc':False,
    '.f4v':False,
    '.flv':False,
    '.M2TS':False,
    '.m2v':False,
    '.m4p':False,
    '.m4v':False,
    '.mkv':False
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

        output_folder = './'
        if len(sys.argv) == 1:
            output_folder = filedialog.askdirectory(initialdir=os.getcwd(), title="Select output folder")
        
        if not output_folder:
            return None

        default_video_name = f"{youtube_video.title}.{audio_format}"
        video_path = os.path.join(output_folder, default_video_name)
        video_stream.download(output_path=output_folder, filename=default_video_name)
        
        return video_path

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
            messagebox.showinfo("Download Completed", f"Video downloaded successfully.\nSaved at: {self.functions.download_video(youtube_video_url, audio_format)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
def main():
    functions = YouTubeStreamConverterFunctions()
    if len(sys.argv) > 2:
        return functions.download_video(sys.argv[1], sys.argv[2])

    elif len(sys.argv) == 1:
        
        root = tk.Tk()
        app = YouTubeStreamConverterUI(root, functions)
        root.mainloop()
        return 0
    else:
        return "Usage: youtube.exe https://www.youtube.com/watch?v=your_video_id filetype"

if __name__ == "__main__":
    print(main())