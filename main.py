import yt_dlp
import os

#Poner el link del video en la variable url
url = 'https://www.youtube.com/watch?v=9v6ZLgqCjV0'

#Definir la carpeta donde se guardará los audios
carpeta_destino = os.path.join(os.path.expanduser('D:/Audios-descargados-yy'), 'Audios')

#Crear la carpeta 'Audios' si no existe
os.makedirs(carpeta_destino, exist_ok=True)

#Opciones de descarga para obtener solo el audio
ydl_opts = {
    'format': 'bestaudio/best',  # Selecciona solo el mejor stream de audio disponible
    'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),  # Guardar en la carpeta especificada
    'postprocessors': [{  # Utiliza post-procesadores para convertir el formato de audio
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Convertir el audio a formato MP3
        'preferredquality': '192',  # Calidad del audio en kbps
    }],
}

#Descargar el audio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"Descarga completada. El audio se guardó en: {carpeta_destino}")