# o  Whil Loop é bom para quando vc tem uma condição

valo =100
dia=0
while valo > 20:
  dia += 1 
  print(f'No dia {dia} o prudoto  vai ser vendido por R$:{valo}')
  valo-=5


  valorp = int(input('Digite o valor de seu Produto em R$: '))
  while valorp > 20:
    valorp = (valorp * 0.10) + valorp
    print(f'O valor  final so seu   produto sera de R${valorp}')
    break