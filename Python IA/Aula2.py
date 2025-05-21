# ATIVIDADE PRÁTICA 1
# Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: "maçã","banana","uva","laranja" e "morango". Em seguida, imprima o conjunto.

frutas = set()
frutas.add('maça')
frutas.add('banana')
frutas.add('uva')
frutas.add('laranja')
frutas.add('morango')
print(frutas)

# ATIVIDADE PRÁTICA 2
# Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

print ('banana' in frutas)

# ATIVIDADE PRÁTICA 3
# Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele: "morango" , "cereja" e "framboesa". Em seguida, imprima o conjunto.

frutas_vermelhas = set()
frutas_vermelhas.add('morango')
frutas_vermelhas.add('cereja')
frutas_vermelhas.add('framboesa')
print(frutas_vermelhas)

# ATIVIDADE PRÁTICA 4
# Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

frutas_vermelhas.remove('cereja')
print(frutas_vermelhas)

# ATIVIDADE PRÁTICA 5
# Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

a = {'phyton','java','C#'}
b = {'html','css','javascript'}
a.update(b)
print(a)
print(a|b) #essa é outra forma de juntar conjuntos
conjunto_geral = a.union(b)
print(conjunto_geral) #mais uma forma de fazer

# ATIVIDADE PRÁTICA 6
# Crie um programa que recebe dois conjuntos e exibe a interseção deles.

a = {'phyton','java','C#','javascript'}
b = {'html','css','javascript'}
a.intersection(b)
print(a)

# ATIVIDADE PRÁTICA 7
# Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

a = ['phyton','java','C#','javascript']
b = ['html','css','javascript']



# ATIVIDADE PRÁTICA 8
# Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.

pessoas = {
    'Dorival':'43',
    'Marcela':'42',
    'Roberto': '41'
    }
print(pessoas)

# ATIVIDADE PRÁTICA 9
# Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

for nome,idade in pessoas.items():
    print(f'Nome: {nome} e idade: {idade}')
    
    
lista_nomes = ['Igor','Leticia','Jefferson']
lista_idades = ['24','32','31']

usuarios = dict(zip(lista_nomes, lista_idades))
print(usuarios)

# ATIVIDADE PRÁTICA 10
# Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.

lista2 = dict()
for i in range(3):
    lista2['nome'] = str(input('Digite um nome:'))
    lista2['idade'] = str(input('Digite uma idade:'))

print(lista2)


dicionario = {}

while True:
    opcao = int(input('Digite 1-Para Sair e 2-Para cadastrar um nome e idade: '))
    
    if opcao == 1:
        break
    else:
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')

        dicionario[nome] = idade
        print(dicionario)


# ATIVIDADE PRÁTICA 11
# Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.




# ATIVIDADE PRÁTICA 12
# Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.




# ATIVIDADE PRÁTICA 13
# Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.



# ATIVIDADE PRÁTICA 14
# Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.




# ATIVIDADE PRÁTICA 15
# Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.





# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos - passo 1
# Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas:
# Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: 'nome','idade','notas'. As notas devem ser armazenadas em uma tupla.




# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos - passo 2
# Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada. Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la. Aluno com Melhor Média: O programa deve identificar e exibir o aluno com a melhor média de notas.