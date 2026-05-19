# 1. Definição da Classe Mãe (Base)
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"{self.marca} {self.modelo}"


# 2. Definição da Classe Filha (Herança)
class CarroEletrico(Carro):  
    def __init__(self, marca, modelo, autonomia_bateria):
        # O super().__init__ puxa os atributos 'marca' e 'modelo' da classe mãe
        super().__init__(marca, modelo) 
        self.autonomia_bateria = autonomia_bateria

    # Sobrescreve o método exibir_info para incluir a autonomia
    def exibir_info(self):
        return f"⚡ {self.marca} {self.modelo} - luxo sustentável com {self.autonomia_bateria}km de autonomia."

    # Método especial para representação em texto do objeto
    def __str__(self):
        return f"{self.marca} {self.modelo} ⚡ {self.autonomia_bateria}km"


# --- EXEMPLO DE USO PRÁTICO ---
if __name__ == "__main__":
    # Criando uma instância (objeto) da classe CarroEletrico
    meu_carro = CarroEletrico("BYD", "Seal", 520)

    # Testando o método exibir_info()
    print(meu_carro.exibir_info())

    # Testando o método __str__() (ativado automaticamente ao usar print no objeto)
    print(meu_carro)