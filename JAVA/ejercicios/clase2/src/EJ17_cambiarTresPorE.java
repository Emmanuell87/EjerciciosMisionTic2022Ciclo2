public class EJ17_cambiarTresPorE {
    public static void main(String[] args) {
        for (int i = 10000; i < 100000; i++) {
            String[] numString = Integer.toString(i).split("", 5);
            StringBuffer cadena = new StringBuffer();
            for (int x = 0; x < numString.length; x++) {
                
                String jaja = numString[x];
                if (jaja.equals("3")){
                    cadena = cadena.append("E");
                }
                else{
                    cadena = cadena.append(numString[x]);
                }
            }
            System.out.println(cadena);
            
        }
    }
}
