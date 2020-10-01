from flask import Flask, redirect, render_template, request, session
from Jogo import *



app = Flask(__name__, static_url_path="", template_folder="templates", static_folder="static")

@app.route("/")
def iniciar():
    return render_template ("index.html")


@app.route("/form_inserir_jogo")
def form_inserir_jogo():
    return render_template("inserir_jogo.html")



@app.route("/inserir_jogo", methods=["POST"])
def inserir_jogo():
    placar_atual = request.form["placar"]
    if int(placar_atual) < 0 or int(placar_atual) > 1000:
        return render_template("exceptions.html")
    Jogo.create(Placar=placar_atual,
                MinimoDaTemp = set_minimo_temporada(int(placar_atual)),
                MaximoDaTemp = set_maximo_temporada(int(placar_atual)),
                QuebraRecMinimo = set_rec_minimo(int(placar_atual)), 
                QuebraRecMaximo = set_rec_maximo(int(placar_atual)))
    
    return redirect("/listar_jogos")


@app.route("/listar_jogos")
def listar_jogos():
    return render_template("listar_jogos.html", jogos=Jogo.select())



lista_placares=[]
jogos = Jogo.select()
for jogo in jogos:
    #print(jogo.Placar)
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
                    QuebraRecMinimo = max(lista_recordes_max)
                    return QuebraRecMinimo

app.run(debug=True)