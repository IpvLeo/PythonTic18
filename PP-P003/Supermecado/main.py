import os


produtos = []

def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')

def inserirProduto():
    codigo = input("Digite o código do produto (Deve conter 13 dígitos): ")
    while len(codigo) != 13 or not codigo.isdigit():
        print()
        print("Código inválido. Deve conter 13 dígitos numéricos.")
        print()
        codigo = input("Digite o código do produto (Deve conter 13 dígitos): ")

    nome = input("Digite o nome do produto: ")
    while not nome[0].isupper():
        print()
        print("Deve começar com uma letra maiúscula.")
        print()
        nome = input("Digite o nome do produto: ")

    preco = input("Digite o preço do produto: ")
    while not preco.replace('.', '', 1).isdigit():
        print()
        print("Preço inválido. (Use o formato por exemplo, 12.34).")
        print()
        preco = input("Digite o preço do produto: ")

    produto = {'codigo': codigo, 'nome': nome, 'preco': float(preco)}
    produtos.append(produto)
    print()
    print("Produto cadastrado com sucesso!")
    print()

def excluirProduto():
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print()
            print("Produto excluído com sucesso!")
            return
    print()    
    print("Produto não encontrado.")

def listarProdutos():
    limparTela()
    print("Lista de Produtos:")
    print("------------------")
    print()
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

def consultarPreco():
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"O preço de {produto['nome']} é R${produto['preco']:.2f}")
            return
    print()    
    print("Produto não encontrado.")
    print()

def menu():
    while True:
        print()
        print("[CADASTRO DE PRODUTOS]")
        print("=====================")
        print()
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        limparTela()

        if opcao == '1':
            inserirProduto()
        elif opcao == '2':
            excluirProduto()
        elif opcao == '3':
            listarProdutos()
        elif opcao == '4':
            consultarPreco()
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    menu()
