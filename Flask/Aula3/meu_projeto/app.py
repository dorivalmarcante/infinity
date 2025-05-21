from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        return f'Nome: {nome}, Email: {email}'
    return render_template('index.html')
    
@app.route('/soma', methods=['GET', 'POST'])
def soma():
    mensagem = ''
    resultado = None
    if request.method == 'POST':
        n1 = request.form.get('n1', '').strip()
        n2 = request.form.get('n2', '').strip()
        if not n1 or not n2:
            mensagem = 'Erro: Ambos os campos devem ser preenchidos.'
        else:
            n1 = float(n1)
            n2 = float(n2)
            resultado = n1 + n2
    return render_template('soma.html', mensagem=mensagem, resultado=resultado)

@app.route('/produto', methods=['GET', 'POST'])
def produto():
    erro = ''
    resultado = ''
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        preco = request.form.get('preco', '').strip()
        qtd = request.form.get('qtd', '').strip()
        if not nome or len(nome) < 4:
            erro = 'Erro: O nome do produto deve ter pelo menos 4 letras.'
        elif not preco or float(preco) <= 0:
            erro = 'Erro: O valor deve ser maior que zero.'
        elif not qtd or int(qtd) <= 0:
            erro = 'Erro: A quantidade deve ser maior que zero.'
        else:
            resultado = 'Produto cadastrado com sucesso!'
    return render_template('produto.html', erro=erro, resultado=resultado)

if __name__=="__main__":
    app.run(debug=True)