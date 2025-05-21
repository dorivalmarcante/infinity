#Atividade 01:
# Tabuada de um Número:  Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um numero: '))
for i in range(1,11):
    print(f'{numero}X{i} = {numero*i}')

# Atividade 02:
# Soma de Números de 1 a 100:  Crie um programa que use um laço for para somar todos os números de 1 a 100 e exiba o resultado.

soma = 0
for i in range(101):
    soma +=i

print (soma)
    
# Atividade 03:
# Caractere por Caractere:  Escreva um programa que solicite uma palavra ao usuário e use um laço for para exibir cada caractere da palavra em uma linha separada.

palavra = str(input('Digite uma palavra: '))
for i in palavra:
    print(i)

# Atividade 04:
# Contagem Regressiva de 10 a 1:  Desenvolva um programa que use um laço for para fazer uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

for i in range(10,0,-1):
    print(i)
print('Feliz Ano Novo')

# Atividade 05:
# Contagem de Números Positivos e Negativos: Escreva um programa que solicite ao usuário 10 números e use um laço for com uma condicional para contar quantos são positivos e quantos são negativos.

positivo = 0
negativo = 0
for i in range (1,11):
    numero = int(input(f'Digite o {i}º numero:'))
    if numero >= 0 :
        positivo += 1
    else:
        negativo += 1
print(f'Voce digitou {positivo} numeros positivos e {negativo} numeros negativos')

# Atividade 06:
# Soma de Números Pares: Escreva um programa que use um laço for para somar todos os números pares de 1 a 50 e exiba o resultado final.

soma=0
for i in range (1,51):
    if i % 2 ==0:
        soma += i
print(soma)

# Atividade 07:
# Contagem de Vogais em uma Palavra: Crie um programa que solicite uma palavra ao usuário e use um laço for com uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

palavra = str(input('Digite uma palavra: ')).lower()
soma = 0
for i in palavra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        soma +=1
if soma == 1:
    print(f'A palavra digitada tem {soma} vogal')
elif soma > 1:
    print(f'A palavra digitada tem {soma} vogais')
else:
    print(f'A palavra digitada nao tem vogais')                  

# Atividade 08:
# Cálculo de Média de Notas: Escreva um programa que solicite 5 notas de alunos. Use um laço for para somar as notas e uma condicional para exibir a média e a classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).

media = 0
soma = 0
for i in range(1,6):
    nota = float(input(f'Digite a {i}ª nota: '))
    soma += nota
media = soma / 5
if media >= 6:
    print(f'Sua nota é {media} e voce foi aprovado')
else:
    print(f'Sua nota é {media} e voce foi reprovado')

# Atividade 09:
# Verificar Números Pares e Impares com Interrupção: Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

par = 0
impar = 0
for i in range (1,21):
    if i == 15:
        break
    elif i % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'{par} numeros são par e {impar} numeros são impar.')

# Atividade 10:
# Contar Números Positivos e Negativos: Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.

positivo = 0
negativo = 0
for i in range (1,11):
    numero = int(input(f'Digite o {i}º numero:'))
    if numero == 0:
        print('Voce digitou 0. Esse numero encerra o programa. Saindo...')
        break
    if numero > 0 :
        positivo += 1
    else:
        negativo += 1
print(f'Voce digitou {positivo} numeros positivos e {negativo} numeros negativos')

# Atividade 11:
# Verificar Múltiplos de 5 e Parar: Escreva um programa que use um laço for para imprimir números de 1 a 30. Use uma condicional para verificar se um número é múltiplo de 5 e outro para verificar se é maior que 20 e interromper o loop com break.

for i in range (1,31):
    if i % 5 ==0:
        print(i)
    if i > 20:
        break

# Atividade 12:
# Soma de Números com Desconto: Peça ao usuário para inserir 5 preços de produtos. Use um laço for para calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e interrompa o loop com break.

soma = 0
for i in range (1,6):
    preco = float(input(f'Digite o preço do {i}º produto: '))
    soma += preco
    if soma > 100:
        soma -= soma * 0.1
print(f'Total final com desconto (se aplicável): R${soma:.2f}')
        