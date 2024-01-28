# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self):
        self.cor = 'preto'
        self.modelo = 'punto'
        self.velocidade = 0
        self.velocidade_maxima = 162
        self.ligado = False

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
        self.velocidade = 0
    
    def acelerar(self):

        if not self.ligado:
          return
        
        if self.velocidade < self.velocidade_maxima:
            self.velocidade += 1
    
    def desacelerar(self):

        if not self.ligado:
          return
        
        if self.velocidade > 0:
            self.velocidade -= 1
    
    def __str__(self) -> str:
        return f'Cor: {self.cor}\tModelo: {self.modelo}\tLigado: {self.ligado}\tVelocidade: {self.velocidade}'


# Crie uma instância da classe carro.
punto = Carro()
print(punto)
# Faça o carro "andar" utilizando os métodos da sua classe.
punto.ligar()
punto.acelerar()
print(punto)
# Faça o carro "parar" utilizando os métodos da sua classe.
punto.desacelerar()
punto.desligar()
print(punto)