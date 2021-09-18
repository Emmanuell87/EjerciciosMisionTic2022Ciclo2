import java.util.Scanner;

public class EJ3_sueldoTrabajador {
    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.println("Ingrese las horas trabajadas durante el mes: ");
        int horas = sc.nextInt();

        int costaHora = 30000;

        int sueldoTrabajador = horas * costaHora;
        System.out.println("El sueldo del trabajador es: " + sueldoTrabajador);
    }

    private static Scanner sc;
}
