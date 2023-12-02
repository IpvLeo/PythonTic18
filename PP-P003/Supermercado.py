

from os import remove, replace
from threading import local


def inserirNovoProduto(produtos):
    while(True):
        codigo = (input("Insira o codigo do produto com 13 digitos: "))
         
        if( codigo == '0'):
            print("Produto adiciconado")
            break
        elif(len(codigo) != 13):
            print("Tente novamente!") 
            continue
            
        nomeProduto = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto")
            
        novoProduto = {'codigo': codigo, 'nome': nomeProduto, 'preço': preco}
        produtos.append(novoProduto)
        return produtos
    

def excluirProduto(produtos):
    codigo = input("Insira o codigo do produto que quer excluir com 13 digitos: ")
    if( len(codigo) == 13):
            print("Produto excluido.")
            
    elif(len(codigo) != 13):
            print("Tente novamente!")        
    for produto in produtos:
        if(produto['codigo'] == codigo):
            produtos.remove(produto)
        print(f"produto removido", {codigo} ," da lista")
        break
        
    return produtos
       
       
       
def listaProdutos(produtos):
    for produto in produtos:
        print(f"Codigo: {produto['codigo']} \nNome do Produto: {produto['nome']} \nPreço: {produto['preço']}")
    return 
       
       
def alterarProdutos(produtos):
    codigo = input("Insira o codigo do produto que quer alterar com 13 digitos: ")
    novocodigo = input("insira o novo produto: ")
    for produto in produtos:
        if(codigo == produto['codigo']):
            novocodigo = codigo.replace( codigo , novocodigo)
            produto['codigo'] = novocodigo
            print(novocodigo)
            print(f"Codigo: {produto['codigo']}")
            
        
            
       

       

tabelaProdutos = []
inserirNovoProduto(tabelaProdutos)
listaProdutos(tabelaProdutos)
#excluirProduto(tabelaProdutos)
alterarProdutos(tabelaProdutos)






                  





