# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Documentar que el contenedor usa el puerto 5000
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]