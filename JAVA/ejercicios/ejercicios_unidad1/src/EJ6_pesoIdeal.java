
import java.util.Scanner;

/*
Realiza un programa que solicite el sexo (H/M) y la altura (cm) al usuario y
que calcule el peso ideal.
    peso ideal mujeres = altura - 120
    peso ideal hombres = altura - 110
*/


public class EJ6_pesoIdeal {
    public static void main(String[] args) {
        var datos = solicitarDatos();
        var pesoIdeal = calcularPesoIdeal(datos);
        mostrarResultado(pesoIdeal);
    }


    public static Object[] solicitarDatos(){
        Scanner sc = new Scanner(System.in);

        // Capturar sexo
        System.out.println("Ingrese su sexo si es hombre o mujer con H/M respectivamente.");
        var sexo = sc.nextLine();
        
        // Capturar altura en cm
        System.out.println("Ingrese su altura en cm.");
        double altura = sc.nextDouble();
        sc.close();

        Object datos[] = new Object[2];

        datos[0] = sexo;
        datos[1] = altura;
        
        return datos;
    }

    private static double calcularPesoIdeal(Object[] datos) {

        var pesoIdeal = 0.0;
        String sexo = (String) datos[0];
        double estatura = (double) datos[1];

        if (sexo.equalsIgnoreCase("h")){
            pesoIdeal = estatura - 110;
        }
        else if(sexo.equalsIgnoreCase("m")){
            pesoIdeal = estatura - 120;
        }

        return pesoIdeal;        
    }

    public static void mostrarResultado(double resultado){

    
        System.out.printf("Su peso ideal es de: %.2f", resultado);
        

    }

}
