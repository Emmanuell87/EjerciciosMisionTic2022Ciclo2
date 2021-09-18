package co.edu.utp.misiontic2022.c2;

public class Empleado extends Persona {

    //Atributos

    private String id_empleado;  
    private String titulo_empleado;

    //Constructores
    public Empleado() {
        super("Angie");
        System.out.println("Este es el constructor de Empleado");
    }

    //Getters and Setters
    public String getId_empleado() {
        return id_empleado;
    }
    public void setId_empleado(String id_empleado) {
        this.id_empleado = id_empleado;
    }
    public String getTitulo_empleado() {
        return titulo_empleado;
    }
    public void setTitulo_empleado(String titulo_empleado) {
        this.titulo_empleado = titulo_empleado;
    }

}
