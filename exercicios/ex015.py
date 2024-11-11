class veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def get_info(self):
        return f"Marca: {self.__marca}, Modelo: {self. __modelo}"
    
class carro(veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.__ano = ano

    def get_info(self):
        return f"Tipo: Carro, {super().get_info()}, Ano: {self.__ano}"

def exibir_info_veiculo(veiculo):
    print(veiculo.get_info())

carro_1 = carro("Mitsubishi", "Lancer", 2023)
carro_2 = carro("Subaru", "WRX", 2023)

exibir_info_veiculo(carro_1)
exibir_info_veiculo(carro_2)