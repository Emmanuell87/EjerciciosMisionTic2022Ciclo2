package co.edu.utp.misiontic2022.c2;

public class Persona {
    private String nombre;
    private Integer edad;
    private String genero;

    //Constructores
    Persona(){
        System.out.println("Yo estoy en el primer constructor Persona");
    }
    
    Persona(String nombre){
        System.out.println("Este es el segundo constructor con nombre " + nombre);
    }


    // Getters and Setters
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public Integer getEdad() {
        return edad;
    }
    public void setEdad(Integer edad) {
        this.edad = edad;
    }
    public String getGenero() {
        return genero;
    }
    public void setGenero(String genero) {
        this.genero = genero;
    }

    
}
