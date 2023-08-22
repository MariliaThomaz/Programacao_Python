print('Ola mundo')

nome =  input("Qual é seu  nome: ")
#idade = input("Qual é sua  idade: ")



# calculando o ano que pessoa  naceu  e mostra idade

ano_nac  = input("que ano que vc naceu: ")
print(type(ano_nac))
idade =  2022 - int(ano_nac)
print(idade)
print(type(ano_nac))



#pegar uma  letra  oua  mais d uma  varivel

fruta = 'abaconte'

print(fruta[4])

#modtra  um intalado de  letras 
print(fruta[1:5])


#otra maneira de  print

testoF = f'O {nome} , nacimeto {ano_nac}, idadade {idade}'
print(testoF)


mesagem = "   Marilia  esta dendo presetimetos de coisa"

print(mesagem.lower())# letras  miscula
print(mesagem.upper())# letras  maiuscula
print(mesagem.capitalize())#pega priemro letra  minuscla em maiusscula
print(mesagem.find('c'))#ele  procura letra c no  texto mostra a  posição ele está

print(mesagem.replace('a', '$'))#trocndo letras do texto 
print(mesagem.strip()) #tirando espaço primero cataque

# matemtica


calcando=  2 + 2 * 3 /2
#  2 *3 =6
#6 /2 = 3
#2+3 = 5
print(calcando)
espocial = 5 **2 # valores exponencial é o valor elevado 5^2
print(espocial)
espocial = 5 **2  +5
print(espocial)

# operadores de comparaçãobject
'''
== equal
!=   note equal
'''
