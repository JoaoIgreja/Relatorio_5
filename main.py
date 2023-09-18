from writeAJson import writeAJson
from database import Database
from LivroModel import LivroModel
from cli import LivrosCLI

db = Database(database="biblioteca", collection="livros")
livroModel = LivroModel(database=db)

LivrosCLI = LivrosCLI(livroModel)
LivrosCLI.run()
