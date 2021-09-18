package co.edu.utp.misiontic2022.c2;

public class Tablero {
    
    //Atributos
    private Casilla[] casillas;

    //Constructores
    public Tablero() {
        casillas = new Casilla[64];

        for (int i = 0; i < 64; i++){
            casillas[i] = new Casilla(i/8, i%8);
        }
    }

    public boolean HacerEnroque(){
        return true;
    }

    public boolean HacerJaque(){
        return true;
    }

    public boolean HacerJaqueMate(){
        return true;
    }
}
