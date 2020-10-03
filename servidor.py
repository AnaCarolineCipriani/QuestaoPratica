from flask import Flask, redirect, render_template, request, session
from Jogo import *
from funcoes import * 



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

    """
    Jogo.create(Placar=12,                       #Utilizei para a primeira insercao no banco de dados
                MinimoDaTemp = 12,               #Rodo a aplicacao com esses valores, insiro um numero qualquer no registrar jogo
                MaximoDaTemp = 12,               #E volto com os metodos acima para rodar novamente e normalmente
                QuebraRecMinimo = 0, 
                QuebraRecMaximo = 0)    
    """
    
    return redirect("/listar_jogos")


def show_basketcoin():
    bkc = set_basketcoin()
    return bkc


@app.route("/listar_jogos")
def listar_jogos():
    return render_template("listar_jogos.html", jogos=Jogo.select(), bkb = show_basketcoin())



app.run(debug=True)