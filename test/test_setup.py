""" Teste de funcionalidade básica. """
import pytest

from src import __version__


class TestBasicFunctionality(object):
    """Classe de teste para funcionalidade básica."""

    def setUp(self) -> None:
        """Configuração inicial para os testes."""
        # Aqui você pode adicionar qualquer configuração necessária antes de cada teste

    def tearDown(self) -> None:
        """Limpeza após os testes."""
        # Aqui você pode adicionar qualquer limpeza necessária após cada teste

    def test_import(self) -> None:
        """Testa se o módulo pode ser importado."""
        assert __version__ is not None, "O módulo não pôde ser importado."

    def test_version(self) -> None:
        """Testa se a versão é uma string."""
        assert isinstance(__version__, str)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
