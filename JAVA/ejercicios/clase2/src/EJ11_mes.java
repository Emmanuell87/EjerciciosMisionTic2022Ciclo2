import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class EJ11_mes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un número entero: ");
        int numMes = sc.nextInt();
        sc.close();
        
        Map<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "Enero y tiene 31 días");
        map.put(2, "Febrero y tiene 28 días");
        map.put(3, "Marzo y tiene 31 días");
        map.put(4, "Abril y tiene 30 días");
        map.put(5, "Mayo y tiene 31 días");
        map.put(6, "Junio y tiene 30 días");
        map.put(7, "Julio y tiene 31 días");
        map.put(8, "Agosto y tiene 31 días");
        map.put(9, "Septiembre y tiene 30 días");
        map.put(10, "Octubre y tiene 31 días");
        map.put(11, "Noviembre y tiene 30 días");
        map.put(12, "Diciembre y tiene 31 días");

        if(numMes >= 1 && numMes <= 12){
            var mesNombre = map.get(numMes);
            System.out.println("El mes: " + numMes + ", corresponde a: " + mesNombre);
        }
        else{
            System.out.println("El número ingresado: " + numMes + ", no corresponde a un mes");
        }
    }
}
