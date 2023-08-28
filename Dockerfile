# Use a imagem oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do bot para o contêiner
COPY . .

# Comando para executar o bot
CMD ["python", "main.py"]

# Para buildar a imagem e rodar container 
# docker build -t discord-bot .
# docker run discord-bot