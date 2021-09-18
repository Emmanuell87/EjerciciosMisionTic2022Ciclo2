import java.util.Scanner;

public class EJ3_clase01 {
    public static void main(String[] args) {
        int salario = 1000;
        int bonus = 250;
        int limiteVentasBonus = 10;

        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el numero de ventas del vendedor");

        int ventas = sc.nextInt();
        sc.close();

        if (ventas > limiteVentasBonus){
            salario += bonus;
        }

        System.out.println("El salario del vendedor en esta semana es de: $" + salario);

    }
}
