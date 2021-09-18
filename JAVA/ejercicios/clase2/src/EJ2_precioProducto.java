import java.util.Scanner;

public class EJ2_precioProducto {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el precio del producto; ");
        double precioUnidad = sc.nextDouble();
        System.out.println("Ingrese el número de productos vendidos: ");
        int cantidadProductos = sc.nextInt();
        System.out.println("Ingrese el porcentaje de iva aplicado: Ej si es 19% ingresar 19");
        double iva = sc.nextDouble();
        sc.close();

        var resultado = Math.round((precioUnidad * cantidadProductos * ((iva/100) + 1)) * 100.0) / 100.0;
        System.out.println(resultado);

        
    }
}
