import java.util.Scanner;

public class EJ15_factoriales {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero: ");
        int num = sc.nextInt();
        sc.close();

        var solucion = sumaFactorial(num);
        System.out.println(solucion);
    }

    private static int sumaFactorial(int num) {
        var resultado = 0;
        for (int i = num; i >= 0; i--){
            var suma = 0;
            for (int x = 0; x <= i; x++){
                if(x == 0){
                    suma += 1;
                }
                else{
                    suma *= x;
                }
            }
            resultado += suma; 
        }
        
        return resultado;
    }
}
