import java.util.Scanner;

public class EJ2_promedioNotas {
    private static Scanner sc;
    public static void main(String[] args) {
        sc = new Scanner(System.in);
        System.out.println("Ingrese el nombre del estudiante: ");
        String nombre = sc.next();
        System.out.println("Ingrese la primer nota del estudiante: ");
        float nota1 = sc.nextFloat();
        System.out.println("Ingrese la segunda nota del estudiante: ");
        float nota2 = sc.nextFloat();
        System.out.println("Ingrese la tercera nota del estudiante: ");
        float nota3 = sc.nextFloat();

        var promedio = Math.round(((nota1 + nota2 + nota3)/3)*100.0)/100.0;
        if(promedio >= 3) {
            System.out.println("El promedio de la nota del estudiante " + nombre + " es: " + promedio + ", Aprobado.");
        }
        else {
            System.out.println("El promedio de la nota del estudiante: " + nombre + " es: " + promedio + ", Reprobado.");
        }
    }
}
