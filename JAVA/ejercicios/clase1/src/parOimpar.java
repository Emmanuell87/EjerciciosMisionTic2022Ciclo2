import java.util.Scanner;

public class parOimpar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero");
        var numero = sc.nextInt();
        sc.close();

        System.out.println((numero%2 == 0 ? numero + " Es Par": numero + " Es Impar")); 

    }
}
