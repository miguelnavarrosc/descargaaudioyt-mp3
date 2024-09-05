import yt_dlp
import os

#cambia LINK DE VIDEO por el link del video ecesario.
url = 'LINK DE VIDEO'

#Definir la carpeta  cambia RUTA_DESTINO con la ruta de la carpeta que necesitas.
carpeta_destino = os.path.join(os.path.expanduser('D:/App-Mp3-Python'), 'Audios')

#Crear la carpeta si no existe
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