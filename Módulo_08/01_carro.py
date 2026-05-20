 
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"✨ Um belo {self.marca} {self.modelo}, puro luxo.")

    def __str__(self):
        return f"{self.marca} {self.modelo} 💎"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"⚡ {self.marca} {self.modelo} - luxo sustentável com {self.autonomia_bateria}km de autonomia.")

    def __str__(self):
        return f"{self.marca} {self.modelo} ⚡ ({self.autonomia_bateria}km)"


carro1 = Carro("BMW", "M8")
carro2 = CarroEletrico("BMW", "i7", 600)


carro1.exibir_info()
carro2.exibir_info()

print(carro1)
print(carro2)