def somar():
    print('Esta funcao vai somar valroes')

def multi():
    print('Esta funcao vai multiplicar')


def fin_idex (to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1