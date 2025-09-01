#!/bin/bash

# Script para inicializar o projeto Caramelo com Docker

echo "🐾 Iniciando o projeto Caramelo..."

# Verificar se Docker e Docker Compose estão instalados
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não está instalado. Por favor, instale o Docker primeiro."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro."
    exit 1
fi

# Criar as pastas necessárias se não existirem
mkdir -p data
mkdir -p notebooks

echo "📁 Pastas criadas: data/ e notebooks/"

# Verificar se existe arquivo de dados
if [ ! -f "data/data.zip" ]; then
    echo "⚠️  Arquivo data.zip não encontrado em data/"
    echo "   Coloque seu dataset na pasta data/ antes de continuar"
    echo "   Você pode continuar sem o dataset para testar o ambiente"
fi

# Construir e iniciar o container
echo "🐳 Construindo e iniciando o container Docker..."
if [ "$EUID" -eq 0 ]; then
    docker-compose up -d --build
else
    sudo docker-compose up -d --build
fi

if [ $? -eq 0 ]; then
    echo "✅ Container iniciado com sucesso!"
    echo "🌐 Acesse o Jupyter em: http://localhost:8888"
    echo "📚 Documentação Docker: DOCKER_README.md"
    echo ""
    echo "Para parar o container, execute:"
    echo "   sudo docker-compose down"
else
    echo "❌ Erro ao iniciar o container"
    exit 1
fi
