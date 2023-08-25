
numero = [2,3,2,4]

print()

nome = ['carol', 'jose', 'marilia', 'paula']

#pegar  um  item  da  listra
print(nome[2])

#mudar  item da  lisada
nome[2] ='Marilia Thomaz'

print(nome)

#função para  lista

#add  novos  item  para  lista no finaç dela
nome.append('Helia')
print(nome)

#remover  item da lista
nome.remove('Marilia Thomaz')
print(nome)

#add  um item na  lita mais esolhendo lugar
nome.insert(2,'Marilia Thomaz F' )
print(nome)

#tinado pela  posição 
nome.pop(3)
print(nome)

#organisa  por  odem alfabetica
nome.pop()
print(nome)

#concatenar  lita

nuemro = [1,2,46,7,1]

final= numero *2
print(final)

junataLista = numero + nome
print(junataLista)

#pode usa uma medodo
numero.extend(numero)
print(f'usando o extend: {numero}')


#cria  lista dentro de  lista
items= [['item1','intem2'],['item3', 'item4']]
print(items[1][1])

#for lupe com  lista

valos = [50, 86, 466, 10, 36 ]

for x in valos:
    print(x)


#lista de cor com veficação
cores = input('Digite  uma cor: ')
cor= ['amarelo', 'verde', 'azul', 'vermelho']

if cores.lower() in  cor:
    print('No estoque')
else:
    print('Não  temos esta cor no estoque')

#junatando lista com metodo list e zip

corr= ['amarelo', 'verde', 'azul', 'vermelho']
vava = [10, 25, 35, 40, 21]

duas_lista = zip(corr, vava)#zip junta  lista

print(list(duas_lista))#trasfoamdo fomato de lista


#uma  lista  por  input

frutas=  input('Digite  uma  fruta com vigulas: ')

fruta_lista = frutas.split(', ')

print(fruta_lista)

#lista Tuple  ela  ocupa menos espaçoa é  usada para caso  vc não  ira atera dados dela

list_tuple=('amarelo', 'verde', 'azul', 'vermelho')

print(type(list_tuple))