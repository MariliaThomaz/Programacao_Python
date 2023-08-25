from sys import getsizeof 
#Função lambida é uma função reduzida
#Uma função lambda ela não tem nome ela só tem argumentos depoisa Expressão

soma = lambda x,y: x+y + 10

print(soma(7,4))

#Uma função dentro de outra função

def somar(x):
    fun2 = lambda x: x +10
    return fun2(x) *4

print(somar(2))

#Map Function

lista = [1,2,3,4]

'''
def multi(x):
    return x * 2

list2 = map(multi,lista)

print(list(list2))

'''
# rezindo

print(list(map(lambda x: x * 2, lista)))


#filter

valores = [71,50,41,11,8]

# def compar(x):
#     return x >20

print(list(filter(lambda x: x>20, valores)))

#List Comprehesion

fruta =['abaxaxi','maga', 'maça', 'uva', 'banana', 'melacia']

fruta2 = [iten for iten in  fruta if  'm' in iten]
print(fruta)

#List Comprehesion
valores1 = [x * 10 for x  in range(6)]
print(valores1)

#Geneator Expressuons
#vendo quanto gasta de memoria



numi = [x*10 for x in range(400)]
print(type(numi))
print(getsizeof(numi))