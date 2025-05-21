# ATIVIDADE PRÁTICA 1 - Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função. A  função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.

# def media(n1,n2,n3):
#     media = (n1+n2+n3)/3
#     return media

# n1 = float(input('Insira a primeira nota: '))
# n2 = float(input('Insira a segunda nota: '))
# n3 = float(input('Insira a terceira nota: '))

# media = media(n1,n2,n2)
# print(f'A média das notas digitadas é {media}')

# ATIVIDADE PRÁTICA 2 - Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos, comprimento e largura de um retângulo, e retorna a área desse retângulo. Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada.

# def calcular_area_retangulo(comprimento,largura):
#     area = comprimento * largura
#     return area

# c = float(input('Digite o comprimento: '))
# l = float(input('Digite a largua: '))

# area = calcular_area_retangulo(c,l)
# print(f'A area é de {area}')

#Criar um script para cadastro de pessoas sem um limite de cadastro
# def cadastro(cod,nome,idade):
#     pessoas[cod] = {
#         'nome':nome,
#         'idade':idade
#         }

# pessoas = {}
# cod=0

# while True:
#     opcao=int(input('Digite a opção desejada: (1) para novo cadastro (2) para sair:'))
#     if opcao == 1:   
#         cod += 1
#         nome= str(input('Digite o nome:'))
#         idade= int(input('digite a idade: '))
#         cadastro(cod=cod,nome=nome,idade=idade)
#     elif opcao == 2:
#         break
#     else:
#         print('Opção inválida')
# print("\nCadastros realizados:")
# for chave, dados in pessoas.items():
#     print(f"Nome: {dados['nome']}, Idade: {dados['idade']}")
    
# def teste(**kwargs):
#     for chave, valor in kwargs.items():
#         print(chave,valor)
        
# teste(kwargs={'Dorival':23,'Felipe':22})

# ATIVIDADE PRÁTICA 3 - Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos posicionais (usando *args). A função deve concatenar todas as strings em uma única string e retorná-la.

# def concatenar_strings(*args):
#     texto = ''
#     for i in args:
#         texto += i
#     return texto

# entradas = []
        
# while True:
#     valor = input('Digite um valor inteiro: (-1 pra encerrar)')
#     if valor == "-1":
#         break
#     else:
#         entradas.append(valor)
        
# resultado = concatenar_strings(*entradas)
# print("Resultado concatenado:", resultado)

#função lambda é uma função de uma linha só
quadrado = lambda x:x**2
print(quadrado(10))

ajuste_nome = lambda nome:nome.title()
print(ajuste_nome('dorival'))

verifica_num = lambda x: 'Par' if x % 2 == 0 else 'Impar'
n = float(input('Digite um numero: '))
print(verifica_num(n))

lista=[1,2,3,4,5]
mapeamento = list(map(lambda x:x**2, lista))
print(mapeamento)

lista2=['felipe','tiago','caio']
mapeamento = list(map(lambda x:x.title(), lista2))
print(mapeamento)
filtro = list(filter(lambda x:x == 'felipe',lista2))
print(filtro)

lista3=[*range(100)]
lista3=list(filter(lambda x:x%2 == 0,lista3))
print(lista3)