import java.util.Scanner;

public class EJ13_conversionMoneda {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de dinero a convertir: ");
        var dinero = sc.nextDouble();
        System.out.println("Ingrese la palabra 'Pesos' si desea convertir a pesos de lo contrario ingresar 'Dolar'");
        var convertirA = sc.next();
        sc.close();

        if (convertirA.equals("Dolar")){
            var conversion = dinero*0.00027;
            System.out.printf("%.2f Dolares", conversion); 
        }
        else if(convertirA.equals("Pesos")){
            var conversion = dinero/0.00027;
            System.out.printf("%.2f Pesos", conversion); 
        }
        else{
            System.out.println("Error, por favor ingrese bien la palabra clave que corresponda a la conversion a realizar");
        }
    }
}
