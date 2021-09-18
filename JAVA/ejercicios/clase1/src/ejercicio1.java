import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        
        System.out.println("Introduzca un número entero: ");
        var numero = sc.nextInt();
        sc.close();

        var digitos = numeroDigitos(numero);
        System.out.println("El numero tiene " + digitos + " cifras");

    }

    public static int numeroDigitos(int numero) {
        var cifras = 0;

        while (numero != 0){
            numero/= 10;
            cifras++;
        }

        return cifras;
    }
}
