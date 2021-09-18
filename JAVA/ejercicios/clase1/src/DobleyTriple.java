import java.util.Scanner;

public class DobleyTriple {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero");
        var numero = sc.nextInt();
        sc.close();

        var numeroDoble = numero * 2;
        var numeroTriple = numero * 3;

        System.out.println("El doble es: " + numeroDoble + ", el triple es: " + numeroTriple);
    }
}
