public class temperaturas {
    public static void main(String[] args) {
        
        double[] gradoscentigrados = new double[5];

        gradoscentigrados[0] = -273.15;
        gradoscentigrados[1] = 30;
        gradoscentigrados[2] = -280;
        gradoscentigrados[3] = -15;
        gradoscentigrados[4] = 300;

        for (int i = 0; i < 5; i++){
            if (gradoscentigrados[i] < -273.15){
                System.out.println("Error, el valor en centigrados: " + gradoscentigrados[i] + " no puede ser menor al cero absoluto (-273.15)");
            }
            else {
                var fahrenheit = Math.round((centigradosAfahrenheit(gradoscentigrados[i])) * 100.0)/ 100.0;
                System.out.println("La temperatura en centigrados: " + gradoscentigrados[i] + "°C, equivale en fahrenheit a: " + fahrenheit + "°F");
            }
        }
    }


    public static double centigradosAfahrenheit(double centigrados){
        
        var fahrenheit = 32 + (9*centigrados/5);

        return fahrenheit;
        
    }
}
