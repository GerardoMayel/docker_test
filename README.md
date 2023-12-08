Docker Test Project

Descripción

Este proyecto es una demostración de cómo usar Docker y Docker Compose para ejecutar dos aplicaciones Python en contenedores separados. Cada aplicación imprime un mensaje personalizado en la consola y registra este mensaje, junto con otros datos, en archivos de log.

Estructura del Proyecto

Copy code
tu_proyecto/
│
├── app1/
│ ├── Dockerfile
│ └── hello_world_1.py
│
├── app2/
│ ├── Dockerfile
│ └── hello_world_2.py
│
├── logs/
│ ├── app1/
│ └── app2/
│
└── docker-compose.yml
app1/ y app2/: Directorios que contienen los Dockerfiles y scripts Python para cada aplicación.
logs/: Directorio donde se almacenan los logs generados por cada aplicación.
docker-compose.yml: Define y orquesta los servicios de Docker.
Requisitos

Docker
Docker Compose
Configuración y Uso

Para configurar y utilizar este proyecto:

Clona el Repositorio: git clone https://github.com/GerardoMayel/docker_test.git.
Navega al Directorio del Proyecto: cd docker_test.
Construye y Levanta los Contenedores: docker-compose up --build.
Personalización

Puedes personalizar los mensajes impresos por cada aplicación modificando las variables de entorno en docker-compose.yml.

Logs

Los logs de cada aplicación se almacenan en el directorio logs/ correspondiente en el host. Estos logs incluyen los mensajes impresos y la salida del comando pip freeze.

Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de seguir las buenas prácticas de desarrollo y mantener la estructura y estilo del código existente.

Licencia

Este proyecto está bajo la Licencia MIT.
