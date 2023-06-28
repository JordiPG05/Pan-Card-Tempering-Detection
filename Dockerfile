# Usamos una imagen base de Python
FROM python:3.11.2

# Establecemos un directorio de trabajo
WORKDIR /app

# Copiamos los requerimientos de la aplicación
COPY requirements.txt requirements.txt

# Instalamos los requerimientos
RUN pip install -r requirements.txt

# Copiamos el código fuente de la aplicación
COPY . /app

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE $PORT

# Comando para ejecutar la aplicación
CMD gunicorn -b :$PORT app:app
