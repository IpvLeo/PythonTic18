
def reajusta_dez_porcento(lista_colaboradores):
    for empregado in lista_colaboradores:
        empregado['salario'] *= 1.1

def ler_arquivo_e_armazenar_lista(nome_arquivo):
    lista_colaboradores = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            empregado = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'ano_nascimento': int(dados[2]),
                'RG': dados[3],
                'ano_admissao': int(dados[4]),
                'salario': float(dados[5])
            }
            lista_colaboradores.append(empregado)
    return lista_colaboradores


def exibirInfor(lista_colaboradores):
    for empregado in lista_colaboradores:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}")
        print(f"Ano de Nascimento: {empregado['ano_nascimento']}")
        print(f"RG: {empregado['RG']}")
        print(f"Ano de Admissão: {empregado['ano_admissao']}")
        print(f"Salário: R${empregado['salario']:.2f}")
        print("\n")


if __name__ == "__main__":
    arqFuncionarios = "funcionarios.txt"

    listaFuncionarios = ler_arquivo_e_armazenar_lista(arqFuncionarios)


    print("Informações antes do reajuste:")
    exibirInfor(listaFuncionarios)

   
    reajusta_dez_porcento(listaFuncionarios)

    print("\nInformações após o reajuste:")
    exibirInfor(listaFuncionarios)