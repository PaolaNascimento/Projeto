# """
# Aqui eu escrevo que eu quiser como se fosse um comentário.
# chamando de  DocString
# """

# '''
# Escrever notas ou fazer comentários
# '''

# Uma variavél são os objetos comuns e descrições conhecidas 
#Variavél= Nome / String = "Paola"
    #Que ficara dessa forma : Nome = "Paola"
# # Parecido com as três aspas("""), me permite escrever um comentário.


# print('Hello, world!')
# print('Hi, world!')

# #COMANDO SINAL DE SEPARAÇÃO
# print(12, 34, sep="-")
# print(12, 34, sep='-')

# #String é tudo aquilo que esta dentro de aspas () são caracteres declarações e comandos ditos por mim.

# #Escape
# print("Paola \"Gomes")

# #Saber o tipo do valor

# print(type ('Paola'))

# print(10 == 10)
# print(10 == 11)

# print(type (10 == 10))

# print(10, -10)

# nome_completo = 'Paola Gomes'
# print(nome_completo)

# nome = 'Paola Gomes'
# sobrenome = 'Nascimento'
# idade = 23
# ano_nascimento = 2022 - idade
# maior_de_idade = idade >= 18
# altura_metros = 1.60

# print('Nome:', nome)
# print('Sobrenome:', sobrenome)
# print('Idade:', idade)
# print('Ano de nascimento:', ano_nascimento)
# print('É maior de idade?', maior_de_idade)
# print('Altura em metros:', altura_metros)

# adicao = 10 + 10
# print('Adição', adicao)

# subtracao = 10 - 5
# print('Subtração', subtracao)

# multiplicacao = 10 * 10
# print('Multiplicação', multiplicacao)

# divisao = 10 / 3  # float
# print('Divisão', divisao)

# divisao_inteira = 10 // 3
# print('Divisão inteira', divisao_inteira)

# exponenciacao = 2 ** 10
# print('Exponenciação', exponenciacao)

# modulo = 55 % 2  # resto da divisão
# print('Módulo', modulo)

# print(10 % 8 == 0)
# print(16 % 8 == 0)
# print(10 % 2 == 0)
# print(15 % 2 == 0)
# print(16 % 2 == 0)


# concatenacao = 'Paola' + ' ' + 'Gomes'
# print(concatenacao)

# a_dez_vezes = 'A' * 10
# tres_vezes_paola = 3 * 'Paola'
# print(a_dez_vezes)
# print(tres_vezes_paola)

# # 1. (n + n)
# # 2. **
# # 3. * / // %
# # 4. + -
# conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
# print(conta_1)

# numero1 = int(input('Primeiro número:'))
# numero2 = int(input('Segundo número:'))
# print(numero1+numero2)

# print('7'+'4')
# print(7+4)

# nome = 'Paola'
# idade = 23
# telefone = 115326452
# print(nome,idade,telefone)

# nome = input('Qual seu nome?')
# idade = input ('Qual sua idade?')
# telefone = input ('Qual seu telefone?')
# print(nome,idade,telefone)

# nome = input('Qual seu nome?')
# print('Olá Prazer em te conhecer', nome, '!')

# nome = input('Qual seu nome?')
# print('Olá Prazer em te conhecer, {}'.format(nome))

# dia = input('Dia:')
# mes = input('mes:')
# ano = input('ano:')
# print('Você nasceu no dia', dia, mes, ano, sep='-')

# n1 = int(input('Primeiro número:'))
# n2 = int(input('Segundo número:'))
# s = n1 + n2
# print('A soma entre {} e {} vale {}'.format(n1,n2,s))

# a = input('Digite algo:')
# print('O tipo primitivo desse valor é' ,type(a))
# print('Só tem espaços? ', a.isspace())
# print('É um número? ', a.isnumeric())
# print('É um Alfabético? ', a.isalpha())
# print('É um alfanumerico? ', a.isalnum())

# n1 = int(input('Primeiro número:'))
# n2 = int(input('Segundo número:'))
# n3 = int(input('Terceiro número:'))
# n4 = int(input('Quarto número:'))
# s = (n1*n2) + (n3+n4)
# print('A soma entre {},{},{},{},{} e {} vale {}'.format(n1,n2,n3,n4,s))

# nome = input('Qual seu nome?')
# print('Olá Prazer em te conhecer, {:=^20}'.format(nome))

# nome = input('Qual seu nome?')
# print('Olá Prazer em te conhecer, {:20}!'.format(nome))

# print('"Já sei!"')

# nome = "Paola"
# idade = 23
# fotmato = '{n} tem {i} anos'
# print(fotmato.format(n=nome, i=idade))

# nome = 'Paola'
# idade = 23
# formato = f'{nome} tem {idade: .2f} anos'
# print(formato)

# n1 = int(input('Um valor:'))
# n2 = int(input('Outro valor:'))
# s = n1 + n2
# m = n2 * n2
# d = n1/ n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {}, o produto é {} e a divisão é {:.1f}'.format(s,m,d))
# print('Divisão inteira {} e potência {}'.format(di,e))

#PARA NÃO QUEBRAR
# n1 = int(input('Um valor:'))
# n2 = int(input('Outro valor:'))
# s = n1 + n2
# m = n2 * n2
# d = n1/ n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {}, o produto é {} e a divisão é {:.1f}'.format(s,m,d), end=' ')
# print('Divisão inteira {} e potência {}'.format(di,e))

#PARA QUEBRAR
# n1 = int(input('Um valor:'))
# n2 = int(input('Outro valor:'))
# s = n1 + n2
# m = n2 * n2
# d = n1/ n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {},  o produto é {} e a divisão é {:.1f}'.format(s,m,d), end=' ')
# print(' \n Divisão inteira {} e potência {}'.format(di,e))

# num = int(input('Digite um valor'))
# antecessor = num -1
# sucessor = num +1
# print('O valor de um', num,'é o sucessor', sucessor )
# print("O valor de um", num, 'é o antecessor', antecessor)

#num = int(input('Digite um valor')) 
#raiz = num ** 5
#antecessor = num -1
#sucessor = num +1
#dobro = num + num
#print('O valor', num,'é o sucessor', sucessor )
#print("O valor", num, 'é o antecessor', antecessor)
#print("O valor", num, 'é o dobro', dobro)
#print('A raiz quadrada de', num, 'é', raiz)



#nome = 'Paola Gomes'
#altura = 1.62
#peso = 50
#imc = peso / altura ** 2    
#print(nome, 'tem', altura, 'de altura',)
#print( 'pesa', peso,'quilos e seu imc é',)
#print(imc)

#1Formatando strings
#nome = input('Digite um nome:')
#idade = int(input('Digite um número:'))

#mensagem = f"Olá, meu nome é {nome} e tenho {idade} anos."
#print(mensagem)

#2Formatando strings
#nome = input('Digite um nome:')
#idade = int(input('Digite um número:'))
#mensagem = "Tenho {1} anos e meu nome é {0}.".format(nome, idade)
#print(mensagem)

#if/elif/else (se/se não se/ se não)

#entrada = input('Você quer "entrar" ou "sair?" ')
#if entrada == 'entrar':
    #print('Você entrou no sistema')
#elif entrada == 'sair':
    #print('Você saiu do sistema')
#else:
    #print('Você não digitou nada!')

''''
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')
'''
'''
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
'''
''''
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)
'''

print('Olá')