# model.py
import mysql.connector
from db_config import dbConfig

class Produto:
    def __init__(self, nome: str, descricao: str, preco: float, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    @staticmethod
    def _get_connection():
        return mysql.connector.connect(**db_config)

    def salvar(self):
        """Salva um produto no banco. Se o ID existir, atualiza. Senão, cria um novo."""
        conn = Produto._get_connection()
        cursor = conn.cursor()
        if self.id:
            # Atualizar produto existente
            query = "UPDATE produtos SET nome = %s, descricao = %s, preco = %s WHERE id = %s"
            cursor.execute(query, (self.nome, self.descricao, self.preco, self.id))
        else:
            # Inserir novo produto
            query = "INSERT INTO produtos (nome, descricao, preco) VALUES (%s, %s, %s)"
            cursor.execute(query, (self.nome, self.descricao, self.preco))
            self.id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        """Retorna uma lista de todos os produtos do banco."""
        conn = Produto._get_connection()
        cursor = conn.cursor(dictionary=True) # dictionary=True facilita o acesso por nome de coluna
        query = "SELECT * FROM produtos"
        cursor.execute(query)
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return produtos

    @staticmethod
    def buscar_por_id(id):
        """Busca um produto específico pelo seu ID."""
        conn = Produto._get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM produtos WHERE id = %s"
        cursor.execute(query, (id,))
        produto = cursor.fetchone()
        cursor.close()
        conn.close()
        return produto

    @staticmethod
    def deletar(id):
        """Deleta um produto do banco de dados pelo seu ID."""
        conn = Produto._get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()