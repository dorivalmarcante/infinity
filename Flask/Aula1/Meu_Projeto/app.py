from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, mundo! Esta é a minha primeira aplicação Flask'
@app.route('/user/<nome>')
def saudar(nome):
    return f'Olá, {nome}!'
@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1,num2):
    return f'A soma de {num1} mais {num2} é {num1+num2}!'
@app.route('/sobre')
def sobre():
    return 'Esta é a página Sobre do projeto flask'
@app.route('/contato')
def contato():
    return 'Entre em contato pelo email: contato@flaskapp.com.'

tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False},
    {"id": 2, "titulo": "Ler um livro", "concluida": True},
    {"id": 3, "titulo": "Dormir", "concluida": False},
    {"id": 4, "titulo": "Viajar", "concluida": True},
    {"id": 5, "titulo": "Comer um Sushi com Polvo", "concluida": False},
]

@app.route('/tarefas')
def pegar_tarefas():
    return tarefas
@app.route('/tarefas/<titulo>')
def add_tarefa(titulo):
    tamanho_lista = len(tarefas)
    novo_id = tamanho_lista + 1
    novo_titulo = titulo
    novo_status = False
    nova_tarefa = {
        "id":novo_id,
        "titulo":novo_titulo,
        "concluido":novo_status
    }
    tarefas.append(nova_tarefa)
    return tarefas

@app.route("/att_tarefa/<int:id>/<novo_titulo>")
def atualizar_titulo(id,novo_titulo):
    for t in tarefas:
        if t["id"] == id:
            posicao = tarefas.index(t)
            tarefas[posicao]["titulo"] = novo_titulo
            return tarefas
    return "Não encontrei o id passado"

@app.route("/del_tarefa/<int:id>")
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return tarefas
    return "Não encontrei o id passado"

# Questão:
# Crie uma aplicação Flask para gerenciar uma biblioteca com as seguintes rotas:
livros = [
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "status": "disponível"},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "status": "emprestado"},
    {"titulo": "O Senhor dos Anéis","autor": "J.R.R. Tolkien","ano": 1954,"status": "disponível"},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "status": "emprestado"},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "status": "disponível"}
]
# GET /livros – Retorne uma lista de todos os livros cadastrados. Cada livro deve ter o título, autor, ano de publicação e status (disponível ou emprestado).
@app.route("/livros")
def listar_livros():
    return livros
# POST /livros/<titulo>/<autor>/<int:ano>/<status> – Receba os dados de um livro na URL (título, autor, ano de publicação e status de disponibilidade) e adicione-o à lista de livros.
@app.route('/livros/<titulo>/<autor>/<int:ano>/<status>')
def add_livro(titulo,autor,ano,status):
    novo_titulo = titulo
    novo_autor = autor
    novo_ano = ano
    novo_status = status
    novo_livro = {
        "titulo":novo_titulo,
        "autor":novo_autor,
        "ano":novo_ano,
        "status":novo_status
    }
    livros.append(novo_livro)
    return livros
# GET /livros/<titulo> – Receba o título de um livro e retorne os detalhes do livro correspondente, como autor, ano de publicação e status.
@app.route('/livros/<titulo>')
def detalhe_livro(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            return f"Título: {livro['titulo']}, Ano: {livro['ano']}, Autor: {livro['autor']}, Status: {livro['status']}"
    return "Não encontrei o titulo passado"
# PUT /livros/<titulo>/<status> – Receba o título do livro e um novo status ("disponível" ou "emprestado") e atualize o status do livro com esse título.
@app.route('/livros/<titulo>/<status>')
def novo_status(titulo,status):
    for livro in livros:
        if livro["titulo"] == titulo:
            livro["status"] = status
            return f"Título: {livro['titulo']}, Ano: {livro['ano']}, Autor: {livro['autor']}, Status: {livro['status']}"
    return "Não encontrei o titulo passado" 
# DELETE /livros/<titulo> – Receba o título de um livro e remova esse livro da lista de livros cadastrados.

# Ajustei o caminho da rota para /livros/deletar/<titulo>, pois estava a mesma que era usada para retornar os detalhes do livro, então ele nao apagava, pq rodava a de exibir os detalhes primeiro

@app.route("/livros/deletar/<titulo>")
def deletar_livro(titulo):
    for livro in livros:
        if livro["titulo"] == titulo:
            livros.remove(livro)
            return livros
    return "Não encontrei o título passado"


if __name__ == '__main__':
    app.run(debug=True)
    
