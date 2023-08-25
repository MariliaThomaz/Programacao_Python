#quando usar  Array  para quando tem prblema de  perfomase  tiposa  tenho  muisto  dados 
from array import array
lentra = ['a', 'b', 'c', 'd']
numero_i = [10, 14 ,51, 30]
nuemro_f = [40.22, 71.44, 44.55]

print(lentra)
print(numero_i)
print(nuemro_f)

lentra = array('u',['a', 'b', 'c', 'd'])
numero_i = array('i', [10, 14 ,51, 30])
nuemro_f = array('f', [40.22, 71.44, 44.55])

print(lentra)
print(numero_i)
print(nuemro_f)

#set trabalhando com Listas

lista1 = [10,20,30,50,70]
lista2 = [10,20,60,12,80]
#coventado  lista  para  Set
num1 = set(lista1)
num2 = set(lista2)

print(f'set 1: {num1}')
print(f'set 2: {num2}')

print(f'set Union Tira os repetidos: {num1 | num2}')
print(f'set Differnce motra valore direntes: {num1 - num2}')
print(f'set Symmetric Differnce tira os dubliado duas  lista: {num1 ^ num2}')
print(f'set Ande ele  motra o que dupliada  duas lista: {num1 & num2}')

#para ver  o  tamanho
print(len(num2))


#funçoes de Set

s1 = {1,2,3,4,5,6}
s1.add(10)
s1.update([ 6, 41,25,32])
s1.remove(10)
s1.discard(3)
print(s1)

#strig 

set3 = {'a', 'b', 'c', 'd'}
set2 = {'a', 'b', 'f', 'n'}

set4 = set3.difference(set2)

print(f'difference: {set4}')

set4 = set3.intersection(set2)
print(f'intersection:  {set4}')

set4 = set3.symmetric_difference(set2)
print(f'symmetric_differencen:  {set4}')

#dicionario 

aluno = {'nome':'Ana', 'idade': '24', 'Nota_final': 10, 'Apravoção': True}

print(aluno)

print(f'somete o nome: {aluno["nome"]}')

#mudade dadao no disoanrioa

aluno['nome'] = 'Carol'

print(aluno)

#aluazar mais de  um campo
aluno.update({'nome':'Jose', 
              'idade': '14', 
              'Nota_final': 8, 
              'Apravoção': True,
              'Marteias': ['Matematica', 'Portuges', ' Historia',  'Filosfia']})

print(aluno)

print(aluno.get('Marteias'))

'''
for keys, values in aluno.items():
    print(keys, values)
'''