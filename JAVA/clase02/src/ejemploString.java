public class ejemploString {
    public static void main(String[] args) {
        String cadena1 = "Esto es una cadena";
        String cadena2 = "Hola";
        String cadena3 = "hola";
        String cadena4 = "            hola  asdfghj           ";

        System.out.println("Longitud de la cadena es: " + cadena1.length());
        System.out.println("Función indexof(): " + cadena1.indexOf("una"));
        System.out.println("Función lastIndexOf(): " + cadena1.lastIndexOf("e"));
        System.out.println("Función charAt(): " + cadena2.charAt(3));
        System.out.println("Función .equals(): " + cadena2.equals(cadena3));
        System.out.println("Función .equalsIgnoreCase(): " + cadena2.equalsIgnoreCase(cadena3));
        System.out.println("Función .trim(): " + cadena4.trim());
    }
}
