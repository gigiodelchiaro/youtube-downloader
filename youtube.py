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

        output_folder = './'

        default_video_name = f"{youtube_video.title}.{audio_format}"
        video_path = os.path.join(output_folder, default_video_name)
        video_stream.download(output_path=output_folder, filename=default_video_name)
        
        return video_path

def main():
    functions = YouTubeStreamConverterFunctions()
    if len(sys.argv) > 2:
        return functions.download_video(sys.argv[1], sys.argv[2])
    else:
        return "Usage: youtube.exe https://www.youtube.com/watch?v=your_video_id filetype"

if __name__ == "__main__":
    print(main())