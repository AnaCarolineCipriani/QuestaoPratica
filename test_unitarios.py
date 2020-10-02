import pytest

from Jogo import *
from funcoes import *

#Os testes dependem do que está inserido no banco de dados. 
#Os testes abaixo foram feitos com apenas 2 jogos cadastrados no banco de dados : placares 12 e  24.

def test_set_minimo_temporada():
    assert set_minimo_temporada(10) == 10
    assert set_minimo_temporada(24) == 10

def test_set_maximo_temporada():
    assert set_maximo_temporada(28) == 28
    assert set_maximo_temporada(12) == 24

def test_set_rec_maximo():
    assert set_rec_maximo(24) == 1
    assert set_rec_maximo(11) == 0

def test_set_rec_minimo():
    assert set_rec_minimo(10) == 1 
    

