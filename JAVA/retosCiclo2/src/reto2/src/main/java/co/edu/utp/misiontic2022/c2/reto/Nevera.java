package co.edu.utp.misiontic2022.c2.reto;
public class Nevera extends Electrodomestico {
    
    //Atributos
    protected final static Integer CAPACIDAD_BASE = 100;
    private Integer capacidad;
    

    
    //Constructores
    Nevera(){
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W_BASE, CAPACIDAD_BASE);
    }

    Nevera(Double precioBase, Integer peso){
        this(precioBase, peso, CONSUMO_W_BASE, CAPACIDAD_BASE);
    }

    Nevera(Double precioBase, Integer peso, char consumoW, Integer capacidad){
        super(precioBase, peso, consumoW);
        this.capacidad = capacidad;
    }

    //Metodos
    public Double calcularPrecio(){

        
        Double adicion = super.calcularPrecio();

        if(this.capacidad > 250){
            adicion += 100;
        }


        return adicion;
    }

}
