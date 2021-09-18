import java.util.Scanner;

public class pago_trabajador {
    public static void main(String[] args) {
    
        Scanner capturador = new Scanner(System.in);

    //1. Capturar el número de horas trabajadas.
        System.out.println("Ingresa la cantidad de horas trabajadas");
        int numeroHoras = capturador.nextInt();

    //2. Capturar el costo de la hora.
        System.out.println("Ingresa el costo de la hora");
        double costoHoras = capturador.nextDouble();

        capturador.close();

    //Calcular el resultado.
       double resultado = numeroHoras * costoHoras;

    //mostrar el resultado en consola
        System.out.println("El pago del empleado es : " + resultado);
        
        
    }
}
