import java.util.Scanner;

public class EJ3_quitarCifras {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero entero: ");
        int n = sc.nextInt();
        System.out.println("Ingrese la cantidad de cifras que desea quitarle");
        int m = sc.nextInt();
        sc.close();
        
        String string_n = Integer.toString(n);
        if (m > string_n.length()){
            System.out.println("Por favor ingrese una cantidad de cifra a quitar, que sea menor o igual a las cifras que tiene su número");
            
        }
        else{
            var potencia = (int) Math.pow(10, m);
            
            var newNumero = n / potencia;
            System.out.println(newNumero);
        }

        
    }

}
