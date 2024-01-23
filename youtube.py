import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

class YouTubeStreamConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Converter vídeo do YouTube")
        master.geometry("500x300")  # Ajuste o tamanho da janela principal

        # Estilo do ttk
        style = ttk.Style()
        style.configure('TLabel', font=('Segoe UI', 12))  # Ajuste a fonte para os rótulos
        style.configure('TButton', font=('Segoe UI', 12))  # Ajuste a fonte para os botões
        style.configure('TCheckbutton', font=('Segoe UI', 12))  # Ajuste a fonte para os checkbuttons
        style.configure('TEntry', font=('Segoe UI', 12))  # Ajuste a fonte para as entradas

        # Widget de entrada para URL do YouTube
        self.url_label = ttk.Label(master, text="Link do vídeo:")
        self.url_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.url_entry = ttk.Entry(master, width=40)
        self.url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        # Checkbutton para conversão de áudio
        self.convert_to_wav_var = tk.IntVar()
        self.convert_to_wav_checkbox = ttk.Checkbutton(master, text="Converter para WAV", variable=self.convert_to_wav_var)
        self.convert_to_wav_checkbox.grid(row=1, column=0, columnspan=3, pady=5)

        # Botão para iniciar streaming e conversão
        self.start_button = ttk.Button(master, text="Iniciar", command=self.start_conversion)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10)


    def start_conversion(self):
        youtube_video_url = self.url_entry.get().strip()
        convert_to_wav = bool(self.convert_to_wav_var.get())

        if not youtube_video_url:
            messagebox.showerror("Erro", "Link inválido.")
            return

        try:
            self.stream_and_convert(youtube_video_url, convert_to_wav)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def stream_and_convert(self, video_url, convert_to_wav):
        # Cria um objeto YouTube
        youtube_video = YouTube(video_url)

        # Obtém o fluxo de maior resolução (você pode personalizar isso com base em seus requisitos)
        video_stream = youtube_video.streams.get_highest_resolution()

        # Pede ao usuário para escolher uma pasta
        output_folder = filedialog.askdirectory(initialdir=os.getcwd(), title="Selecione a pasta de saída")

        if not output_folder:
            return

        # Define nomes de arquivo padrão com base no título do vídeo
        default_video_name = f"{youtube_video.title}.mp4"
        default_wav_name = f"{youtube_video.title}.wav"

        # Baixa o vídeo
        video_path = os.path.join(output_folder, default_video_name)
        video_stream.download(output_path=output_folder, filename=default_video_name)

        if convert_to_wav:
            # Converte o áudio temporário do vídeo para WAV
            video_clip = VideoFileClip(video_path)
            audio_clip = video_clip.audio
            wav_output_path = os.path.join(output_folder, default_wav_name)
            audio_clip.write_audiofile(wav_output_path, codec='pcm_s16le')
            audio_clip.close()
            video_clip.close()

            # Exclui o arquivo de vídeo temporário
            os.remove(video_path)

            messagebox.showinfo("Conversão Concluída", f"Conversão de vídeo e áudio concluída.\nÁudio salvo em: {wav_output_path}")
        else:
            messagebox.showinfo("Conversão Concluída", f"Vídeo baixado com sucesso.\nSalvo em: {video_path}")

def main():
    root = tk.Tk()
    app = YouTubeStreamConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
