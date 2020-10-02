import pytest

from Jogo import *
from funcoes import *

#Os testes dependem do que está inserido no banco de dados. 
#Os testes abaixo foram feitos com apenas 2 jogos cadastrados no banco de dados : placares 12, 24 e 10.

def test_set_minimo_temporada():
    assert set_minimo_temporada(10) == 10
    assert set_minimo_temporada(24) == 10

def test_set_maximo_temporada():
    assert set_maximo_temporada(23) == 24
    assert set_maximo_temporada(12) == 24
    assert set_maximo_temporada(37) == 37

def test_set_rec_maximo():
    assert set_rec_maximo(24) == 1
    assert set_rec_maximo(25) == 2

def test_set_rec_minimo():
    assert set_rec_minimo(10) == 1 

def test_set_basketcoin():
    assert set_basketcoin() == 5
    

