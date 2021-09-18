import java.util.Scanner;

public class EJ5_adivinaElNumero {
    public static void main(String[] args) {
        var Max = 100;
        var Min = 1;
        var numeroAadivinar = Math.round(Min + (Math.random() * (Max - Min)));
        System.out.println("***************ADIVINA EL NÚMERO***************");
        int intentos = 1;
        while (true) {
            sc = new Scanner(System.in);
            System.out.println("Ingrese un número entero entre 1 y 100: ");
            int numero = sc.nextInt();
            if (numero >= 1 && numero <= 100){
                if(numero == numeroAadivinar){
                    System.out.println("FELICIDADES, has adivinidado el número: " + numeroAadivinar + " en " + intentos + " intentos.");
                    break;
                }
                else if (numeroAadivinar > numero){
                    System.out.println("El número que busca es mayor.");
                    intentos += 1;
                }
                else{
                    System.out.println("El número que busca es menor.");
                    intentos += 1;
                }
            }
            else{
                System.out.println("Por favor ingrese un número entre 1 y 100.");
            }
        }
    }

    private static Scanner sc;
}
