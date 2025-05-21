# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         data = request.form["nome"]
#         return f'Dados recebidos: {data}'
#     return '''
#         <form method="POST">
#             Nome: <input type="text" name="nome">
#             <input type="submit" value="Enviar">
#         </form>
#     '''

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/hello/<nome>')
def hello(nome):
    return render_template('index.html', nome=nome)
        
@app.route('/info')
def info():
    usuario = {'nome':'Ana','idade':25}
    return render_template('info.html',usuario=usuario)

@app.route('/lista')
def lista():
    itens = ['Maça','Banana','Laranja']
    return render_template('lista.html', itens=itens)

@app.route('/ano/<ano>')
def ano(ano):
    return f'Você nasceu em {ano}!'

@app.route('/submits', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        nome = request.form["nome"]
        idade = request.form["idade"]
        data = [nome,idade]
        return f'Dados recebidos: {data}'
    return '''
        <form method="POST">
            Nome: <input type="text" name="nome">
            Idade: <input type="text" name="idade">
            <input type="submit" value="Enviar">
        </form>
    '''
    
@app.route('/lista2')
def lista2():
    itens = ['Java','Python','JS']
    return render_template('lista2.html', itens=itens)
 
 


        
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
# EXERCICIO:
# Crie uma rota que aceita um parametro<int:ano> e exiba uma mensagem como "você nasceu em {ano}".
# Crie um formulario que usa os metodos GET e POST para enviar e exibir um nome
# Crie um template que exibe uma lista de produtos passada pelo backend
# Configure um template base com um cabeçalho e rodapé, e estenda-o em uma página especifica.