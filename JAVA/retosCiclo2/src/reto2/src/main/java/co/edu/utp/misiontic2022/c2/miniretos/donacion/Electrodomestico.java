package co.edu.utp.misiontic2022.c2.miniretos.donacion;
public class Electrodomestico {

    //Atributos
    private Integer PESO_BASE;
    private char CONSUMO_W_BASE;
    private Double PRECIO_BASE;
    private Integer peso;
    private char consumoW;
    private Double precioBase;

    //Constructores
    Electrodomestico(){
        this.PESO_BASE = 5;
        this.CONSUMO_W_BASE = 'F';
        this.PRECIO_BASE = 100.0;
        this.peso = PESO_BASE;
        this.consumoW = CONSUMO_W_BASE;
        this.precioBase = PRECIO_BASE;
    }

    public Electrodomestico(Double precioBase, Integer peso) {
        this.CONSUMO_W_BASE = 'F';
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = CONSUMO_W_BASE;
    }

    public Electrodomestico(Double precioBase, Integer peso, char consumoW){
        //codigo
        this.precioBase = precioBase;
        this.peso = peso;
        comprobarConsumoW(consumoW);
    }

    //Metodos
    public void comprobarConsumoW(char consumoW){
        
        if(Character.compare(consumoW, 'A') >= 0 && Character.compare(consumoW, 'F') <= 0){
            this.consumoW = consumoW;
        } else {
            this.consumoW = CONSUMO_W_BASE;
        }
    }

    public Double calcularPrecio(){
        var adicion = 0;
        switch(this.consumoW){
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

        if(this.peso >=0 && this.peso < 19){
            adicion += 10;
        } else if(this.peso >= 19 && this.peso < 49){
            adicion += 50; 
        } else if(this.peso >= 49 && this.peso < 80){
            adicion += 80; 
        } else if(this.peso >= 79){
            adicion += 100; 
        }

        
        return this.precioBase + adicion;
    }

    //Getters and Setters
    public Integer getPeso() {
        return peso;
    }

    public void setPeso(Integer peso) {
        this.peso = peso;
    }

    public char getConsumoW() {
        return consumoW;
    }

    public void setConsumoW(char consumoW) {
        this.consumoW = consumoW;
    }

    public Double getPrecioBase() {
        return precioBase;
    }

    public void setPrecioBase(Double precioBase) {
        this.precioBase = precioBase;
    }

    

}
