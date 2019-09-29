/* Program Hitung Faktor Persekutuan
* dibuat untuk submisi jawaban dari soal Logical Solving 
* rekrutasi Daspro Laboratory
* @author LumpiaBasah (Kelompok 10)
* GitHub: https://github.com/sonadztux/Logical-Solving-Rekrutasi-DASPRO-LumpiaBasah
*/
import java.util.Scanner;

public class faktor_persekutuan {
    // Objek input dari class Scanner untuk input user
    static Scanner input = new Scanner(System.in);

    // Fungsi untuk mencari faktor dari masing-masing angka yang diinput
    static void cari_faktor(int bilangan){
        System.out.print("Faktor dari "+bilangan+" : ");
        for (int i = 1; i <= bilangan; i++) {
            if(bilangan % i == 0) {
                System.out.print(i+" ");
            }
        }
    }

    // Fungsi untuk mencetak faktor persekutuan
    static void cetak_persekutuan(int bilangan1, int bilangan2) {
        System.out.print("\nFaktor persekutuan bilangan "+bilangan1+" dan "+bilangan2+" : ");
        for (int i = 1; i <= bilangan1; i++) {
            if (bilangan1 % i == 0 && bilangan2 % i == 0) {
                System.out.print(i+" ");
            }
        }
    }
    
    public static void main(String[] args) {
        // Input
        System.out.println("Input Faktor Persekutuan 2 Bilangan");
        System.out.print("Angka pertama\t: ");
        int bilangan1 = input.nextInt();
        System.out.print("Angka kedua\t: ");
        int bilangan2 = input.nextInt();

        // Calling the function
        cari_faktor(bilangan1);
        System.out.println("");
        cari_faktor(bilangan2);
        cetak_persekutuan(bilangan1, bilangan2);
    }
}