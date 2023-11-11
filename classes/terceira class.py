from datetime import date

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #cls é metodo de criar classe
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, (date.today().year - ano))
    
    @staticmethod
    def ehMaiorIdade(idade):
        return idade > 18
    
def main():
    pessoa1 = Pessoa("Ana", 11)
    pessoa2 = Pessoa.apartirAnoNascimento("Biel", 2001)
    print(pessoa1.idade)
    print(pessoa2.idade)

    print(Pessoa.ehMaiorIdade(19))

if __name__ == '__main__':
    main()
