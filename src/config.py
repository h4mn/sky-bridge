""" Configuração do projeto. """

from pathlib import Path
from typing import Dict

from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Diretórios do projeto
BASE_DIR = Path(__file__).parent.parent
CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"