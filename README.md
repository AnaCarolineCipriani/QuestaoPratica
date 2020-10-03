# QuestaoPratica

## Bem vindo ao BasketHub! 

### O BasketHub é uma plataforma feita para auxiliar o usuário a acompanhar seus registros de pontuação de cada partida de basquete que jogou com seus amigos! 

## Tecnologias Utilizadas 
Python
Flask
Peewee
HTML
CSS

## Instalações 
<p>Instalar a linguagem de programação Python <strong>(incluindo o pip)</strong> - https://www.python.org/downloads/ </p>
<p>Instalar um editor de código-fonte (Visual Studio Code) - https://code.visualstudio.com/download</p>
<p>No Visual Studio Code, ir em Terminal - Novo Terminal e digitar : </p>
<p>pip install flask </p>
<p>pip install peewee </p>
<p>pip install pytest </p>

## Rodar o Projeto 
<p> Ir no arquivo servidor.py, clicar com o botão direito do mouse no editor, e clicar em Run Python File in Terminal </p>
<p>Após isso, irá aparecer uma rota no terminal : 127.0.0:5000 </p>
<p>CTRL + Clique com o botão esquerdo do mouse</p>
<p>A aplicação irá abrir na web</p>
<p> <strong> Clique em Registrar Jogo, então, será redirecionado(a) para a interface de consulta de dados</strong></p>
<p><strong> Dessa forma, poderá continuar registrando os jogos e acompanhando as pontuações</strong></p>

<img src="public/rodar_api.gif">

## Testes unitários 
<p>Para rodar os testes unitários, é necessário encerrar a aplicação e abrir um novo terminal.</p>
<p>Após abrir esse novo terminal, digitar :  python -m pytest </p>

<img src="public/test_unitario.gif">

## Destaques
<p>O BasketHub tem uma "moeda" local chamada BasketCoin. Irá aparecer no canto superior direito da tela se: </p>
<p>O Recorde Máximo > 0 e < 3 : 5 BasketCoins </p>
<p>O Recorde Máximo > 2 e < 6 : 10 BasketCoins</p>
<p>O Recorde Máximo > 5 : 20 BasketCoins </p>

### ! IMPORTANTE : O banco de dados (jogo.db) do último commit que está aqui no projeto não deve ser apagado
### Ele deve ser utilizado para todo o processo de inserção e consultas no banco de dados. 

## Imagens 
<img src="public/index.png">
<img src="public/listar.png">
<img src="public/registrar.png">
<img src="public/exception.png">



