#def é a compressão de definition function - para criar uma def, digita def e o nome da função

def imprimir():
    print('Olá')
    
imprimir()

#função são ações, então o nome deve ser uma ação (imprimir, somar, rodar, fazer, subtrair)

def saudacao(nome):
    return f'Olá {nome}'

print(saudacao('Dorival'))


def saudacao(nomes):
    '''
    parameter nome:list
    
    Esta função recebe uma lista e percorre os dados dentro de uma lista
    
    '''
    for i in nomes:
        return i
lista = ['Felipe','Camila','Thalita','Lucas']

print(saudacao.__doc__) #mostra a documentação da função
print(saudacao(nomes=lista))

# ATIVIDADE PRÁTICA 1 - Crie uma função que receba um nome e imprima uma saudação personalizada.

def saudar(nome):
    '''
        parameter nome: string
        
        Esta função recebe um nome e imprime uma saudação personalizada na tela
        
    '''
    return f'Olá {nome}, seja bem vindo!'

nome = input('Digite seu nome: ')
print(saudar(nome))

#ATIVIDADE PRÁTICA 2 - Crie uma função que receba um horário e imprima "Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.
def horario(hora):
    '''
        parameter hora: integer
        
        Esta função recebe um valor de hora e retorna uma mensagem de saudação de acordo com o horario recebido
    
    '''
    if hora >= 5 and hora < 12:
        return 'Bom dia'
    elif hora >= 12 and hora <18:
        return 'Boa tarde'
    elif hora >=18 and hora <= 23:
        return 'Boa Noite'
    elif hora == 24 or hora >= 0 and hora <5:
        return 'Boa Madrugada'
    else:
        return 'Hora inválida'
    
hora = int(input('Digite a hora atual:'))
print(horario(hora=hora))

# ATIVIDADE PRÁTICA 3 - Crie uma função que receba dois números e retorne a soma deles.

def somar(n1,n2):
    '''
        parameter n1,n2: integer
        
        Esta função recebe dois numeros e mostra a soma dos valores
    
    '''
    return f'A soma de {n1} mais {n2} é igual a {n1+n2}'

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print(somar(n1,n2))

# ATIVIDADE PRÁTICA 4 - Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo.

def subtrair(n1,n2):
    '''
        parameter n1,n2: integer
        
        Esta função recebe dois numeros e mostra a subtração dos valores
    
    '''
    return f'A subtração de {n1} menos {n2} é igual a {n1-n2}'

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print(subtrair(n1,n2))

# ATIVIDADE PRÁTICA 5 - Crie uma função que receba dois números e retorne a multiplicação deles.

def multiplicar(n1,n2):
    '''
        parameter n1,n2: integer
        
        Esta função recebe dois numeros e mostra a multiplicação dos valores
    
    '''
    return f'A multiplicação de {n1} vezes {n2} é igual a {n1*n2}'

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print(multiplicar(n1=n1,n2=n2))

# ATIVIDADE PRÁTICA 6 - Crie uma função que receba dois números e retorne a divisão deles.

def dividir(n1,n2):
    '''
        parameter n1,n2: integer
        
        Esta função recebe dois numeros e mostra a divisão dos valores
    
    '''
    return f'{n1} dividido por {n2} é igual a {n1/n2}'

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print(dividir(n1=n1,n2=n2))

# DESAFIO PRÁTICO - Calculadora
# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair. (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.
# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse exercício.

def somar(n1,n2):
    return f'A soma de {n1} mais {n2} é igual a {n1+n2}'
def subtrair(n1,n2):
    return f'A subtração de {n1} menos {n2} é igual a {n1-n2}'
def multiplicar(n1,n2):
    return f'A multiplicação de {n1} vezes {n2} é igual a {n1*n2}'
def dividir(n1,n2):
    return f'{n1} dividido por {n2} é igual a {n1/n2}'

while True:
    acao=int(input('Digite a ação desejada: 1:somar / 2:subtratir / 3:multiplicar / 4:dividir / 5:Sair '))
    if acao == 1:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print(somar(n1,n2))
    elif acao == 2:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print(subtrair(n1,n2))
    elif acao == 3:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print(multiplicar(n1=n1,n2=n2))
    elif acao == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print(dividir(n1=n1,n2=n2))
    elif acao == 5:
        break
print('Encerrando...')