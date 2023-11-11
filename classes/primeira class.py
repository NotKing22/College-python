class Pessoa:
    #__texto__ significa private # O self é uma referência ao objeto da classe em que está sendo usado, permitindo que seus métodos e atributos sejam acessados e modificados. É utilizado como primeiro parâmetro em métodos de instância e permite a interação com as variáveis de instância da classe. 
    #
    # self = this.
    #
    def set_nome(self, nome):
        self.nome = nome

    def set_endereço(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender

    #init é um termo usado para "inicializar os objetos"
    def __init__(self, nome, endereço):
        self.set_nome(nome)
        self.set_endereço(endereço)

# HERANÇA DE CLASSES
class Profissional(Pessoa):

   # A função super() é utilizada para acessar os métodos e atributos da classe pai em uma classe filha, em casos de herança. Quando usada com argumentos, como super    (ClasseFilha, self).metodo(), a função retorna um objeto proxy que delega chamadas de método para uma classe pai ou irmã da classe atual. Dessa forma, a classe filha pode acessar e modificar os atributos e métodos da classe pai, além de incluir novos métodos e atributos específicos da classe filha. No exemplo apresentado, o super().__init__(nome, idade) é utilizado para chamar o construtor da classe pai Pessoa na classe filha Profissional.

    def __init__(self, nome, endereço, profissao):
        #mas nome e idade ja existem em Pessoa
        super().__init__(nome, endereço)
        self.profissao = profissao

    def imprimir(self):
        print(f"nome {self.get_nome()} e trabalha como ", self.profissao)


def main():
    pessoa1 = Pessoa("Peleco", "Rua: Das neves")
    pessoa2 = Pessoa("Elma Maria", "Rua: sim")

    print(' ')
    print(f"O nome da pessoa é {pessoa1.get_nome()}, e mora na {pessoa1.get_ender()}")
    print(f'O nome da pessoa2 é {pessoa2.get_nome()}, e mora na {pessoa2.get_ender()}')
    print(' ')
    p = Profissional("Ana", 25, "Balconista")
    p.imprimir()

if __name__ == '__main__':
    main()
    