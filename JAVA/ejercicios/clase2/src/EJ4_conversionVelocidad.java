import java.util.Scanner;

public class EJ4_conversionVelocidad {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la velocidad en Km/h a convertir a m/s: ");
        var km = sc.nextDouble();
        sc.close();

        double m = convertirVelocidad(km);
        System.out.println(km +"km/h equivale a: " + m + "m/s");
         
    }

    private static double convertirVelocidad(double km) {
        double conversion = Math.round(((km * 1000) / 3600) * 100.0)/100.0 ;
        return conversion;
    }
}
