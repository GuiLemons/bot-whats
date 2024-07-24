# Use uma imagem base oficial do Python
FROM python:3.12

# Instale ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar a aplicação
CMD ["python", "app.py"]  # Substitua "app.py" pelo seu arquivo principal
