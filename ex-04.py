
class Veiculo:

    def __init__(self, nome, velocidade, km):
        self.nome = nome;
        self.velocidade = velocidade;
        self.km = km;

    def capacidade_assentos(self, capacidade):
        print("-------------------------------------")
        print(f"A capacidade máxima de assentos do veículo {self.nome} é de {capacidade}")
        print("-------------------------------------")

    def toStrg(self):
        print(f"nome = {self.nome}")
        print(f"A velocidade máxima é {self.velocidade}")
        print(f"Quilometros percorridos por litro: {self.km}")
        print("-------------------------------------")

meu_carro = Veiculo("fusca", 180, 10)
meu_carro.toStrg()

class onibus(Veiculo):
    pass

    def capacidade_assentos(self, capacidade=70):
        return super().capacidade_assentos(capacidade=70)

onibus_escolar = onibus("Onibus", 100, 10)
onibus_escolar.toStrg()
onibus_escolar.capacidade_assentos()


