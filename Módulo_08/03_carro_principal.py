class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        return f"O veículo {self.marca} {self.modelo} está ligado."


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def ligar(self):
        return f"🏍️ {self.marca} {self.modelo} ({self.cilindradas}cc) deu a partida: BRRRAAAP!"

    def __str__(self):
        return f"Moto: {self.marca} {self.modelo}"


if __name__ == "__main__":
    minha_moto = Moto("Suzuki", "GSX-S750", 750)
#my baby
    print(minha_moto)

    print(minha_moto.ligar())