# 1. Classe Mãe (Base)
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        return f"O veículo {self.marca} {self.modelo} está ligado."


# 2. Classe Filha (Herança)
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        # O super() evita que você tenha que refazer self.marca e self.modelo
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Sobrescrita de método (Polimorfismo): mudando o comportamento do método ligar
    def ligar(self):
        return f"🏍️ {self.marca} {self.modelo} ({self.cilindradas}cc) deu a partida: BRRRAAAP!"

    # Personalizando a exibição do objeto
    def __str__(self):
        return f"Moto: {self.marca} {self.modelo}"


# --- TESTANDO O CÓDIGO ---
if __name__ == "__main__":
    # Criando uma moto (que herda de Veiculo)
    minha_moto = Moto("Honda", "CB 500X", 471)

    # 1. Testando o método mágico __str__
    print(minha_moto) 
    # Saída: Moto: Honda CB 500X

    # 2. Testando o método ligar() modificado na classe Moto
    print(minha_moto.ligar()) 
    # Saída: 🏍️ Honda CB 500X (471cc) deu a partida: BRRRAAAP!