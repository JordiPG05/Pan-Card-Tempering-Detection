# Usamos una imagen base de Python  
FROM python:3.11.2 

# Instalamos las dependencias necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-dev

# Establecemos un directorio de trabajo  
WORKDIR /app  

# Copiamos los requerimientos de la aplicación  
COPY requirements.txt requirements.txt  

# Instalamos los requerimientos  
RUN pip install -r requirements.txt  

# Copiamos el código fuente de la aplicación  
COPY . /app   
COPY app.py .  
COPY config.py .  

# Exponemos el puerto en el que se ejecutará la aplicación  
EXPOSE 5000  

# Comando para ejecutar la aplicación  
CMD ["python", "app.py"]