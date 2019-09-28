def hitung_persamaan(a, b, c):
    if (c-b)%a != 0:
        if c-b < 0 and a < 0:
            return print('x =',str(-1*(c-b))+'/'+str(-1*a))
        return print('x =',str(1*(c-b))+'/'+str(1*a))
    else:
        return(print('x =',int((c-b)/a))) 

def elemen_persamaan(persamaan):
    for elemen in persamaan:
        if elemen == 'x':
            if persamaan[:(persamaan.find('x'))] == '':
                a = 1
            else:
                a = persamaan[:(persamaan.find('x'))]
        elif elemen == '=':
            if persamaan[(persamaan.find('x')+1):(persamaan.find('='))] == '':
                b = 0
            elif persamaan[(persamaan.find('x')+1):persamaan.find('x')+2] == '+':
                b = persamaan[(persamaan.find('x')+2):(persamaan.find('='))]
            else:
                b = persamaan[(persamaan.find('x')+1):(persamaan.find('='))]
            c = persamaan[(persamaan.find('=')+1):]
    print('a =', a)
    print('b =', b)
    print('c =', c)
    return hitung_persamaan(int(a), int(b), int(c))

def cek_input_persamaan(persamaan):
    before_equal = persamaan[:persamaan.find('=')]
    if before_equal[-1] == 'x':
        if '-' in before_equal:
            if before_equal.find('-') != 0:
                return print('Format Penulisan Salah')
            else:
                return elemen_persamaan(persamaan)
        elif '+' in before_equal:
            return print('Format Penulisan Salah')
        else:
            return elemen_persamaan(persamaan)
    else:
        return elemen_persamaan(persamaan)

persamaan = input('Persamaan : ')
cek_input_persamaan(persamaan)