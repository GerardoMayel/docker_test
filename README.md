# docker_hello_world_python

Contiene el código para los primeros pasos con Docker y Docker Compose

# Docker Test Project

Este proyecto demuestra el uso de Docker y Docker Compose para ejecutar dos simples aplicaciones Python en contenedores separados.

## Estructura del Proyecto

docker_test/
│
├── app1/
│ ├── Dockerfile
│ └── hello_world_1.py
│
├── app2/
│ ├── Dockerfile
│ └── hello_world_2.py
│
├── .dockerignore
└── docker-compose.yml

- `app1/` y `app2/`: Contienen los Dockerfiles y scripts Python para cada aplicación.
- `.dockerignore`: Especifica los archivos y directorios que Docker debería ignorar.
- `docker-compose.yml`: Define y orquesta los servicios de Docker.

## Requisitos

- Docker
- Docker Compose
