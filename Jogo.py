from peewee import *

db=SqliteDatabase("jogo.db")
class Modelo(Model):
    class Meta:
        database=db

class Jogo(Modelo):
    Placar = IntegerField()
    MinimoDaTemp = IntegerField()
    MaximoDaTemp = IntegerField()
    QuebraRecMinimo = IntegerField()
    QuebraRecMaximo = IntegerField() 

db.connect()
db.create_tables([Jogo])