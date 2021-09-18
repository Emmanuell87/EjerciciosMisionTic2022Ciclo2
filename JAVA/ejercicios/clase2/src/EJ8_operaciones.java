import java.util.Scanner;

public class EJ8_operaciones {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el primer número: ");
        double num1 = sc.nextDouble();
        System.out.println("Ingrese el segundo número: ");
        double num2 = sc.nextDouble();
        sc.close();

        if (num2 != 0) {
            var division = Math.round((num1 / num2) * 100.0) /100.0;
            System.out.println(division);
        }
        else{
            System.out.println("Error: no es podible dividir por 0");
        }
    }
}
