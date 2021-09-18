import java.util.ArrayList;
import java.util.Scanner;

public class EJ10_fibonacci {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero que indique hasta donde quieres ver la secuencia de fibonacci: ");
        int numMax = sc.nextInt();
        sc.close();

        ArrayList<Integer> secuencia = secuenciaFibonacci(numMax);
        System.out.println(secuencia);
    }



    private static ArrayList<Integer> secuenciaFibonacci(int numMax) {
        

        ArrayList<Integer> secuencia = new ArrayList<Integer>();
        secuencia.add(0);
        secuencia.add(1);   
        while (true) {
            var n = secuencia.get(secuencia.size()-2);
            var m = secuencia.get(secuencia.size()-1);
            var newNum = n + m;
            if (newNum < numMax){
                secuencia.add(newNum);
            }
            else{ 
                break;
            }
        }
        
        return secuencia;
    }
}
