import os
import shutil
from mutagen.easyid3 import EasyID3
import musicbrainzngs

# Configura la conexión a MusicBrainz con tu información
musicbrainzngs.set_useragent("MusicOr", "1.0", "adrian3rus@gmail.com")

def obtener_metadatos_mp3(ruta_archivo):
    try:
        audio = EasyID3(ruta_archivo)
        return {
            'title': audio.get('title', [None])[0],
            'album': audio.get('album', [None])[0],
            'artist': audio.get('artist', [None])[0]
        }
    except Exception as e:
        print(f'Error al leer los metadatos de {ruta_archivo}: {e}')
        return None

def buscar_en_musicbrainz(metadatos):
    try:
        resultado = musicbrainzngs.search_recordings(
            artist=metadatos['artist'], 
            release=metadatos['album'], 
            recording=metadatos['title']
        )
        if resultado['recording-list']:
            return resultado['recording-list'][0]['artist-credit'][0]['artist']['name']
        else:
            return None
    except Exception as e:
        print(f'Error al buscar en MusicBrainz: {e}')
        return None

def organizar_mp3_por_autor(carpeta_origen):
    carpeta_sin_id = os.path.join(carpeta_origen, 'SIN_ID')
    if not os.path.exists(carpeta_sin_id):
        os.makedirs(carpeta_sin_id)

    for raiz, carpetas, archivos in os.walk(carpeta_origen):
        for archivo in archivos:
            if archivo.lower().endswith('.mp3'):
                ruta_completa = os.path.join(raiz, archivo)
                metadatos = obtener_metadatos_mp3(ruta_completa)

                if metadatos is None:
                    print(f'Se salta el archivo: {archivo} debido a un error al leer los metadatos.')
                    continue  # Saltar al siguiente archivo

                if metadatos and (metadatos['artist'] or metadatos['title'] or metadatos['album']):
                    autor = metadatos['artist'] or buscar_en_musicbrainz(metadatos)
                    
                    if autor:
                        carpeta_destino = os.path.join(carpeta_origen, autor)
                        if not os.path.exists(carpeta_destino):
                            os.makedirs(carpeta_destino)
                        shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
                        print(f'Movido: {archivo} -> {carpeta_destino}')
                    else:
                        shutil.move(ruta_completa, os.path.join(carpeta_sin_id, archivo))
                        print(f'Movido a SIN_ID: {archivo}')
                else:
                    shutil.move(ruta_completa, os.path.join(carpeta_sin_id, archivo))
                    print(f'Movido a SIN_ID: {archivo}')

# Ruta de la carpeta que quieres organizar
carpeta_origen = 'd:/musica'

organizar_mp3_por_autor(carpeta_origen)
