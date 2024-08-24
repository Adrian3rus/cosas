import os
import shutil
from mutagen.easyid3 import EasyID3

def obtener_autor_mp3(ruta_archivo):
    try:
        # Cargar los metadatos del archivo MP3
        audio = EasyID3(ruta_archivo)
        # Retornar el nombre del artista (autor)
        return audio['artist'][0] if 'artist' in audio else None
    except Exception as e:
        print(f'Error al leer el autor de {ruta_archivo}: {e}')
        return None

def organizar_mp3_por_autor(carpeta_origen):
    # Carpeta para los archivos sin metadatos
    carpeta_sin_id = os.path.join(carpeta_origen, 'SIN_ID')
    if not os.path.exists(carpeta_sin_id):
        os.makedirs(carpeta_sin_id)

    # Recorre todos los archivos y subcarpetas en la carpeta origen
    for raiz, carpetas, archivos in os.walk(carpeta_origen):
        for archivo in archivos:
            if archivo.lower().endswith('.mp3'):
                ruta_completa = os.path.join(raiz, archivo)

                # Obtener el autor del archivo MP3
                autor = obtener_autor_mp3(ruta_completa)

                if autor:
                    # Crear la carpeta de destino según el autor
                    carpeta_destino = os.path.join(carpeta_origen, autor)

                    if not os.path.exists(carpeta_destino):
                        os.makedirs(carpeta_destino)

                    # Mover el archivo a la carpeta correspondiente
                    shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
                    print(f'Movido: {archivo} -> {carpeta_destino}')
                else:
                    # Mover el archivo a la carpeta SIN_ID
                    shutil.move(ruta_completa, os.path.join(carpeta_sin_id, archivo))
                    print(f'Movido a SIN_ID: {archivo}')

# Ruta de la carpeta que quieres organizar
carpeta_origen = 'c:/users/adria/Downloads'

organizar_mp3_por_autor(carpeta_origen)
