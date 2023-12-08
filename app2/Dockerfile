# app2/Dockerfile
FROM python:3.8
WORKDIR /app

# Crear un entorno virtual en el contenedor y activarlo
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

#crear el archivo de log
#RUN mkdir -p /app/logs

#copair el archivo de requirements
COPY requirements.txt .

#actialisar pip y instalar requirements
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

#copiar el archivo hello_world_2.py
COPY . .
#ejecutar el archivo hello_world_2.py
CMD ["python", "hello_world_2.py"]