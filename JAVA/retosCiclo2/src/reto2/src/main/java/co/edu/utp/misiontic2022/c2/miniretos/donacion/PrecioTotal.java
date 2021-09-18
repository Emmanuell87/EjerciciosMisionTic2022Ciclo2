package co.edu.utp.misiontic2022.c2.miniretos.donacion;
public class PrecioTotal {
    
    //Atributos
    private Double totalElectrodomesticos;
    private Double totalTelevisores;
    private Double totalLavadoras;
    private Electrodomestico[] listaElectrodomesticos;

    //Constructores
    PrecioTotal(Electrodomestico[] listaElectrodomesticos){
        this.listaElectrodomesticos = listaElectrodomesticos;
        this.totalElectrodomesticos = 0.0;
        this.totalTelevisores = 0.0;
        this.totalLavadoras = 0.0;
        for(int i = 0; i < this.listaElectrodomesticos.length; i++){
           if(this.listaElectrodomesticos[i] instanceof Television){
                this.totalTelevisores += listaElectrodomesticos[i].calcularPrecio();
                this.totalElectrodomesticos += totalTelevisores;
            } else if(this.listaElectrodomesticos[i] instanceof Lavadora){
                this.totalLavadoras += listaElectrodomesticos[i].calcularPrecio();
                this.totalElectrodomesticos += totalLavadoras;
            } else{
                this.totalElectrodomesticos += listaElectrodomesticos[i].calcularPrecio();
            }
        }
    }

    //Metodos
    public void mostrarTotales() {
        // Código

        //Mostramos los resultados
        System.out.println("La suma del precio de los electrodomésticos es de " + totalElectrodomesticos);
        System.out.println("La suma del precio de las lavadoras es de " + totalLavadoras);
        System.out.println("La suma del precio de las televisiones es de " + totalTelevisores);
    }
}
