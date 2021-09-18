package co.edu.utp.misiontic2022.c2;

public class Casilla implements Dibujable {

    //Atributos
    private Color color; // Enum Color (Blanco o Negro)
    private Integer fila;
    private Integer columna;

    //Constructores
    Casilla(Integer fila, Integer columna){
        this.fila = fila;
        this.columna = columna;
        this.color = (fila + columna) % 2 == 0 ? color.BLANCO: color.NEGRO;
    }

    public boolean Ocupada(){
        return true;
    }

    @Override
    public void pintar() {
        // TODO Auto-generated method stub
        
    }

    @Override
    public void posicionar(Integer x, Integer y) {
        // TODO Auto-generated method stub
        
    }
}
