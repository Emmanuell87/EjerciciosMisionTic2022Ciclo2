package co.edu.utp.misiontic2022.c2;

import java.util.Scanner;

public class numeroDeLaSuerte {
    
    //Vista / Interacción
    public static void saludo(){
        System.out.println("Hola - APP Número de la suerte");
    }

    //1. Solicita la fecha nacimiento en formato String
    public static String leerFecha(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresar la fecha DD/MM/AAAA");
        String fecha = sc.nextLine();
        sc.close();
        return fecha;
    }

    // 2. Extraer las porciones que hacen referencia al dia, mes y año (split)
    public static int obtenerNumerosSuerte(String fecha){
        // Variable que almacena el resultado de la
        int numeroSuerte = 0;
        // 2. Extraer las porciones
        //"08/06/2003"   ->  ["08", "06", "2003"]
        String [] arregloFecha = fecha.split("/", 3);

        // Variables para las versiones numericas
        int valorDia = Integer.parseInt(arregloFecha[0]);
        int valorMes = Integer.parseInt(arregloFecha[1]);
        int valorAño = Integer.parseInt(arregloFecha[2]);

        //4. Sumar los pedazos y almacenarlos
        int sumaPartesFecha = valorDia + valorMes + valorAño;

        //Convertir a String sumaPartesFecha
        String sumaPartesFechaCadena = Integer.toString(sumaPartesFecha);

        //5. De la sumatoria extraer las cifras y //6. Sumar las cifras y retornar, numeroDeLaSuerte
        for(int i = 0; i < sumaPartesFechaCadena.length(); i++){
            numeroSuerte = numeroSuerte + Character.getNumericValue(sumaPartesFechaCadena.charAt(i));
        }
        return numeroSuerte;
    }

    public static void reportarNumeroSuerte(int numeroSuerte){
        System.out.println("El numero de la suerte es: " + numeroSuerte);
    }

    public static void main(String[] args) {
        saludo();
        String datoFecha = leerFecha();
        reportarNumeroSuerte(obtenerNumerosSuerte(datoFecha));
        
    }
}
