package co.edu.utp.misiontic2022.c2;

public abstract class Pieza implements Dibujable, ElementoMovil{

    private String color;

    
    public boolean Capturar(){
        // Si en la casilla en la que se mueve se encuentra una pieza 
        //del oponente, entonces captura la pieza
        return true;
    }

    public abstract boolean mover();

}
