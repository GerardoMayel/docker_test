#!/bin/bash

# Navega al directorio del proyecto
cd /home/ubuntu/repos/docker_test

# Construye y levanta los contenedores
docker-compose up --build -d

echo "Contenedores desplegados exitosa mente"