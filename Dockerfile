# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie os arquivos de dependências
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto do código
COPY . .

# Comando padrão para execução
CMD ["python", "-m", "src"]
