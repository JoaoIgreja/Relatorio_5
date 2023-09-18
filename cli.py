class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "sair":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class LivrosCLI(SimpleCLI):
    def __init__(self, livros_model):
        super().__init__()
        self.livros_model = livros_model
        self.add_command("criar", self.criar_livro)
        self.add_command("ler", self.read_livro)
        self.add_command("atualizar", self.atualizar_livro)
        self.add_command("deletar", self.delete_livro)

    def criar_livro(self):
        titulo = (input("Escreva o titulo: "))
        autor = input("Escreva o autor: ")
        ano = int(input("Escreva o ano: "))
        preco = int(input("Escreva o preco: "))
        self.livros_model.criar_livro(titulo, autor, ano, preco)

    def read_livro(self):
        id = input("Enter the id: ")
        livro = self.livros_model.read_livro_by_id(id)
        if livro:
            print(f"id: {livro['id']}")
            print(f"titulo: {livro['titulo']}")
            print(f"autor: {livro['autor']}")
            print(f"ano: {livro['ano']}")
            print(f"preco: {livro['preco']}")

    def atualizar_livro(self):
        id = input("Enter the id: ")
        titulo = input("Entre com o novo titulo: ")
        autor = int(input("Entre com o novo autor: "))
        ano = int(input("Entre com o novo ano: "))
        preco = int(input("Entre com o novo preco: "))
        self.livros_model.atualizar_livro(id, titulo, autor, ano, preco)

    def delete_livro(self):
        id = input("Enter the id: ")
        self.livros_model.delete_livro(id)

    def run(self):
        print("Bem vindo ao CLI de livros!")
        print("Available commands: criar, ler, atualizar, deletar, sair")
        super().run()
