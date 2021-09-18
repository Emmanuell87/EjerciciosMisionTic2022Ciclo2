public class EJ16_eliminarCaracteres {
    public static void main(String[] args) {
        StringBuffer cadenaCaracteres = new StringBuffer("ZYWXVUTSRQPONMLKJIHGFEDCBA");

        System.out.println(cadenaCaracteres);
        var condicion = cadenaCaracteres.length()-1;
        for (int i = 0; i < condicion; i++){
            cadenaCaracteres.deleteCharAt(0);
            System.out.println(cadenaCaracteres);
        }
    }
}
