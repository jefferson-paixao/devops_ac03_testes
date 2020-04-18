import pytest
from com.jefferson.bd import bancodedados

def test_criando_tabela():
    banco = bancodedados()
    assert  banco.criando_tabela() == 1, "Deveria ser 1"