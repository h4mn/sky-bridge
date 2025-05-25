#!/usr/bin/env bash

# Cores para output
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Se não houver argumentos, mostra o help
if [ $# -eq 0 ]; then
    echo -e "${CYAN}Sky Bridge CLI${NC}"
    echo
    echo "Uso: sb [comando] [opções]"
    echo
    echo "Comandos principais:"
    echo "  sb --help      :: Mostra ajuda"
    echo "  sb --version   :: Mostra versão"
    echo "  sb check      :: Comandos de verificação"
    echo "  sb config     :: Comandos de configuração"
    echo "  sb setup      :: Configura ambiente"
    exit 0
fi

# Repassa todos os argumentos para o CLI
python3 -m src.cli "$@"
