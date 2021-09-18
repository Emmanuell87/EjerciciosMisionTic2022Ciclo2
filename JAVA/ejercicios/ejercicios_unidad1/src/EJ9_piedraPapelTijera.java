import java.util.Scanner;

public class EJ9_piedraPapelTijera {
    private static Scanner sc; 
    
    public static void saludo(){
        System.out.println("               Juego - Piedra, papel o tijera               ");
    }

    public static String[] obtenerOpcionesJugadores(){
        sc = new Scanner(System.in);

        // Capturar opción jugador 1
        System.out.println("\n                   Turno Jugador 1.");
        System.out.println("Ingresa el dato correpondiente. Piedra(p), Papel(pa) o Tijera(t).");
        String jugador1 = sc.next();
        while (!(jugador1.equalsIgnoreCase("p") ||  jugador1.equalsIgnoreCase("pa") ||  jugador1.equalsIgnoreCase("t"))){
            System.out.println("Por favor, ingrese una opción valida.");
            jugador1 = sc.next();
        }

        // Capturar opción jugador 2
        System.out.println("\n                   Turno Jugador 2.");
        System.out.println("Ingresa el dato correpondiente. Piedra(p), Papel(pa) o Tijera(t).");
        String jugador2 = sc.next();
        while (!(jugador2.equalsIgnoreCase("p") || jugador2.equalsIgnoreCase("pa")  || jugador2.equalsIgnoreCase("t"))){
            System.out.println("Por favor, ingrese una opción valida.");
            jugador2 = sc.next();
        }


        String[] opcionesJugadores = {jugador1, jugador2};
        return opcionesJugadores;
    }

    public static int estadoJuego(String[] opcionesJugadores){

        
        // 0 si gana jugador1, 1 si gana jugador2 o 2 si es empate
        var ganador = 0;
        if(opcionesJugadores[0].equalsIgnoreCase("p")){
            if (opcionesJugadores[1].equalsIgnoreCase("pa")){
                ganador = 1;
            }
            else if(opcionesJugadores[1].equalsIgnoreCase("t")){
                ganador = 0;
            }
            else{
                ganador = 2;
            }
        }
        if(opcionesJugadores[0].equalsIgnoreCase("pa")){
            if (opcionesJugadores[1].equalsIgnoreCase("t")){
                ganador = 1;
            }
            else if(opcionesJugadores[1].equalsIgnoreCase("p")){
                ganador = 0;
            }
            else{
                ganador = 2;
            }
        }
        if(opcionesJugadores[0].equalsIgnoreCase("t")){
            if (opcionesJugadores[1].equalsIgnoreCase("p")){
                ganador = 1;
            }
            else if(opcionesJugadores[1].equalsIgnoreCase("pa")){
                ganador = 0;
            }
            else{
                ganador = 2;
            }
        }
        

        return ganador;
    }

    public static void mostrarResultado(int ganador){

        String mensaje = "";
        switch(ganador){
            case 0:
                mensaje = "Jugador 1 ha ganado.";
                break;
            case 1:
                mensaje = "Jugador 2 ha ganado.";
                break;
            case 2:
                mensaje = "Han empatado.";
        }

        System.out.println(mensaje);
    }

    public static boolean seguirJuego(){
        System.out.println("Desea seguir jugando?. S/N.");
        var dato =  sc.next();
        boolean again = false;
        if (!(dato.equalsIgnoreCase("s") || dato.equalsIgnoreCase("n"))){
            System.out.println("Por favor, ingrese una opción valida.");
            dato = sc.next();
        }
        else if(dato.equalsIgnoreCase("s")){
            again = true;
        }
        else{
            again = false;
        }

        
        
        return again;
    }
    
    public static void main(String[] args) {
        saludo();

        var again = true;
        while(again){
            //LIMPIAR CONSOLA
            System.out.print("\033[H\033[2J");
            System.out.flush();


            var opcionesJugadores = obtenerOpcionesJugadores();
            var resultadoJuego = estadoJuego(opcionesJugadores);
            mostrarResultado(resultadoJuego);
            sc.reset();
            again = seguirJuego();
        }
    }
}
