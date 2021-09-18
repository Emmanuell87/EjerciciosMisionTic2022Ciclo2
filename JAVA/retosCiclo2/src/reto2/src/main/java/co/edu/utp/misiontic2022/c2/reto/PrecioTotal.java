package co.edu.utp.misiontic2022.c2.reto;
public class PrecioTotal {
    
    //Atributos
    private Double totalElectrodomesticos = 0.0;
    private Double totalEstufa = 0.0;
    private Double totalNevera = 0.0;
    private Electrodomestico[] listaElectrodomesticos;

    //Constructores
    PrecioTotal(Electrodomestico[] listaElectrodomesticos){
        this.listaElectrodomesticos = listaElectrodomesticos;
        
    }

    //Metodos
    public void mostrarTotales() {
        // Código
        for(int i = 0; i < this.listaElectrodomesticos.length; i++){
            if (this.listaElectrodomesticos[i] instanceof Electrodomestico){
                this.totalElectrodomesticos += listaElectrodomesticos[i].calcularPrecio(); 
            }
            if(this.listaElectrodomesticos[i] instanceof Estufa){
                this.totalEstufa += listaElectrodomesticos[i].calcularPrecio();
            }
            if(this.listaElectrodomesticos[i] instanceof Nevera){
                this.totalNevera += listaElectrodomesticos[i].calcularPrecio();
            } 
            
        }

        //Mostramos los resultados
        System.out.println("La suma del precio de los Electrodomésticos es de " + totalElectrodomesticos);
        System.out.println("La suma del precio de las Neveras es de " + totalNevera);
        System.out.println("La suma del precio de las Estufas es de " + totalEstufa);
    }
}
