from flask import Flask, redirect, render_template, request, session
from Jogo import *



app = Flask(__name__, static_url_path="", static_folder="templates")

@app.route("/")
def iniciar():
    return render_template ("index.html")


@app.route("/form_inserir_jogo")
def form_inserir_jogo():
    return render_template("inserir_jogo.html")



@app.route("/inserir_jogo", methods=["POST"])
def inserir_jogo():
    placar_atual = request.form["placar"]
    Jogo.create(Placar=placar_atual,
                MinimoDaTemp = set_minimo_temporada(int(placar_atual)),
                MaximoDaTemp = set_maximo_temporada(int(placar_atual)),
                QuebraRecMinimo = 0, 
                QuebraRecMaximo = 0)
    
    return redirect("/")


@app.route("/listar_jogo")
def listar_jogo():
    return render_template("listar_jogos.html", jogos=Jogo.select())



lista_placares=[]
jogos = Jogo.select()
for jogo in jogos:
    print(jogo.Placar)
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
            #print(lista_placares) teste
            #print(Placar) teste
            MaximoDaTemp = Placar
            lista_placares.append(MaximoDaTemp)
            return MaximoDaTemp
        else:
            MaximoDaTemp = max(lista_placares)
            lista_placares.append(MaximoDaTemp)
            print(lista_placares)
            return MaximoDaTemp



app.run(debug=True)