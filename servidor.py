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
                QuebraRecMinimo = set_quebra_recorde_minimo(int(placar_atual)), 
                QuebraRecMaximo = set_quebra_recorde_maximo(int(placar_atual)))
    
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

count = 0 

def set_quebra_recorde_minimo(Placar):
    QuebraRecMinimo = 0
    for j in jogos: 
        if min(lista_placares[:-2]) > Placar:
            QuebraRecMinimo = 1
            print(lista_placares)
            return QuebraRecMinimo
        else:
            QuebraRecMinimo = 0
            print(lista_placares)
            return QuebraRecMinimo


def set_quebra_recorde_maximo(Placar):
    QuebraRecMaximo = 0
    for j in jogos: 
        if max(lista_placares[:-1]) < Placar or max(lista_placares[:-1]) == Placar:
            QuebraRecMaximo = 1
            return QuebraRecMaximo
        else:
            QuebraRecMaximo = 0
            return QuebraRecMaximo


app.run(debug=True)