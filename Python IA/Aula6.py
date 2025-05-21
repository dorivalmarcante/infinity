# Desenvolver um programa de linha de comando que permite aos usuários gerenciar suas tarefas diárias, atribuindo-lhes prioridades e categorias. O projeto será organizado em várias
# partes e usará funções, listas, tuplas, dicionários, conjuntos e um ambiente virtual. Passos do projeto:
# Configuração do Ambiente Virtual:
# Crie um ambiente virtual usando o módulo venv
# Definição de Dados:
# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir informações como nome, descrição, prioridade e categoria. Você pode usar dicionários para representar as tarefas.
# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas como concluídas, exibir tarefas por prioridade ou categoria, e outras funcionalidades que desejar.
# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao usuário interagir com o programa.

tarefas = [
    {'nome': 'Dormir', 'descrição': 'Dormir', 'prioridade': 'máxima','categoria': 'pessoal','concluida':True},
    {'nome': 'Comprar leite e pão', 'descrição': 'Ir ao mercado para comprar leite e pão', 'prioridade': 'mínima', 'categoria': 'pessoal','concluida':True},
    {'nome': 'Responde e-mails urgentes', 'descrição': 'Responda e-mails que exigem resposta imediata', 'prioridade': 'máxima', 'categoria': 'financeiro','concluida':False},
    {'nome': 'Organizar mesa de trabalho', 'descrição': 'Arrumar a mesa de trabalho para melhorar a produtividade', 'prioridade': 'média', 'categoria': 'profissional','concluida':True},
    {'nome': 'Ligar para o médico', 'descrição': 'Agendar consulta médica', 'prioridade': 'média', 'categoria': 'pessoal','concluida':False},
    {'nome': 'Estudar para a prova de matemática', 'descrição': 'Estudar o conteúdo de matemática para a prova amanhã', 'prioridade': 'máxima', 'categoria': 'profissional','concluida':True},
    {'nome': 'Fazer exercícios físicos', 'descrição': 'Realizar a rotina de exercícios para manter a saúde', 'prioridade': 'média', 'categoria': 'pessoal','concluida':False},
    {'nome': 'Assistir um episódio da série favorita', 'descrição': 'Relaxar assistindo a série preferida para descansar', 'prioridade': 'mínima', 'categoria': 'pessoal','concluida':False}
]

escolha = int(input("Voce quer organizar as tarefas por: 1-Categoria - 2-Prioridade: "))

if escolha == 1:
    categoria_selecionada = int(input('Digite a categoria que quer visualizar: 1:Pessoal, 2:Profissional, 3:Financeiro: '))
    if categoria_selecionada==1:
        categoria_selecionada="pessoal"
    elif categoria_selecionada==2:
        categoria_selecionada="profissional"
    elif categoria_selecionada==3:
        categoria_selecionada="financeiro"
    else:
        print("Opção inválida, tente novamente!")
elif escolha == 2:
    prioridade_selecionada = int(input('Digite a prioridade que quer visualizar: 1:Mínima, 2:Média, 3:Máxima: '))
    if prioridade_selecionada==1:
        prioridade_selecionada="mínima"
    elif prioridade_selecionada==2:
        prioridade_selecionada="média"
    elif prioridade_selecionada==3:
        prioridade_selecionada="máxima"
    else:
        print("Opção inválida, tente novamente!")
else:
    print("Opção inválida, tente novamente!")

if escolha == 1:
    for dados in tarefas:
        if dados['categoria'] == categoria_selecionada:
            print(f"Nome: {dados['nome']}, Descrição: {dados['descrição']}, Prioridade: {dados['prioridade']}, Categoria: {dados['categoria']}, Concluída: {dados['concluida']}")
elif escolha == 2:
    for dados in tarefas:
        if dados['prioridade'] == prioridade_selecionada:
            print(f"Nome: {dados['nome']}, Descrição: {dados['descrição']}, Prioridade: {dados['prioridade']}, Categoria: {dados['categoria']}, Concluída: {dados['concluida']}")


# def add_tarefa():
#     nome_tarefa = input('Digite o nome da tarefa: ')
#     descricao_tarefa = input('Digite a descrição: ')
#     prioridade_tarefa = int(input('Digite 1:Mínima, 2:Média, 3:Máxima: '))
#     categoria_tarefa = int(input('Digite 1.Pessoal, 2:Profissional, 3:Lazer: '))
#     concluida_tarefa = int(input('Digite 1.Não concluida, 2.Concluída: '))
    
#     if prioridade_tarefa==1:
#         prioridade_tarefa="mínima"
#     elif prioridade_tarefa==2:
#         prioridade_tarefa="média"
#     elif prioridade_tarefa==3:
#         prioridade_tarefa="máxima"
#     else:
#         print("Opção inválida, tente novamente!")
#         return
    
#     if categoria_tarefa==1:
#         categoria_tarefa="Pessoal"
#     elif categoria_tarefa==2:
#         categoria_tarefa="Profissional"
#     elif categoria_tarefa==3:
#         categoria_tarefa="Financeiro"
#     else:
#         print("Opção inválida, tente novamente!")
#         return

#     if concluida_tarefa==1:
#         concluida_tarefa = False
#     elif concluida_tarefa==2:
#         concluida_tarefa = True
#     else:
#         print("Opção inválida, tente novamente!")
#         return
        
#     nova_tarefa = {
#         'nome': nome_tarefa,
#         'descricao':descricao_tarefa,
#         'prioridade':prioridade_tarefa,
#         'categoria':categoria_tarefa,
#         'concluida':concluida_tarefa
#     }
#     tarefas.append(nova_tarefa)

# add_tarefa()  