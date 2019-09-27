persamaan = 'x-1=5'

def hitung_persamaan(a, b, c):
        return int((c-b)/a)

def elemen_persamaan(persamaan):
    for elemen in persamaan:
        if elemen == 'x':
            index_konstanta = persamaan.index(elemen)
            if persamaan[:(persamaan.index(elemen))] == '':
                a = 1
            else:
                a = int(persamaan[:(persamaan.index(elemen))])
        elif elemen == '=':
            b = int(persamaan[(index_konstanta+1):(persamaan.index(elemen))])
            c = int(persamaan[(persamaan.index(elemen)+1):])
    return hitung_persamaan(a, b, c)

print(elemen_persamaan(persamaan))

# string = 'x'
# print(''==string[:string.index('x')])