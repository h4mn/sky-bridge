""" Teste de funcionalidade básica. """
import pytest

from src import __version__

def test_version():
    """ Testa se a versão é uma string. """
    assert isinstance(__version__, str)