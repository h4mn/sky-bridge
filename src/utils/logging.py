""" Configuração de logging para Sky Bridge. """
import logging
import sys
from pathlib import Path

def setup_logging(
    level: str = "INFO",
    log_file: Path | None = None
) -> logging.Logger:
    """Configura o logging para a aplicação."""
    logger = logging.getLogger("sky_bridge")
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (opcional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger