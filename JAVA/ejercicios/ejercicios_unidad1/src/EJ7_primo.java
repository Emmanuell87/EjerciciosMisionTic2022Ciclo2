import java.util.Scanner;

/*
Pedir un número, comprobar si es primo y preguntar si quiere introducir más
(S/N) y volver a pensar.
*/


public class EJ7_primo {

    public static void saludo(){
        System.out.println("APP - es primo?");
    }

    public static int obtenerNumero(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero.");
        int numero = sc.nextInt();
        sc.close();

        return numero;
    }

    public static boolean esPrimo(int numero){

        int contador = 2;
        boolean primo=true;

        while ((primo) && (contador<numero/2)){
            if (numero % contador == 0){
                primo = false;
            }
            contador++;
        }

        return primo;
    }

    public static void mostrarResultado(boolean resultado, int numero){
        if(resultado == true){
            System.out.println("El numero " + numero + " es primo");
        }
        else{
            System.out.println("El numero " + numero + " no es primo");
        }
    }

    public static void main(String[] args) {
        saludo();
        
        var numero = obtenerNumero();
        var es_primo = esPrimo(numero);
        mostrarResultado(es_primo, numero);
            
        
    }
}
