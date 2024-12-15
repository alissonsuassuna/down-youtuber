import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

def download_video():
    url = url_entry.get()
    folder = folder_path.get()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo.")
        return

    if not folder:
        messagebox.showerror("Erro", "Por favor, selecione uma pasta para salvar o vídeo.")
        return

    try:
        ydl_opts = {
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", f"Vídeo baixado com sucesso em {folder}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo: {e}")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# Configuração da janela principal
app = tk.Tk()
app.title("YouTube Video Downloader")
app.geometry("400x200")
app.resizable(False, False)

# Variáveis
folder_path = tk.StringVar()

# Widgets
url_label = tk.Label(app, text="URL do Vídeo:")
url_label.pack(pady=5)

url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

folder_label = tk.Label(app, text="Pasta de Destino:")
folder_label.pack(pady=5)

folder_entry = tk.Entry(app, textvariable=folder_path, width=50, state="readonly")
folder_entry.pack(pady=5)

browse_button = tk.Button(app, text="Selecionar Pasta", command=browse_folder)
browse_button.pack(pady=5)

download_button = tk.Button(app, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)

# Inicia o loop da interface
app.mainloop()
