# app.py
from flask import Flask, render_template, request, redirect, url_for
from model import Produto

app = Flask(__name__)

# Rota principal (Read - Listar todos)
@app.route('/')
def index():
    produtos = Produto.buscar_todos()
    return render_template('lista_produtos.html', produtos=produtos)

# Rota para exibir o formulário de novo produto
@app.route('/novo')
def novo():
    return render_template('form_produto.html', produto=None)

# Rota para salvar um novo produto (Create)
@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    produto = Produto(nome=nome, descricao=descricao, preco=preco)
    produto.salvar()
    return redirect(url_for('index'))

# Rota para exibir o formulário de edição (preenche com dados)
@app.route('/editar/<int:id>')
def editar(id):
    produto = Produto.buscar_por_id(id)
    return render_template('form_produto.html', produto=produto)

# Rota para atualizar um produto existente (Update)
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    produto = Produto(id=id, nome=nome, descricao=descricao, preco=preco)
    produto.salvar() # O método salvar já lida com a atualização se o ID existir
    return redirect(url_for('index'))

# Rota para deletar um produto (Delete)
@app.route('/deletar/<int:id>')
def deletar(id):
    Produto.deletar(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)