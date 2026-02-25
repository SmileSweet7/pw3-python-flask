# Importando o flask para a aplicação
from flask import Flask, render_template
# Carregando o flask na variável "app"
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
#Variáveis com __ são variáveis de ambiente do Python 
#__name__ representa o nome da aplicação

# Criando a rota principal do site
# @ liga a rota a função ligada a ela
@app.route('/')
#def cria funções no Python
def home():
    return render_template('index.html')
@app.route('/lista')
def lista():
    return render_template('lista.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


# Iniciando o servidor na porta 5000
#app.py == principal
if __name__ == '__main__':
# Verificando se o arquivo gravado em __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# O método .run() inicia o servidor

