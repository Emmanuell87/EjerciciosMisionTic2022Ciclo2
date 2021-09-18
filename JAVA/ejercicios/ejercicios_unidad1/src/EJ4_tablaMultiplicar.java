import java.util.Scanner;

public class EJ4_tablaMultiplicar {
    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero: ");
        int numero = sc.nextInt();

        for (int i = 0; i < 11; i++) {
            int multiplo = numero * i;
            System.out.println(numero + "*" + i + " = " + multiplo);
        }
    }
    private static Scanner sc;
}
