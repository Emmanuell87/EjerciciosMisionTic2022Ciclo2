package co.edu.utp.misiontic2022.c2.reto;

public class App {
    public static void main(String[] args) {

        Electrodomestico electrodomesticos2[] = new Electrodomestico[5];
        electrodomesticos2[0] = new Electrodomestico(300.0, 80, 'C');
        electrodomesticos2[1] = new Nevera(150.0, 20);
        electrodomesticos2[2] = new Estufa(500.0, 80, 'E', 42, false);
        electrodomesticos2[3] = new Electrodomestico();
        electrodomesticos2[4] = new Electrodomestico(600.0, 20, 'D');
        PrecioTotal solucion2 = new PrecioTotal(electrodomesticos2);
        solucion2.mostrarTotales();
       
    }
}


