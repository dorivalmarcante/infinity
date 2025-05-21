# Atividade 01:
# Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
    
# Atividade 02:
# Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.

numero = 0
soma = 0
while numero <= 100:
    soma += numero
    numero += 1
print(f'O valor final da soma é {soma}')

# Atividade 03:
# Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um numero para ver sua tabuada: '))
contador = 1
while contador <= 10:
    print(f'{contador} X {numero} = {contador*numero}')
    contador += 1
print('FIM')


# Atividade 04:
# Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

numero = 10
while numero >=1:
    print(numero)
    numero -= 1
print('Feliz Ao Novo!')


# Atividade 05:
# Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.

numero = int(input('Digite um numero: '))
contador = 1
while contador <= numero:
    if contador%2!=0:
        print(contador)
    contador += 1
print('Fim do Programa')

# Atividade 06:
# Escreva um programa que solicite números ao usuário até que ele digite um número negativo, somando apenas os números positivos inseridos.

soma = 0
numero = 0
while numero >= 0:
    numero = int(input('Digite um numero: '))
    if numero >= 0:
        soma += numero
        print(soma)
        
print('Acabou')


