package co.edu.utp.misiontic2022.c2.reto;
public class Estufa extends Electrodomestico {
    
    //Atributos
    protected final static Integer BOQUILLAS_BASE = 2;

    private Integer boquillas;
    private Boolean horno;

    //Constructores
    public Estufa(){
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W_BASE, BOQUILLAS_BASE, false);
    }

    public Estufa(Double precioBase, Integer peso){
        // Código
        this(precioBase, peso, CONSUMO_W_BASE, BOQUILLAS_BASE, false);
    }
        
    public Estufa(Double precioBase, Integer peso, char consumoW, Integer boquillas, boolean horno){
        // Código
        super(precioBase, peso, consumoW);
        this.boquillas = boquillas;
        this.horno = horno;
        
    }
       
    //Metodos
    public Double calcularPrecio(){
        
        

        var adicion = super.calcularPrecio();

        if (this.boquillas > 2){
            adicion += precioBase * 0.4; 
        }
        if(this.horno == true){
           adicion += 150.0;
        }


        return  adicion;
    }
}
