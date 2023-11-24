from datetime import datetime

class ItemTarefa:
    def __init__(self, titulo=None, descricao=None, data_vencimento=None, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento or datetime.now()
        self.concluida = concluida

class ListaTarefas:
    itens = []

    @classmethod
    def inserir(cls, item):
        cls.itens.append(item)
        print("Tarefa cadastrada com sucesso.")

    @classmethod
    def listar(cls, filtrar_concluidas=None):
        print("Lista de Tarefas:")
        for i, item in enumerate(cls.itens):
            if filtrar_concluidas is None or item.concluida == filtrar_concluidas:
                print(f"{i}. {item.titulo} - {'Concluída' if item.concluida else 'Não Concluída'}")

    @classmethod
    def pesquisar_por_palavra_chave(cls, palavra_chave):
        print(f"Tarefas contendo a palavra-chave '{palavra_chave}':")
        for i, item in enumerate(cls.itens):
            if palavra_chave.lower() in (item.titulo.lower() + item.descricao.lower()):
                print(f"{i}. {item.titulo}")

    @classmethod
    def marcar_como_concluida(cls, indice):
        cls.itens[indice].concluida = True
        print(f"Tarefa '{cls.itens[indice].titulo}' marcada como concluída.")

    @classmethod
    def excluir(cls, indice):
        titulo = cls.itens[indice].titulo
        del cls.itens[indice]
        print(f"Tarefa '{titulo}' excluída com sucesso.")

    @classmethod
    def mostrar_estatisticas(cls):
        total_tarefas = len(cls.itens)
        total_concluidas = sum(1 for item in cls.itens if item.concluida)

        print("Estatísticas:")
        print(f"Total de Tarefas: {total_tarefas}")
        print(f"Tarefas Concluídas: {total_concluidas}")
        print(f"Tarefas Não Concluídas: {total_tarefas - total_concluidas}")

if __name__ == "__main__":
    print("[CADASTRO DE TAREFAS]")
    print("=====================")
    print()

    while True:
        print("Escolha uma opção:")
        print("1. Cadastrar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Listar tarefas concluídas")
        print("4. Listar tarefas não concluídas")
        print("5. Pesquisar por palavra-chave")
        print("6. Marcar como concluída")
        print("7. Excluir tarefa")
        print("8. Mostrar estatísticas")
        print("9. Sair")
        print()

        opcao = input("Opção: ")

        if opcao.isdigit():
            escolha = int(opcao)

            if escolha == 1:
                item = ItemTarefa(
                    input("Informe o título da tarefa: "),
                    input("Informe descrição da tarefa: "),
                    datetime.strptime(input("Qual a data de vencimento da tarefa? (Ex.: xx/xx/xxxx ou xx/xx/xx): "), "%d/%m/%Y")
                )
                ListaTarefas.inserir(item)
            elif escolha in [2, 3, 4]:
                ListaTarefas.listar(filtrar_concluidas=(escolha == 3))
            elif escolha == 5:
                ListaTarefas.pesquisar_por_palavra_chave(input("Digite a palavra-chave para pesquisa: "))
            elif escolha == 6:
                ListaTarefas.marcar_como_concluida(int(input("Informe o índice da tarefa a ser marcada como concluída: ")))
            elif escolha == 7:
                ListaTarefas.excluir(int(input("Informe o índice da tarefa a ser excluída: ")))
            elif escolha == 8:
                ListaTarefas.mostrar_estatisticas()
            elif escolha == 9:
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida.")
        else:
            print("Opção inválida.")
