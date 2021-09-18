import java.util.Scanner;

public class EJ5_clase01 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la nota");
        String nota = sc.next();
        sc.close();
        String mensaje = "";

        switch (nota) {
            case "E":
                mensaje = "Excelente Trabajo!, la mejor nota";
                break;
            case "S":
                mensaje = "Sobresaliente, buena nota";
                break;
            case "R":
                mensaje = "Regular, puedes hacerlo mejor";
                break;
            case "I":
                mensaje = "Insuficiente, vuelve a intentarlo";
                break;
        }

        System.out.println(mensaje);

    }

}
