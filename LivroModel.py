from pymongo import MongoClient
from bson.objectid import ObjectId


class LivroModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def criar_livro(self, titulo: str, autor: str, ano: str, preco: str) -> str:
        try:
            livro_data = {"titulo": titulo,
                          "autor": autor, "ano": ano, "preco": preco}
            result = self.collection.insert_one(livro_data)
            livro_id = str(result.inserted_id)
            print(f"Livro {titulo} criado com o id: {livro_id}")
            return livro_id
        except Exception as error:
            print(f"Ocorreu um erro ao criar o livro: {error}")
            return None

    def ler_livro(self, livro_id: str) -> dict:
        try:
            livro = self.collection.find_one({"_id": ObjectId(livro_id)})
            if livro:
                return livro
            else:
                print("Livro não encontrado.")
                return None
        except Exception as error:
            print(f"Ocorreu um erro ao ler o livro: {error}")
            return None

    def atualizar_livro(self, livro_id: str, nome: str, autor: str) -> bool:
        try:
            result = self.collection.update_one({"_id": ObjectId(livro_id)}, {
                                                "$set": {"nome": nome, "autor": autor}})
            if result.modified_count > 0:
                print(f"Livro {livro_id} atualizado com sucesso.")
                return True
            else:
                print("Livro não encontrado.")
                return False
        except Exception as error:
            print(f"Ocorreu um erro ao atualizar o livro: {error}")
            return False

    def deletar_livro(self, livro_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(livro_id)})
            if result.deleted_count > 0:
                print(f"Livro {livro_id} deletado com sucesso.")
                return True
            else:
                print("Livro não encontrado.")
                return False
        except Exception as error:
            print(f"Ocorreu um erro ao deletar o livro: {error}")
            return False
