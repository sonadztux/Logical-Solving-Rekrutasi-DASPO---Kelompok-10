## Panduan sebagai Kontributor
Jika Anda ingin berkontribusi dengan kami, mohon lakukan petunjuk di bawah ini.

### It's Show Time, Let Me Show You Daks ^^
1. Fork repository dan pastikan fork repo yang up to date .
2. Cloning project yang sudah anda fork ke akun anda

        git clone <alamat-repo>

    Contoh menggunakan ssh:

        git clone git@github.com:sonadztux/Logical-Solving-Rekrutasi-DASPRO-Kelompok-10.git

    Contoh menggunakan https:

        git clone https://github.com/sonadztux/Logical-Solving-Rekrutasi-DASPRO-Kelompok-10.git
        
3. Untuk mempermudah pengembangan, hendaknya kita menambahkan repository pusat dengan lokal milik kita agar tidak terjadi konflik dengan kontributor lainnya.

        git remote add <nama-repo> <alamat-repo>

    Contoh:

        git remote add upstream git@github.com:sonadztux/Logical-Solving-Rekrutasi-DASPRO-Kelompok-10.git
        
4. Setelah remote repositori selesai, buatlah branch baru agar tidak merusak history branch utama, dan juga untuk memudahkan racking code, buatlah sesuai dengan issue atau fitur yang ingin dikerjakan.

        git checkout -b <nama-cabang>

    Contoh:

        git checkout -b menu_kemiskinan

5. Di cabang baru ini lah kita akan untuk melakukan perubahan kode, yang nantinya bisa kita push ke repo pusat. Untuk berpindah branch bisa kita gunakan `git checkout <nama-cabang>`, dimana `<nama-cabang>` adalah nama yang anda gunakan pada langkah sebelumnya.

    Contoh:

        git checkout menu_kemiskinan
        
6. Setelah melakukan perubahan, kita bisa lakukan commit berisi deskripsi singkat tentang perubahan yang anda lakukan. Tetapi jika ada penambahan file, bisa menggunakan perintah `git add <nama-file-baru>`, atau gunakan `git add .` untuk menambahkan semua perubahan yang ada di direktori tersebut secara rekursif. Setelah itu baru bisa kita commit.

        git commit -m "<pesan singkat>"

    Contoh:

        git commit -m "fix membuat anda miskin"

7. Setelah selesai melakukan commit, kita akan melakukan persiapan untuk membuat *merge request* atau kalo di github *pull request* (biasa disingkat PR) ke repo pusat. Pertama kita pindah branch kembali ke master. 

        git checkout master

8. Setelah itu, kita akan mengambil kode lagi dari pusat, untuk memastikan tidak terdapat konflik pada kontribusi kode kita. Konflik dapat terjadi jika dua atau lebih kontributor melakukan perubahan pada satu berkas, terutama jika perubahan dilakukan pada baris yang sama, terlepas dari apakah tujuan perubahan sama atau tidak.

        git fetch upstream
        git merge upstream/master

9. Dengan proses diatas, setidaknya kita telah bisa memastikan bahwa tidak ada konflik dengan repo pusat. Sekarang kita kembali ke branch lokal development kita `adminduk`.

        git checkout menu_kemiskinan

10. Setelah itu, kita gabungkan cabang tersebut dengan cabang utama, sehingga kontribusi dapat dikirimkan kembali ke repositori pusat dengan perintah `git rebase <nama-branch>`.

        git rebase master

11. Sebelum push ke repositori pusat, kita akan push ke repository hasil fork di awal pembahasan tadi.

        git push origin menu_kemiskinan

12. Setelah di push, kita akan melakukan merge request dan membandingkan perubahan yang telah dilakukan terhadap repo pusat. Anda juga bisa menyisipkan pesan untuk memberitahukan developer pemilik repositori tentang apa yang anda lakukan. Setelah yakin terhadap perubahan yang telah anda lakukan, silahkan pilih create merge request 

13. Jangan lupa lakukan pull sebelum melakukan perubahan kode !!
 

## Terimakasih
### Alhamdulillah sukses semua daks !!
