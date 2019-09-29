# Program Speed Limit
# dibuat untuk submisi jawaban dari soal Logical Solving 
# rekrutasi Daspro Laboratory
# @author LumpiaBasah (Kelompok 10)
# GitHub: https://github.com/sonadztux/Logical-Solving-Rekrutasi-DASPRO-LumpiaBasah
print(('==='*3)+' Speed Limit'+('==='*3))

# Fungsi untuk speed check
def check_speed_limit(speed):
    # set limit = 70 dan point = 0
    limit = 70
    point = 0
    # point bertambah jika speed lebih besar dari limit setiap kelipatan 5
    if speed > limit:
        point = int((speed - limit)/5)
        # license suspened jika point >= 12
        if point >= 12:
            print('License Suspened')
        else:
            print('Point : '+str(point))
    # Menampilkan Ok jika speed tidak melebihi limit
    else:
        print('Ok.')
        
# Perulangan untuk validasi input user adalah numeric
repeat = True
while repeat:
    # try-except validasi input
    try:
        speed = eval(input('Speed : '))
        # jika validasi terlewati
        # panggil fungsi check_speed_limit dengan parameter speed
        check_speed_limit(speed)
        # set variabel repeat menjadi False
        repeat = False
    except NameError:
        print('Hanya boleh input angka!')