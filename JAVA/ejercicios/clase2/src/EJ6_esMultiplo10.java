import java.util.Scanner;

public class EJ6_esMultiplo10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero entero: ");
        int numero = sc.nextInt();
        sc.close();

        String esMultiplo10 = " Es multiplo de 10";
        String noEsMultiplo10 = " No es multiplo de 10";
        String resultado = (numero%10 == 0 ? esMultiplo10 : noEsMultiplo10);
        System.out.println("El número: " + numero + resultado);

    }
}
