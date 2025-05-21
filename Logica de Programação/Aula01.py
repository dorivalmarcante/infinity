# Atividade 01
idade1 = int(input('Digite a primeira idade: '))
idade2 = int(input('Digite a segunda idade: '))
if idade1 > idade2:
    print('A primeira idade digitada é maior')
elif idade2 > idade1:
    print('A segunda idade digitada é maior')
else:
    print('As duas idades são iguais!')

#Atividade 02
palavra1 = str(input('Digite a primeira palavra: '))
palavra2 = str(input('Digite a segunda palavra: '))
if palavra1 == palavra2:
    print('As palavras digitadas são iguais.')
else:
    print('As palavras digitadas são diferentes.')

#Atividade 03
idade = int(input('Digite a sua idade: '))
if idade < 18:
    print('Você só pode dirigir com 18 anos e habilitado!')
elif idade >= 18:
    habilitado = str(input('Voce é habilitado? (S/N): '))
    if habilitado == "S" or habilitado == "s":
        print('Voce está pronto para dirigir, boa viagem!')
    elif habilitado == "N" or habilitado == "n":
        print('Você ja tem idade para tirar habilitação, mas ainda não pode dirigir!')
    else:
        print('Valor Inválido!')

#Atividade 04
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if nota1 >= 6 and nota2 >=6:
    print('Parabens, voce foi aprovado!')
else:
    print('Você nao foi aprovado!')

#Atividade 05
preco = float(input('Digite o valor do produto desejado: '))
desconto = (preco / 100) * 5
preco -= desconto
print(f'O preço com desconto é R$ {preco}')

#Atividade 06
numero = float(input('Digite um numero qualquer: '))
dobro = numero
dobro *= 2
print(f'O dobro de {numero} é {dobro}')

#Atividade 07
frase1 = str(input('Digite uma frase: '))
letra = str(input('Digite uma letra: '))
resultado = letra in (frase1)
if resultado == True:
    print(f'A letra {letra} está presente na frase!')
else:
    print(f'A letra {letra} não está presente na frase!')

#Atividade 08
frase2 = str(input('Digite uma frase: '))
palavra = str(input('Digite uma palavra: '))
resultado = palavra in (frase2)
if resultado == True:
    print(f'A palavra {palavra} está presente na frase')
else:
    print(f'A palavra {palavra} não está presente na frase')

#Atividade 09
numero = int(input('Digite um numero: '))
if numero%2==0:
    print(f"{numero} é Par!")
else:
    print(f"{numero} é Impar!")
    
#Atividade 10    
nota = float(input('Digite sua nota:'))
if nota >= 6:
    print("Parabéns, você foi aprovado!")
else:
    print("Não foi dessa vez, estude mais!")
    
#Atividade 11
num1 = int(input('Digite um valor qualquer: '))

if num1 >=0 and num1%2==0:
    print(f'O numero {num1} é Par e Positivo!')
elif num1 >=0 and num1%2!=0:
    print(f'O numero {num1} é Impar e Positivo!')
elif num1 <0 and num1%2==0:
    print(f'O numero {num1} é Par e Negativo!')
else:
    print(f'O numero {num1} é Impar e Negativo!')
    
#Atividade 12
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (altura * altura) / peso
print (imc)
    

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print (imc)

