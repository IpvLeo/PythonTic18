

def inserirNovoProduto(produtos):
    codigo = (input("Digite o codigo do produto: "))
    
    while(True):
        if( codigo == '0'):
            print("Produto adiciconado")
            break


        elif(codigo != 13):
            print("Tente novamente!") 
            continue
        
        nomeProduto = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto")
        
        novoProduto = {'codigo': codigo, 'nome': nomeProduto, 'preço': preco}
        produtos.append(novoProduto)
        
        
produtos = []
inserirNovoProduto(produtos)


                  





