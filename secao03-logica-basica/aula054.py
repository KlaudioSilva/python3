'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista.
'''
lista = []

while True:
    print('-' * 5, 'Lista de Compras', '-' * 5)

    print(f'Lista de compras atual {lista}')
    print()
    print('Escolha uma das opções:')
    print('[ 1 ] Acrescentar item')
    print('[ 2 ] Remover item')
    print('[ 3 ] Modificar item')
    print('[ 4 ] Sair do programa')
    print()

    opcao = int(input('Digite aqui a opção escolhida: '))

    if opcao == 1:
        print(f'Lista atual = {lista}')
        item = input('Digite o nome do novo item da lista: ')
        lista.append(item)
        print(f'O item "{item}" foi adicionado à lista.')
    elif opcao == 2:
        item = input('Digite o nome do item que será removido: ')

        if item in lista:
            lista.remove(item)
            print(f'O item {item} foi removido da lista.')
        else:
            print(f'O item {item} não existe nessa lista.')
            continue
    elif opcao == 3:
        item = input('Digite o nome do item que deseja modificar: ')
        if item in lista:
            indice = lista.index(item)
            item_trocado = input(f'Digite o nome do item que vai substituir {item}: ')
            lista[indice] = item_trocado

            print(f'O item {item} foi substituído por {item_trocado}.')
            continue
        else:
            print(f'O item {item} não está nessa lista')
            continue
    elif opcao == 4:
        print('Saindo do Programa.')
        break
    else:
        print('Digite apenas uma das opções: "1", "2", "3" ou "4"')