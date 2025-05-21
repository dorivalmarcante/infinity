# ATIVIDADE PRÁTICA 1 - Faça a definição de uma lista contendo os números de 1 até 5. Finalmente, utilize o print() para exibir os valores da lista.

numeros = [1,2,3,4,5]
for numero in numeros:
    print (numero)
    
# ATIVIDADE PRÁTICA 2 - Faça a definição de uma lista contendo as vogais. Finalmente, utilize o print() para exibir os valores da lista. 

vogais = ['a','e','i','o','u','A','E','I','O','U']
for vogal in vogais:
    print (vogal)

# ATIVIDADE PRÁTICA 3 - Defina uma lista com 5 itens que tenha, pelo menos, 3 classes diferentes. Utilize o print() para exibir o terceiro elemento dessa lista.

valores = [1,'b',3.0,4,'E',5.0,True]
print (valores[2])


lista = [*range(101)]
lista_diferente = [n for n in range(101)] # Para Performance
lista_comprehension = []
for i in range(101):
    lista_comprehension.append(i)
print(lista)
print(lista_diferente)
print(lista_comprehension)

# o melhor para adicionar varios dados é o list comprehension, pois é feito em C

# ATIVIDADE PRÁTICA 4 - Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados. Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição.

palestras = (
    ['Dorival','Marcos','Leticia','Matheus','Cecila'],
    ['Phyton','Matematica','Marketing','Design','Português'],
    ['Infinity','Uninove','IDH','Santa Marcelina','Unicastelo']
)
print(f'Palestrante: {palestras[0][2]}')
print(f'Curso: {palestras[1][2]}')
print(f'Instituição: {palestras[2][2]}')

# ATIVIDADE PRATICA 5 - Pedir para adicionar no sistema alunos, idades, notas e no final, exibir a media das idades e a media das notas

nomes = []
idades = []
notas = []
soma_idade = 0
soma_nota = 0

print('Sistema de calculo de medias (Para encerrar, digite * no campo nome)')

while True:
    nome = str(input('Digite o nome do aluno: '))
    if nome == '*':
        break
    nomes.append(nome)
    idade = int(input('Digite a idade do aluno: '))
    idades.append(idade)
    soma_idade += idade
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)
    soma_nota += nota
    
    
print(f'A media das idades é de {soma_idade/len(idades):.2f}')
print(f'A media das notas é de {soma_nota/len(notas):.2f}')
    