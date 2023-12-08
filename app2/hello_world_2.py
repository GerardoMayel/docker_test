import os
import logging
import subprocess

# Lee la variable de entorno 'MESSAGE'. Si no está definida, usa 'Hello World 1' como predeterminado.
message = os.getenv('MESSAGE', 'Hello World 2 no definido mensaje 2')

# Configuración de logging
logging.basicConfig(filename='/app/logs/app1.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Registra el mensaje en el archivo de log
logging.info(message)

# Imprime el mensaje en la consola
print(message)

#Imprime Hello World
print("Hello World 2")
logging.info("Hello World 2")

#Imprime el resultado de pip freeze
subprocess.call(['pip', 'freeze'])

#guarda el resultado de pip freeze en un archivo
logging.info(subprocess.call(['pip', 'freeze']))












