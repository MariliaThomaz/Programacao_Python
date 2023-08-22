#doi  lupe

for nume1 in range(5):
    print(f'##lupe 1 {nume1}')
    for nume2 in  range(5):
        print(f'lupe 2 {nume2}')

# sepadando a  palavra 
palavra  = " MARILIA"

for spaco in palavra:
    print(f' {spaco}', end='')


#lupe  fgazendo  retagulo

linha =6
cluna =6
simboloa = "@"

for l in range(linha):
    for c in range(cluna):
        print(simboloa, end=" ")
    print()