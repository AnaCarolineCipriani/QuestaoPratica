from Jogo import *

lista_placares=[]
jogos = Jogo.select()
for jogo in jogos:
    lista_placares.append(jogo.Placar)

def set_minimo_temporada(Placar):
    for j in jogos: 
        if min(lista_placares) > Placar:
            MinimoDaTemp = Placar
            lista_placares.append(MinimoDaTemp)
            return MinimoDaTemp
        else:
            MinimoDaTemp = min(lista_placares)
            lista_placares.append(MinimoDaTemp)
            return MinimoDaTemp


def set_maximo_temporada(Placar):
    for j in jogos:
        if max(lista_placares) < Placar:
            MaximoDaTemp = Placar
            lista_placares.append(MaximoDaTemp)
            return MaximoDaTemp
        else:
            MaximoDaTemp = max(lista_placares)
            lista_placares.append(MaximoDaTemp)
            return MaximoDaTemp

lista_recordes_max=[]
lista_recordes_min=[]
jogos = Jogo.select() 
for rec in jogos:
    lista_recordes_max.append(rec.QuebraRecMaximo) 
    lista_recordes_min.append(rec.QuebraRecMinimo)

def set_rec_maximo(Placar):
    for j in jogos:
        if max(lista_placares[:-1]) < Placar:
            QuebraRecMaximo = max(lista_recordes_max) + 1
            lista_recordes_max.append(QuebraRecMaximo)
            return QuebraRecMaximo
        else:
            for r in lista_placares:
                if r == Placar:
                    QuebraRecMaximo = max(lista_recordes_max)
                    return QuebraRecMaximo
                else:
                    QuebraRecMaximo = max(lista_recordes_max)
                    return QuebraRecMaximo

def set_rec_minimo(Placar):
    for j in jogos:
        if min(lista_placares[:-2]) > Placar:
            QuebraRecMinimo = max(lista_recordes_min) + 1
            lista_recordes_min.append(QuebraRecMinimo)
            return QuebraRecMinimo
        else:
            for r in lista_placares:
                if r == Placar:
                    QuebraRecMinimo = max(lista_recordes_min)
                    return QuebraRecMinimo
                else:
                    QuebraRecMinimo = max(lista_recordes_min)
                    return QuebraRecMinimo



def set_basketcoin():
    if len(lista_recordes_max) != 0:
        for i in range(len(lista_recordes_max)):
            if max(lista_recordes_max) > 0 and max(lista_recordes_max) < 3:
                basketcoin = 5
                return basketcoin
            elif max(lista_recordes_max) > 2 and max(lista_recordes_max) < 6:
                basketcoin = 10
                return basketcoin
            else:
                if max(lista_recordes_max) > 5:
                    basketcoin = 20
                    return basketcoin
    else:
        basketcoin = 0
        return basketcoin

  