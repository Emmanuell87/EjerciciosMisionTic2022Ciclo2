import java.util.Scanner;

public class EJ7_esMayuscula {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un caracter: ");
        char letra = sc.nextLine().charAt(0);
        sc.close();
        if(Character.isUpperCase(letra)) {
            System.out.println("Es Mayuscula");
        }
        else{
            System.out.println("No es Mayuscula");
        }
    }
}
