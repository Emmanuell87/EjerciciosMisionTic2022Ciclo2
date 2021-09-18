import java.util.Scanner;

public class EJ2clase01 {
    public static void main(String[] args) {
        Scanner capturador = new Scanner(System.in);

    //Preguntar por la estación del año
        System.out.println("Ingrese una estación del año: ");
        String estacion = capturador.next();

    //Preguntar por el numero entero X
        System.out.println("Ingrese un número entero: ");
        int num = capturador.nextInt();

    //Preguntar por el adjetivo
        System.out.println("Ingrese un adjetivo");
        String adj = capturador.next();

            capturador.close();

        System.out.println("En un día " + adj + " de " + estacion + ", yo bebo un minimo de " + num + " tazas de café");
    }
}
