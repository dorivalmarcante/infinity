#Atividade 01:
#Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.

contador = 1
while contador <= 10:
    print (contador)
    contador += 1
    
#Atividade 02:
#Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.

contador2 = 0
soma = 0

while contador2 <= 100:
    soma = soma + contador2
    contador2 += 1
    
print(soma)

# Atividade 03:
# Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).

valor = int(input('Digite um valor para ver a tabuada: '))
contador3 = 1
while contador3 <= 10:
    print(f'{valor} X {contador3} = {valor*contador3}')
    contador3 += 1
print('FIM')

# Atividade 04:
# Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

contador4 = 10
while contador4 >=1:
    print(contador4)
    contador4 -= 1
    
print('Feliz Ano Novo!')

# Atividade 05:
# Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.

numero = int(input('Digite um numero: '))
count = 0
while count <= numero:
    if count%2!=0:
        print(count)
    count += 1

# Atividade 06:
# Escreva um programa que solicite números ao usuário até que ele digite um número negativo, somando apenas os números positivos inseridos.

soma = 0
while True:
    numero = int(input('Digite um numero:'))
    if numero >= 0:
        soma += numero
    elif numero < 0:
        break
print(soma)

# Atividade 09:
# Crie um programa que use um laço while para contar de 1 a 10 e termine quando atingir 10.
count = 1
while True:
    if count <= 9:
        count+=1
    else:
        break
print(f'valor chegou a {count}')

numero = 0
soma = 0

while soma <= 50:
    numero = int(input('Digite um numero: '))
    soma += numero
print(f'O resultado da soma total é {soma}')

# Soma de Números Pares:
# Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

soma =0
numero=0
while numero <=100:
    if numero%2==0:
        soma +=numero
    numero+=1
print(f'O resultado da soma é {soma}')

# Números Ímpares de 1 a 50:
# Escreva um programa que use um laço while para exibir todos os números ímpares de 1 a 50.

numero=0
while numero <=50:
    if numero%2!=0:
        print(numero)
    numero+=1
    
# Sequência de Fibonacci:
# Faça um programa que use um laço while para exibir os primeiros 20 termos da sequência de Fibonacci.
    
ultimo=0
sequencia=1
contador=0

while contador < 20:
    print(ultimo)
    temp = ultimo
    ultimo = sequencia
    sequencia = temp + sequencia
    contador +=1
    

# Fatorial de um Número:
# Desenvolva um programa que solicite um número ao usuário e use um laço while para calcular o fatorial desse número.

for i in range(100,2):
    print(i)