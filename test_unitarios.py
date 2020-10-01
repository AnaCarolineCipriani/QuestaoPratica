import pytest

from Jogo import *
from funcoes import *



def test_set_minimo_temporada():
    lista_placares=[12,24]
    assert set_minimo_temporada(10) == 10

def test_set_maximo_temporada():
    lista_placares=[12,24]
    assert set_maximo_temporada(28) == 28

def test_set_rec_maximo():
    lista_placares=[12]
    assert set_rec_maximo(24) == 1

def test_set_rec_minimo():
    lista_placares=[12,24]
    assert set_rec_minimo(10) == 1 