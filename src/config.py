""" Configuração do projeto. """

# from dotenv import load_dotenv

from src.types import Path

# Carrega variáveis de ambiente
# load_dotenv()

# Diretórios do projeto
BASE_DIR = Path(__file__).parent.parent
CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
