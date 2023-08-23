

#cria  uma função  def

def  boas_vinda():
    print('Ola Marilia')
    print('Ola  mundo 2023')

boas_vinda()


# função com argumeto

def boas_vinda(nome, idade):
 print(f'ola {nome}. ')
 print(f'Sua idade  é {str(idade)}')

boas_vinda('Marilia', 27)
boas_vinda('Julia', 24)


# Uma tarrfa relizda(pede para ser executado mais ela não armazenou mada)
def clinente1(nome):
   print(f'Ola {nome}')

x = clinente1('Julia') #Prova para


def clinente2(nome):
   return f'Ola {nome}'

z= clinente2('Romulo') #retona um valor  (quando quer  gardar o valor  da varivel vc tem ter  retun)

print(x)
print(z)

# loco de repetição com  função com mais de argumeto 
def soma(*numeros):
   resultado = 0
   for num in numeros:
        resultado += num

   return resultado
   
x = soma (5,3,4,7)
print(f'a soma dos valores : {x}')

# como idetificar  os  parametros

def agencia(**carro):# quando ** é pára varios  paametos
   return carro


print(agencia(marca='Gol', cor='Branco', motor=1.0))