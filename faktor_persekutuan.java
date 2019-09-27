/**
 * faktor_persekutuan
 * @author Kelompok 10
 */
import java.util.Scanner;

public class faktor_persekutuan {
    static Scanner input = new Scanner(System.in);

    static void cari_faktor(int bilangan){
        System.out.print("Faktor dari "+bilangan+" : ");
        for (int i = 1; i <= bilangan; i++) {
            if(bilangan % i == 0) {
                System.out.print(i+" ");
            }
        }
    }

    static void cetak_persekutuan(int bilangan1, int bilangan2) {
        System.out.print("\nFaktor persekutuan bilangan "+bilangan1+" dan "+bilangan2+" : ");
        for (int i = 1; i <= bilangan1; i++) {
            if (bilangan1 % i == 0 && bilangan2 % i == 0) {
                System.out.print(i+" ");
            }
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Input Faktor Persekutuan 2 Bilangan");
        System.out.print("Angka pertama\t: ");
        int bilangan1 = input.nextInt();
        System.out.print("Angka kedua\t: ");
        int bilangan2 = input.nextInt();

        cari_faktor(bilangan1);
        System.out.println("");
        cari_faktor(bilangan2);
        cetak_persekutuan(bilangan1, bilangan2);
    }
}