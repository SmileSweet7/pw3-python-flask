#Importando o flask para a aplicação
from flask import  render_template, request, redirect, url_for

#criando a função principal para inicializar as routes
def init_app(app):
    #variaveis globais
    listaConsoles = ['Playstation 5', 'Xbox One', 'Super Nintendo', 'Atari', '3DS']
    
    listaGames = [{ 'titulo' : 'cs-go', 'ano' : 2012, 'categoria' : 'fps online', 'plataforma': 'PC(Windows)'}]
    #CRIANDO A ROTA PRINCIPAL DO SITE
    @app.route('/') 
    #def cria funções no python ]
    def home():
        return render_template('index.html')
    
    @app.route('/lista')
    def games():
        # Criando  variáveis para a rota de games
        titulo = "Jogos"
        ano = 2011
        categoria = "História"
        #Lista de jogadores (uma lista é um vetor/array)
        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
        # enviando as variaveis para op html
    
        return render_template('lista.html',
                           titulo = titulo,
                           ano = ano,
                           categoria = categoria,
                           jogadores=jogadores )

    @app.route('/formulario',  methods=['GET', 'POST'])
    def formulario():
        
       
         
        return render_template('formulario.html')
            
        
                        
        
    # Rota para cadastrar um jogo
    @app.route('/login', methods= [ 'GET' , 'POST' ])
    def login ():
        # Recebendo os dados do formulário e enviando para página
        
        if request.method == 'POST':
            # Aqui ele irá gravar os dados na lista de jogos
            listaGames.append({'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria'), 'plataforma' : request.form.get('plataforma')})
            # Aqui o usuário será redirecionado novamente para a página
            return redirect(url_for('login'))
        return render_template('login.html',
                               listaGames = listaGames)