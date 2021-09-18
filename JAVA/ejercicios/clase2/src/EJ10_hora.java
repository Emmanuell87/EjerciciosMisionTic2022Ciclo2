import java.util.Scanner;

public class EJ10_hora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el primer número entero: ");
        int hora = sc.nextInt();
        System.out.println("Ingrese el segundo número entero: ");
        int minuto = sc.nextInt();
        System.out.println("Ingrese el tercer número entero:");
        int segundo = sc.nextInt();
        sc.close();
        
        if ((hora >= 0 && hora <= 24) && (minuto >= 0 && minuto <= 59) && (segundo >= 0 && segundo <= 59)){
            System.out.println("La hora: " + hora + ":" + minuto + ":" + segundo + ", Es valida");
        }
        else{
            System.out.println("La hora: " + hora + ":" + minuto + ":" + segundo + ", No es valida");
        }
    }
}
