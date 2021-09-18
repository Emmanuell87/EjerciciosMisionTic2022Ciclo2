package co.edu.utp.misiontic2022.c2.miniretos.donacion;
public class Lavadora extends Electrodomestico {
    
    //Atributos
    private Integer CARGA_BASE;
    private Integer carga;
    

    
    //Constructores
    Lavadora(){
        this.CARGA_BASE = 5;
        this.carga = CARGA_BASE;
    }

    Lavadora(Double precioBase, Integer peso){
        this.setPrecioBase(precioBase);
        this.setPeso(peso);
        this.CARGA_BASE = 5;
        this.carga = CARGA_BASE;
    }

    Lavadora(Double precioBase, Integer peso, char consumoW, Integer carga){
        this.setPrecioBase(precioBase);
        this.setPeso(peso);
        this.comprobarConsumoW(consumoW);
        this.carga = carga;
    }

    //Metodos
    public Double calcularPrecio(){
        var precioBase = getPrecioBase();
        if(this.carga > 30){
            precioBase += 50;
        }
        this.setPrecioBase(precioBase);

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
        System.out.println("------------");
        System.out.println(this.getConsumoW());
        System.out.println(this.getPeso());
        System.out.println(this.getPrecioBase());

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
