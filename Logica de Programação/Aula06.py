# Conversão de Unidades - Crie um programa que converta metros para centímetros. Peça ao usuário para digitar um valor em metros, armazene em uma variável e converta para centímetros. 

metro = float(input('Digite o valor em metros para conversão para centimetros: '))
print(f'O valor em centimetros é de {metro*100}.')

# Cálculo de Área - Crie um programa que calcule a área de um retângulo. Peça ao usuário para digitar a largura e a altura, armazene em variáveis e calcule a área. 

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
print(f'A área do retangulo é {altura*largura}.')


# Cálculo de IMC - Crie um programa que calcule o Índice de Massa Corporal (IMC). Peça ao usuário para digitar seu peso e altura, armazene em variáveis e calcule o IMC.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura*altura)
print(f'Seu imc é de {imc:.2f}')

# Cálculo de Juros Simples - Crie um programa que calcule o valor futuro de um investimento usando a fórmula de juros simples. Peça ao usuário para digitar o capital inicial, a taxa de juros e o tempo de aplicação.

capital_inicial = float(input('Digite o capital inicial: '))
taxa_juros = float(input('Digite a taxa de juros: '))
tempo_aplicacao = int(input('Digite o tempo de aplicação: '))
print(f'O valor final será {capital_inicial * taxa_juros * tempo_aplicacao}.')

# Verificando a Média do Aluno - Crie um algoritmo que peça quatro notas de um aluno, calcule a média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

soma = 0

for i in range (1,5):
	nota = float(input(f'Digite a {1}ª nota do aluno: ')) 
	soma += nota
if soma / 4 >= 6:
	print('Aprovado')
else:
	print('Reprovado')

# Algoritmo de Cálculo de Desconto - Desenvolva um algoritmo que calcule o preço de um produto após aplicar um desconto. Solicite o preço original e o percentual de desconto.

preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o percentual de desconto: '))
valor_final = preco - (preco * (desconto/100))
print(f'O preço final do produto é {valor_final}')


# Algoritmo de Conversão de Tempo - Desenvolva um algoritmo que converta uma quantidade de segundos fornecida pelo usuário em horas, minutos e segundos.

segundos = int(input('Digite os segundos para conversão: '))
segundoss = segundos
minutos = segundos / 60
horas = minutos / 60

hora = 0
minuto = 0
while segundos >= 3600:
    hora+=1
    segundos -=3600
while segundos > 60:
    minuto+=1
    segundos -=60
print(f'{segundoss} segundos equivalem a {hora} hora(s), {minuto} minuto(s) e {segundos} segundo(s).')

# Algoritmo de Conversão de Temperatura - Crie um algoritmo que converta uma temperatura de Celsius para Fahrenheit. Solicite ao usuário a temperatura em Celsius e exiba o resultado em Fahrenheit.

f = float(input('Digite a temperatura em Fº: '))
c = 5/9 * (f-32)
print(c)

#Categoria de Idade - Desenvolva um programa que peça a idade do usuário e informe se ele é criança, adolescente, adulto ou idoso.

idade = int(input('Digite a sua idade: '))
if idade >0 and idade < 12:
    print('Você é uma criança.')
elif idade >=12 and idade <20:
    print('Voce é um adolescente.')
elif idade>=20 and idade <60:
    print('Voce é um adulto')
else:
    print('Voce é um idoso.')
    

#Classificação de Notas - Crie um programa que solicite uma nota de 0 a 100 e informe o conceito (A, B, C, D, E) com base na nota.

nota = float(input('Digite uma nota entre 0 e 100: '))
if nota < 0 or nota >100:
    print('Numero invalido. Encerrando.')
elif nota>= 0 and nota<20:
    print('Sua nota foi E')
elif nota>=20 and nota<40:
    print('Sua nota foi D')
elif nota>=40 and nota<60:
    print('Sua nota foi C')
elif nota>=60 and nota<80:
    print('Sua nota foi B')
else:
    print('Sua nota foi A')

