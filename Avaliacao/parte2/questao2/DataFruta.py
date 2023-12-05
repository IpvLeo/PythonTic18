
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []       

    def getLista(self):
        return self.__lista       

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Nomes: "))
                for i in range(quantidade):
                    nome = input("Digite o nome: ")
                    self.__lista.append(nome)
                break
            except Exception as e:
                print(f"Erro: {e}")
        
    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        meio = len(lista_ordenada) // 2
        if (len(lista_ordenada) % 2 == 0):
            print(f"\nMediana dos nomes: {lista_ordenada[meio-1]}")
        else:
            print(f"Mediana dos nomes: {lista_ordenada[meio]}")

    def mostraMenor(self):
        print(f"\nMenor nome: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior nome: {max(self.__lista)}")

    def listarEmOrdem(self):
        print(f"Lista de nomes ordenada: {sorted(self.__lista)}")

    def __str__(self):
        return f"Lista de nomes: {', '.join(self.__lista)}"
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []    

    def getLista(self):
        return self.__lista    
    
    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Datas: \n"))
                for i in range(quantidade):
                    while True:
                        try:
                            print(f"Data {i + 1}:")
                            dia = int(input("Insira o dia: "))
                            mes = int(input("Insira o mês: "))
                            ano = int(input("Insira o ano: "))
                            data = Data(dia, mes, ano)
                            self.__lista.append(data)
                            break
                        except Exception as e:
                            print(f"Erro: {e}")
                break
            except Exception as e:
                print(f"Erro: {e}")
    
    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        meio = len(lista_ordenada) // 2
        if (len(lista_ordenada) % 2 == 0):
            print(f"\nMediana das datas: {lista_ordenada[meio-1]}")
        else:
            print(f"Mediana das datas: {lista_ordenada[meio]}")
     
    def mostraMenor(self):
        print(f"\nMenor data: {min(self.__lista)}")
        pass
    
    def mostraMaior(self):
        print(f"Maior data: {max(self.__lista)}")
        pass

    def listarEmOrdem(self):
        print(f"Lista de datas ordenada: {sorted(map(str, self.__lista))}")
    
    def __str__(self):
        return f"Lista de datas: {', '.join(map(str, self.__lista))}"

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []      

    def getLista(self):
        return self.__lista      

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Salários: "))
                for i in range(quantidade):
                    salario = float(input("Digite o salario: "))
                    self.__lista.append(salario)
                break
            except Exception as e:
                print(f"Erro: {e}")

    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        if len(lista_ordenada) % 2 == 0:
            print(f"\nMediana dos salarios: {(lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2}")
        else:
            print(f"Mediana dos salarios: {lista_ordenada[tamanho // 2]}")

    def mostraMenor(self):
        print(f"\nMenor salario: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior salario: {max(self.__lista)}")

    def listarEmOrdem(self):
        print(f"Lista de salários ordenada: {sorted(self.__lista)}")
    
    def __str__(self):
        return f"Lista de salarios: {self.__lista}"

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Idades: "))
                for i in range(quantidade):
                    idade = int(input("Digite a idade: "))
                    self.__lista.append(idade)
                break
            except Exception as e:
                print(f"Erro: {e}")
    
    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        if len(lista_ordenada) % 2 == 0:
            print(f"\nMediana das idades: {(lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2}")
        else:
            print(f"Mediana das idades: {lista_ordenada[tamanho // 2]}") 
    
    def mostraMenor(self):
        print(f"\Menor idade: {min(self.__lista)}")
    
    def mostraMaior(self):
        print(f"Maior idade: {max(self.__lista)}")

    def listarEmOrdem(self):
        print(f"Lista de idades ordenada: {sorted(self.__lista)}")

    def __str__(self):
        return f"Lista de idades: {self.__lista}"

def percorreNomeSalario(nomes, salarios):
    print("\nLista de nomes com salários:")
    for nome, salario in zip(nomes.getLista(), salarios.getLista()):
        print(f"Nome: {nome}, Salário: {salario}")

def imprimeSalarios10porcento(salarios):
    salarios10porcento = list(map(lambda salario: salario * (1 + 10 / 100), salarios.getLista()))
    total = sum(salarios10porcento)
    print("Salários reajustados: ")
    for salario in salarios10porcento:
        print(f"{salario:.2f}")
    print(f"\nTotal da folha de pagamento após reajuste: \n R$ {total:.2f}")

def imprimeDatasModificadas(datas):
    datas_modificadas = filter(lambda data: data.ano < 2019, datas.getLista())
    print("Datas após modificação:")
    for data in datas_modificadas:
        data.dia = 1
        print(data)
    
def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        print(lista)
        print("___________________")
    
    percorreNomeSalario(nomes, salarios)
    imprimeSalarios10porcento(salarios)
    imprimeDatasModificadas(datas)

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()