import os
import logging
import subprocess

# Configuración de logging
logging.basicConfig(filename='/app/logs/app1.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Lee la variable de entorno 'MESSAGE'. Si no está definida, usa 'Hello World 1' como predeterminado.
message = os.getenv('MESSAGE', 'Hello World 1 no definido mensaje 1')

# Registra el mensaje en el archivo de log y lo imprime en la consola
logging.info(message)
print(message)

# Imprime y registra "Hello World"
print("Hello World 1")
logging.info("Hello World 1")

# Ejecuta pip freeze y captura la salida
try:
    requirements_output = subprocess.check_output(['pip', 'freeze'], text=True)
    print(requirements_output)
    logging.info(requirements_output)
except subprocess.CalledProcessError as e:
    logging.error("Error al ejecutar pip freeze: " + str(e))

