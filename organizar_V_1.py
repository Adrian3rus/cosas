import os
import shutil

def organizar_archivos_por_extension(carpeta_origen):
    # Lista de extensiones a organizar
    extensiones = {
        'mp3': 'Audio',
        'mp4': 'Video',
        'jpg': 'Imagenes',
        'png': 'Imagenes',
        'jpeg': 'Imagenes',
        'gif': 'Imagenes',
        'svg': 'Imagenes',
        'txt': 'Documentos',
        'pdf': 'Documentos',
        'exe': 'Programas',
        'rar': 'Comprimidos',
        'zip': 'Comprimidos',
        'iso': 'ISOS',
        # Agrega más extensiones y carpetas aquí si es necesario
    }

    # Crea una carpeta para extensiones no reconocidas
    carpeta_otros = os.path.join(carpeta_origen, 'Otros')
    if not os.path.exists(carpeta_otros):
        os.makedirs(carpeta_otros)

    # Recorre todos los archivos y subcarpetas en la carpeta origen
    for raiz, carpetas, archivos in os.walk(carpeta_origen):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)

            if os.path.isfile(ruta_completa):
                # Obtiene la extensión del archivo
                extension = archivo.split('.')[-1].lower()

                # Verifica si la extensión está en el diccionario
                if extension in extensiones:
                    # Carpeta de destino según la extensión
                    carpeta_destino = os.path.join(carpeta_origen, extensiones[extension])

                    # Crea la carpeta si no existe
                    if not os.path.exists(carpeta_destino):
                        os.makedirs(carpeta_destino)

                    # Mueve el archivo a la carpeta correspondiente
                    try:
                        shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
                        print(f'Movido: {archivo} -> {carpeta_destino}')
                    except Exception as e:
                        print(f'Error al mover {archivo}: {e}')
                else:
                    # Mueve los archivos con extensiones no reconocidas a la carpeta 'Otros'
                    try:
                        shutil.move(ruta_completa, os.path.join(carpeta_otros, archivo))
                        print(f'Movido a Otros: {archivo}')
                    except Exception as e:
                        print(f'Error al mover {archivo} a Otros: {e}')
            else:
                print(f'No es un archivo: {archivo}')

# Ruta de la carpeta que quieres organizar
carpeta_origen = 'c:/users/adria/Downloads'

organizar_archivos_por_extension(carpeta_origen)
