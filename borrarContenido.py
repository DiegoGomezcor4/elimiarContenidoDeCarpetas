import os
import shutil

def borrar_contenido_carpeta(ruta_carpeta):
    try:
        # Obtener la lista de archivos y carpetas en la carpeta
        contenido = os.listdir(ruta_carpeta)

        # Iterar sobre cada elemento en la carpeta
        for elemento in contenido:
            ruta_elemento = os.path.join(ruta_carpeta, elemento)

            # Verificar si es un archivo y borrarlo
            if os.path.isfile(ruta_elemento):
                os.remove(ruta_elemento)
            # Si es una carpeta, borrar su contenido de manera recursiva
            elif os.path.isdir(ruta_elemento):
                shutil.rmtree(ruta_elemento)

        print(f"Contenido de la carpeta '{ruta_carpeta}' borrado exitosamente.")
    except Exception as e:
        print(f"Error al borrar contenido: {e}")

# Ruta de la carpeta que quieres vaciar
ruta_carpeta_a_borrar_1 = "C:/Users/Test/Downloads/Excel/"
ruta_carpeta_a_borrar_2 = "C:/Users/Test/Downloads/Pdf/"
ruta_carpeta_a_borrar_3 = "C:/Users/Test/Downloads/Ejecutables/"

# Llamar a la función para borrar el contenido
borrar_contenido_carpeta(ruta_carpeta_a_borrar_1)
borrar_contenido_carpeta(ruta_carpeta_a_borrar_2)
borrar_contenido_carpeta(ruta_carpeta_a_borrar_3)
