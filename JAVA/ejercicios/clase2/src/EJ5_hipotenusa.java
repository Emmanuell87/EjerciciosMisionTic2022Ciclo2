import java.util.Scanner;

public class EJ5_hipotenusa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la longitud del primer cateto: ");
        double catetoA = sc.nextDouble();
        System.out.println("ingrese la longitud del segundo cateto");
        double catetoB = sc.nextDouble();
        sc.close();

        double hipotenusa = hipotenusa(catetoA, catetoB);
        System.out.println(hipotenusa);
        // un printf en este caso sirve para reducir un numero a x cantidad de decimales
        System.out.printf("%.1f cm. %.2f cm", hipotenusa);
    }

    private static double hipotenusa(double catetoA, double catetoB) {
        var hipotenusa = Math.round((Math.sqrt(catetoA*catetoA + catetoB*catetoB)) * 100.0)/ 100.0;
        return hipotenusa;
    }
}
