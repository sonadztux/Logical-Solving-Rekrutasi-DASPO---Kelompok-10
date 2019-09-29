# Program Mencari The Best Second
# dibuat untuk submisi jawaban dari soal Logical Solving 
# rekrutasi Daspro Laboratory
# @author LumpiaBasah (Kelompok 10)
# GitHub: https://github.com/sonadztux/Logical-Solving-Rekrutasi-DASPRO-LumpiaBasah
print('Aplikasi menentukan Best Second')

# Fungsi untuk mencari the best second
def cari_best_second(daftar_angka):
    # Deklarasi list kosong untuk menyimpan nilai unique
    angka_unique = []
    # Perulangan untuk mendapat setiap angka inputan pada list daftar_angka
    for angka in daftar_angka:
        # Append angka jika angka belum ada di list angka_unique
        if angka not in angka_unique:
            angka_unique.append(angka)
    # Descending sorting angka-angka di list angka_unique
    angka_unique.sort(reverse=True)
    # Mengembalikan angka terbesar kedua
    return angka_unique[1]

# Perulangan untuk validasi input adalah numeric
ulang = True
while ulang:
    # try except validasi input adalah numeric
    try:
        # meminta input user
        data = int(input('Total data : '))
        # validasi input total data harus lebih besar dari 1
        if data > 1:
            print('\r')
            # list untuk menyimpan daftar angka yang diinput
            daftar_angka = []
            tanya = 1
            # perulangan untuk input angka berdasar dari input total data
            while tanya <= data:
                # try-except validasi input adalah numeric
                try:
                    input_angka = int(input('Angka ke-'+str(tanya)+' : '))
                    daftar_angka.append(input_angka)
                    tanya += 1
                except ValueError:
                    print('Hanya boleh input angka!')
            # jika semua validasi dilewati maka panggil fungsi
            # cari_best_second dengan parameter list daftar_angka
            # dan variabel ulang diset menjadi False
            print('\nBest second:',cari_best_second(daftar_angka))
            ulang = False
        else:
            print('Data tidak boleh kurang dari sama dengan 1')
    except ValueError:
        print('Hanya boleh input angka!')