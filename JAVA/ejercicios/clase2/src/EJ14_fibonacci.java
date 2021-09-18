import java.util.ArrayList;
import java.util.Scanner;

public class EJ14_fibonacci {
    
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero que indique cuantos términos de la secuencia fibonacci quieres ver: ");
        int cantTerminos = sc.nextInt();
        sc.close();

        ArrayList<Integer> secuencia = secuenciaFibonacci(cantTerminos);
        System.out.println(secuencia);
    }



    private static ArrayList<Integer> secuenciaFibonacci(int cantTerminos) {
        
     
        ArrayList<Integer> secuencia = new ArrayList<Integer>();
        secuencia.add(0);
        secuencia.add(1);
        
        if (cantTerminos > 2){
            for (int i = 0; i < cantTerminos-2; i++){
                var n = secuencia.get(secuencia.size()-2);
                var m = secuencia.get(secuencia.size()-1);
                var newNum = n + m; 
                secuencia.add(newNum);
            }
        }

        return secuencia;
    }

}
