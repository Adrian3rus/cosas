import os
import shutil

def organizar_archivos_por_extension(carpeta_origen):
    # Lista de extensiones a organizar
    extensiones = {
        'mp3': 'Audio',
        'mp4': 'Video',
        'jpg': 'Imagenes',
        'png': 'Imagenes',
        'jpeg': 'imagenes',
        'gif': 'imagenes',
        'svg': 'imagenes',
        'txt': 'Documentos',
        'pdf': 'Documentos',
        'exe' : 'programas',
        'rar': 'comprimidos',
        'zip': 'comprimidos',
        'iso': 'ISOS',
        # Agrega más extensiones y carpetas aquí si es necesario
    }

    # Recorre todos los archivos en la carpeta origen
    for archivo in os.listdir(carpeta_origen):
        ruta_completa = os.path.join(carpeta_origen, archivo)
        
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
                shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))
                print(f'Movido: {archivo} -> {carpeta_destino}')
            else:
                print(f'Extensión no reconocida: {archivo}')
        else:
            print(f'No es un archivo: {archivo}')

# Ruta de la carpeta que quieres organizar
carpeta_origen = 'c:/users/adria/Downloads'
# C:\Users\adria\Downloads
organizar_archivos_por_extension(carpeta_origen)
