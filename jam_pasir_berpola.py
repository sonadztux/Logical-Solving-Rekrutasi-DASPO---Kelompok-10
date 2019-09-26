# Program Generate Jam Pasir Berpola
# dibuat untuk submisi jawaban dari soal Logical Solving 
# rekrutasi Daspro Laboratory
# @author sonadztux
# GitHub: https://github.com/sonadztux

def cetak_jam(ukuran, isi):
    # Mencetak piramid terbalik
    # Perulangan untuk baris sesuai ukuran yang diinput user
    for baris in range(0, ukuran):
        # cetak pola batas kiri
        print('|', end='')
        # perulangan untuk mencetak spasi
        for spasi_kiri in range(0, baris):
            print(' ', end='')
        # cetak pola pembuka batas tengah
        print('\\', end='')
        # perulangan untuk mencetak isi pola jam berdasar input user
        for kolom in range(2*(baris-ukuran+1), 0):
            print(isi, end='')
        # cetak pola penutup batas tengah
        print('/', end='')
        # perulangan untuk spasi ke kanan
        for spasi_kanan in range(0, baris):
            print(' ', end='')
        # cetak batas kanan
        print('|')

    # Mencetak pola piramid
    # Perulangan untuk baris sesuai ukuran yang diinput user
    for baris in range(0, ukuran):
        # cetak pola batas kiri
        print('|', end='')
        # perulangan untuk mencetak spasi
        for spasi_kiri in range(0, ukuran-1-baris):
            print(' ', end='')
        # cetak pola pembuka batas tengah
        print('/', end='')
        # perulangan untuk mencetak isi pola jam berdasar input user
        for kolom in range(0, 2*(baris)):
            print(isi, end='')
        # cetak pola penutup batas tengah
        print('\\', end='')
        # perulangan untuk spasi ke kanan
        for spasi_kanan in range(0, ukuran-1-baris):
            print(' ', end='')
        # cetak batas kanan
        print('|')

# Meminta input dari user
ukuran = int(input('Masukkan Ukuran : '))
isi = input('Masukkan Isi Jam Pasir : ')

# calling the function
cetak_jam(ukuran, isi)