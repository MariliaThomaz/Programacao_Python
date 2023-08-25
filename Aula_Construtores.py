from datetime import datetime #para pegar  data atual
#Classe de dados
class Funsoanrios:
     
     def __init__(self, nome, sobrnome, anoS):
          self.nome = nome
          self.sobrnome = sobrnome
          self.anoS = anoS

     def nome_completo(self):
          return self.nome + ' ' + self.sobrnome
     
     def idade_fus(self):
          ano_atual = datetime.now().year
          self.anoS = int(ano_atual - self.anoS)
          return self.anoS
          

#Objeto 
usario1 = Funsoanrios('Maria', 'Carvalho', 1992)
usario2 = Funsoanrios('Pedro', 'Lucas', 1996)



print(usario1.nome, usario1.sobrnome)
print(usario2.nome_completo())

print(Funsoanrios.nome_completo(usario1))


