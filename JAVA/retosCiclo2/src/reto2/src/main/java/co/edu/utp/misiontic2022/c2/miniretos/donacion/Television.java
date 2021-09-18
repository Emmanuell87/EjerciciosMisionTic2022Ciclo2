package co.edu.utp.misiontic2022.c2.miniretos.donacion;
public class Television extends Electrodomestico {
    
    //Atributos
    private Integer PULGADAS_BASE;
    private Integer pulgadas;
    private Boolean sintonizadorTDT;

    //Constructores
    public Television(){
        this.sintonizadorTDT = false;
        this.PULGADAS_BASE = 20;
        this.pulgadas = PULGADAS_BASE;
    }

    public Television(Double precioBase, Integer peso){
        // Código
        this.setPrecioBase(precioBase);
        this.setPeso(peso);
        this.sintonizadorTDT = false;
        this.PULGADAS_BASE = 20;
        this.pulgadas = PULGADAS_BASE;
    }
        
    public Television(Double precioBase, Integer peso, char consumoW, Integer pulgadas, boolean sintonizadorTDT){
        // Código
        this.setPrecioBase(precioBase);
        this.setPeso(peso);
        this.comprobarConsumoW(consumoW);
        this.pulgadas = pulgadas;
        this.sintonizadorTDT = sintonizadorTDT;
        
    }
       
    //Metodos
    public Double calcularPrecio(){
        var precioBase = getPrecioBase();
        if(this.sintonizadorTDT == true){
            precioBase += 50.0;
        }
        if (this.pulgadas > 40){
            precioBase = precioBase * 1.3;
        }
        var adicion = 0;
        switch(this.getConsumoW()){
            case 'A':
                adicion += 100;
                break;
            case 'B':
                adicion += 80;
                break;
            case 'C':
                adicion += 60;
                break;
            case 'D':
                adicion += 50;
                break;
            case 'E':
                adicion += 30;
                break;
            case 'F':
                adicion += 10;
                break;     
        }

        var peso = this.getPeso();
        if(peso >=0 && peso < 19){
            adicion += 10;
        } else if(peso >= 19 && peso < 49){
            adicion += 50; 
        } else if(peso >= 49 && peso < 80){
            adicion += 80; 
        } else if(peso >= 79){
            adicion += 100; 
        }


        return precioBase + adicion;
    }
}
