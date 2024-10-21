cont = []
favorito = []

def adicionar_contato(cont):
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email: ')
    novo_contato = {'nome': nome, 'telefone': telefone, 'email': email}

    fav = input('Deseja adicionar aos favoritos? (sim/não) ').lower()

    if fav == 'sim':
        favorito.append(novo_contato)

    cont.append(novo_contato)
    print(f'O contato {nome} foi adicionado com sucesso!')

def desmarcar(favorito):
    desfavoritar = input('Digite o nome do contato que deseja desfavoritar: ')

    for desfav in favorito:
        if desfav['nome'] == desfavoritar:
            favorito.remove(desfav)
            print(f'O contato {desfav["nome"]} foi removido dos favoritos.')
            return

    print('Contato não encontrado nos favoritos.')

def remover_contato(cont):
    nome_para_remover = input('Digite o nome do contato que deseja remover: ')

    for contato in cont:
        if contato['nome'] == nome_para_remover:
            cont.remove(contato)
            print(f'O contato {contato["nome"]} foi removido com sucesso.')
            return

    print('Contato não encontrado na lista.')

def editar(cont):
    nome_para_editar = input('Digite o nome do contato que deseja editar: ')

    for contato in cont:
        if contato['nome'] == nome_para_editar:
            print('O que deseja editar?')
            print('1. Nome')
            print('2. Telefone')
            print('3. Email')

            escolha = input('Escolha uma opção: ')

            if escolha == '1':
                novo_nome = input('Digite o novo nome: ')
                contato['nome'] = novo_nome
                print('Nome atualizado com sucesso!')

            elif escolha == '2':
                novo_telefone = input('Digite o novo telefone: ')
                contato['telefone'] = novo_telefone
                print('Telefone atualizado com sucesso!')

            elif escolha == '3':
                novo_email = input('Digite o novo email: ')
                contato['email'] = novo_email
                print('Email atualizado com sucesso!')

            return

    print('Contato não encontrado.')

while True:
    print('\nAPP DO FEFE')
    print('1. Adicionar Contato')
    print('2. Visualizar Contatos')
    print('3. Editar um contato')
    print('4. Ver favoritos')
    print('5. Tira um contato dos favoritos')
    print('6. Remover contato')
    print('7. Sair')

    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        adicionar_contato(cont)

    elif escolha == 2:
        print('\nTODOS OS CONTATOS')
        for visu in cont:
            print(f"Nome: {visu['nome']}, Telefone: {visu['telefone']}, Email: {visu['email']}")

    elif escolha == 3:
        editar(cont)

    elif escolha == 4:
        print('\nCONTATOS FAVORITOS: ')
        for visuz in favorito:
            print(f"Nome: {visuz['nome']}, Telefone: {visuz['telefone']}, Email: {visuz['email']}")

    elif escolha == 5:
        desmarcar(favorito)

    elif escolha == 6:
        remover_contato(cont)

    elif escolha == 7:
        print("Saindo do aplicativo...")
        break

    else:
        print('Opção inválida. Tente novamente.')
