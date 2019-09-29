# Program Hitung Faktor dan Faktor Persekutuan
# dibuat untuk submisi jawaban dari soal Logical Solving 
# rekrutasi Daspro Laboratory
# @author LumpiaBasah (Kelompok 10)
# GitHub: https://github.com/sonadztux/Logical-Solving-Rekrutasi-DASPRO-LumpiaBasah

# Fungsi untuk menghitung persamaan
def hitung_persamaan(a, b, c):
    # validasi untuk input apakah akan berbentuk pecahan
    # jika hasil sisa bagi c-b/a tidak sama dengan 0
    if (c-b)%a != 0:
        if c-b < 0 and a < 0:
            return print('x =',str(-1*(c-b))+'/'+str(-1*a))
        return print('x =',str(1*(c-b))+'/'+str(1*a))
    # hasil bilangan bulat
    else:
        return(print('x =',int((c-b)/a))) 

# Fungsi untuk menjabarkan elemen-elemen dari persamaan yang diinputkan
def elemen_persamaan(persamaan):
    # iterasi seluruh elemen dari string persamaan yang diinput
    for elemen in persamaan:
        # mencari nilai a berdasar elemen x
        if elemen == 'x':
            if persamaan[:(persamaan.find('x'))] == '':
                a = 1
            else:
                a = persamaan[:(persamaan.find('x'))]
        # mencari elemen b dan c berdasar elemen =
        elif elemen == '=':
            # jika persamaan hanya satu konstanta maka b = 0
            if persamaan[(persamaan.find('x')+1):(persamaan.find('='))] == '':
                b = 0
            # jika operator adalah + maka operator tidak perlu 
            # ikut dimasukkan sebagai nilai b
            elif persamaan[(persamaan.find('x')+1):persamaan.find('x')+2] == '+':
                b = persamaan[(persamaan.find('x')+2):(persamaan.find('='))]
            # jika operator adalah - maka akan dimasukkan 
            # sebagai nilai dari b
            else:
                b = persamaan[(persamaan.find('x')+1):(persamaan.find('='))]
            c = persamaan[(persamaan.find('=')+1):]
    # Menampilkan hasil penjabaran
    print('a =', a)
    print('b =', b)
    print('c =', c)
    # Memanggil fungsi hitung_persamaan dengan parameter elemen hasil penjabaran
    return hitung_persamaan(int(a), int(b), int(c))

# Fungsi untuk validasi inputan dari user
# apakah sudah sesuai dengan format yang sesuai 
def cek_input_persamaan(persamaan):
    # mengambil seluruh elemen sebelum = (sama dengan)
    before_equal = persamaan[:persamaan.find('=')]
    # validasi jika terdapat x pas sebelum = maka format salah
    if before_equal[-1] == 'x':
        # jika terdapat operator (-) di seluruh elemen sebelum (=) 
        # dan indexnya bukanlah 0 maka format inputan salah
        if '-' in before_equal:
            if before_equal.find('-') != 0:
                return print('Format Penulisan Salah')
            else:
                # format penulisan yang benar akan langsung dimasukkan
                # sebagai parameter untuk fungsi elemen_persamaan()
                return elemen_persamaan(persamaan)
        # jika terdapat operator (+) di seluruh elemen sebelum (=)
        # di manapun letak indexnya maka format inputan salah
        elif '+' in before_equal:
            return print('Format Penulisan Salah')
        else:
            return elemen_persamaan(persamaan)
    else:
        return elemen_persamaan(persamaan)

# Meminta input dari user
persamaan = input('Persamaan : ')

# Calling the function
cek_input_persamaan(persamaan)