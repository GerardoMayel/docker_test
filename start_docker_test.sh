#!/bin/bash

# Navega al directorio del proyecto
cd /home/ubuntu/repos/docker_test

mkdir -p /app1/logs
mkdir -p /app2/logs

# Construye y levanta los contenedores
docker-compose up --build -d

echo "Contenedores desplegados exitosa mente"