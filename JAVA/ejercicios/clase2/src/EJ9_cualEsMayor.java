import java.util.Scanner;

public class EJ9_cualEsMayor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el primer número entero: ");
        int num1 = sc.nextInt();
        System.out.println("Ingrese el segundo número entero: ");
        int num2 = sc.nextInt();
        System.out.println("Ingrese el tercer número entero:");
        int num3 = sc.nextInt();
        sc.close();

        if (num1 > num2 && num1 > num3) {
            System.out.println("El mayor entre: " + num1 + ", " + num2 + " y " + num3 + " es: " + num1);
        }
        else if (num2 > num1 && num2 > num3) {
            System.out.println("El mayor entre: " + num1 + ", " + num2 + " y " + num3 + " es: " + num2);
        }
        else{
            System.out.println("El mayor entre: " + num1 + ", " + num2 + " y " + num3 + " es: " + num3);
        }
    }

}
