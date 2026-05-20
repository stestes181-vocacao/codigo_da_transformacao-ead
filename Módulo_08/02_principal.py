class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):  
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo) 
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        return f"⚡ {self.marca} {self.modelo} - luxo sustentável com {self.autonomia_bateria}km de autonomia."

    def __str__(self):
        return f"{self.marca} {self.modelo} ⚡ {self.autonomia_bateria}km"


if __name__ == "__main__":
    meu_carro = CarroEletrico("BMW", "i7", 520)

    print(meu_carro.exibir_info())

    print(meu_carro)