# Verificar Signo - Escreva um programa que peça o dia e o mês de nascimento do usuário e informe o signo correspondente.

dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento (numero): '))
if mes == 3 and dia >= 21 or mes == 4 and dia <=20:
    print('Seu signo é Áries')
elif mes == 4 and dia >= 21 or mes == 5 and dia <=20:
    print('Seu signo é Touro')
elif mes == 5 and dia >= 21 or mes == 6 and dia <=20:
    print('Seu signo é Gemeos')
elif mes == 6 and dia >= 21 or mes == 7 and dia <=21:
    print('Seu signo é Cancer')
elif mes == 7 and dia >= 22 or mes == 8 and dia <=22:
    print('Seu signo é Leão')
elif mes == 8 and dia >= 23 or mes == 9 and dia <=22:
    print('Seu signo é Virgem')
elif mes == 9 and dia >= 23 or mes == 10 and dia <=22:
    print('Seu signo é Libra')
elif mes == 10 and dia >= 23 or mes == 11 and dia <=21:
    print('Seu signo é Escorpião')
elif mes == 11 and dia >= 22 or mes == 12 and dia <=20:
    print('Seu signo é Sagitário')
elif mes == 12 and dia >= 21 or mes == 1 and dia <=20:
    print('Seu signo é Capricórnio')
elif mes == 1 and dia >= 21 or mes == 2 and dia <=21:
    print('Seu signo é Aquário')
elif mes == 2 and dia >= 22 or mes == 3 and dia <=20:
    print('Seu signo é Peixes')
else:
    print('Dia ou mês invalidos')


# Sistema de Login - Desenvolva um programa que simule um sistema de login. O programa deve pedir o nome de usuário e a senha e verificar se correspondem a um usuário pré-cadastrado. Exiba mensagens apropriadas para login bem-sucedido ou falha.

usuario = 'admin'
senha = 'A1b2C3'
tentativas = 0
while True:
    user = input('Digite seu usuario: ')
    passw = input('Digite sua senha: ')
    if user == usuario and passw == senha:
        print('Login aprovado. Acesso liberado!')
        break
    elif tentativas == 2:
        print('Limite de tentativas esgotados. Encerrando!')
        break
    else:
        print('Usuario ou senha invalidos. Tente novamente!')
        tentativas += 1

# Contagem Regressiva - Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

regressiva = 10

while regressiva >0:
    print(regressiva)
    regressiva -= 1
print('Feliz ano novo!!')

# Contagem Regressiva - Desenvolva um programa que use um laço for para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

for i in range (10,0,-1):
    print(i)
print('Feliz ano novo!!')

# Soma de Números Pares - Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.
numero = 0
soma = 0
while numero <= 100:
    if numero %2 == 0:
       soma += numero
    numero +=1
print(soma)

# Tabuada de um Número - Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um numero para ver sua tabuada: '))
for i in range(1,11):
    print(f'{numero}X{i} = {numero*i}')
    
# Verificação de Palíndromo - Escreva um programa que solicite uma palavra ao usuário e use um laço while para verificar se a palavra é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = str(input('Digite uma frase: ')).replace(" ","")
print(palavra)
if palavra == palavra[::-1]:
    print("É um palindromo.")
else:
    print("Não é um palindromo.")


# Sistema de Login com Tentativas Limitadas: Desenvolva um programa que simule um sistema de login. O programa deve solicitar o nome de usuário e senha até que o usuário insira as credenciais corretas ou até que o número máximo de tentativas seja atingido. Use um laço while com uma condicional para verificar as credenciais e limitar as tentativas.

usuario = 'admin'
senha = 'A1b2C3'
tentativas = 0
while True:
    user = input('Digite seu usuario: ')
    passw = input('Digite sua senha: ')
    if user == usuario and passw == senha:
        print('Login aprovado. Acesso liberado!')
        break
    elif tentativas == 2:
        print('Limite de tentativas esgotados. Encerrando!')
        break
    else:
        print('Usuario ou senha invalidos. Tente novamente!')
        tentativas += 1