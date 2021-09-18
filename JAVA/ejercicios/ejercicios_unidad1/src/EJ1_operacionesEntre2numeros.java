import java.util.Scanner;

public class EJ1_operacionesEntre2numeros {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el primer número: ");
        double num1 = sc.nextDouble();
        System.out.println("Ingrese el segundo número: ");
        double num2 = sc.nextDouble();
        sc.close();

        var suma = num1 + num2;
        System.out.println("La suma entre: " + num1 + "+" + num2 + " es: " + suma);
        var resta = num1 - num2;
        System.out.println("La resta entre: " + num1 + "-" + num2 + " es: " + resta);
        var multiplicacion = num1 * num2;
        System.out.println("La multiplicacion entre: " + num1 + "*" + num2 + " es: " + multiplicacion);
        if(num2 != 0){
            var division = Math.round((num1/num2)*100.0)/ 100.0;
            System.out.println("La division entre: " + num1 + "/" + num2 + " es: " + division);
        }
        else{
            System.out.println("No es posible dividir entre 0: ");
        }
        
    }
}
