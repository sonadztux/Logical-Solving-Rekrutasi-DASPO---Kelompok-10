print('Aplikasi menentukan Best Second')

def cari_best_second(daftar_angka):
    angka_unique = []
    for angka in daftar_angka:
        if angka not in angka_unique:
            angka_unique.append(angka)
    angka_unique.sort(reverse=True)
    return angka_unique[1]

ulang = True
while ulang:
    try:
        data = int(input('Total data : '))
        print('\r')
        daftar_angka = []
        tanya = 1
        while tanya <= data:
            try:
                input_angka = int(input('Angka ke-'+str(tanya)+' : '))
                daftar_angka.append(input_angka)
                tanya += 1
            except ValueError:
                print('Hanya boleh input angka!')
        print('\nBest second:',cari_best_second(daftar_angka))
        ulang = False
    except ValueError:
        print('Hanya boleh input angka!')