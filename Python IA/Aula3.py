# ATIVIDADE PRÁTICA 5 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

conjunto = {
    42, 879, 315, 607, 251, 789, 924, 118, 300, 459,
    640, 58, 233, 781, 925, 399, 167, 710, 824, 597,
    15, 222, 841, 367, 143, 190, 929, 6, 762, 110,
    284, 915, 358, 479, 871, 982, 288, 746, 530, 25,
    709, 214, 53, 604, 839, 497, 363, 816, 68, 381,
    772, 134, 197, 721, 889, 375, 44, 980, 627, 163,
    943, 296, 589, 123, 240, 990, 503, 318, 65, 951,
    177, 12
}
maior = 0
menor = 1000
for i in conjunto:
    if i > maior:
        maior = i
print(f'No conjunto digitado, o maior valor é {maior}')        
for i in conjunto:
    if i < menor:
        menor = i
print(f'No conjunto digitado, o menor valor é {menor}')
soma = sum(conjunto)
print (f'A soma dos valores do conjunto é {soma}')

# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a media de cada aluno, imprima o numero de alunos com média maior ou igual a 7.0
medias = []
media = 0
soma = 0
for i in range(2):
    for j in range(4):
        nota = float(input(f'Digite a {j}ª nota do {i}º aluno: '))
        soma += nota
        media = soma / 4
    media = medias.append(media)
    soma = 0
    media = 0
for k in medias:
    if medias >= 7:
        print (medias)
        
        
        
lista = []
for i in range(10):
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    nota4 = float(input('Digite a nota 4: '))
    media - (nota1+nota2+nota3+nota4) / 4
    if media >= 7:
        print('Media adicionada a lista')
        lista.append(media)
    else:
        continue
print(f'A quantidade de alunos com a média maior que 7 é de : {len(lista)}')
