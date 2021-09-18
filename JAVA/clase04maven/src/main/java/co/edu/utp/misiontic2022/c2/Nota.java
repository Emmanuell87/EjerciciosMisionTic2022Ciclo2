package co.edu.utp.misiontic2022.c2;

public class Nota {
    // 1) atributos (antes las variables estaban sueltas)
    private int escala100;
    private double escala5;
    private String cualitativa;
    private String nombre; // Ecaluacion, taller o reto correspondiente

    // CONTRUCTORES (EN ESTE CASO 4)
    Nota(){
        this.escala100 = 0;
        this.escala5 = 0;
        this.cualitativa = "";
    }

    Nota(int pEscala100){
        this.escala100 = pEscala100;
        this.escala5 = (double)pEscala100/20;

        if(pEscala100 >= 60){
            this.cualitativa = "Aprobado";
        } else {
            this.cualitativa = "Reprobado";
        }
    }

    Nota(double pEscala5){
        this.escala5 = pEscala5;
        this.escala100 = (int) pEscala5*20;

        if(pEscala5 >= 2.95){
            this.cualitativa = "Aprobado";
        } else {
            this.cualitativa = "Reprobado";
        }
    }

    Nota(double pEscala5, int pEscala100, String pCualitativo){
        this.escala5 = pEscala5;
        this.escala100 = pEscala100;
        this.cualitativa = pCualitativo;
    }

    //3) Metodos - Comportamiento

    public void mostrarNotasConsola(){
        System.out.println("------------------------");
        System.out.println("-------Info nota--------");
        System.out.println("Valor escala 5 -> " + this.escala5);
        System.out.println("Valor escala 100 -> " + this.escala100);
        System.out.println("Valor escala Cualitativa -> " + this.cualitativa);
    }

    //4 Getters
    
    public int getEscala100(){
        return escala100;
    }

    public double getEscala5(){
        return escala5;
    }

    public String getCualitativa(){
        return cualitativa;
    }
    
    public String getNombre(){
        return nombre;
    }
    
    // 5) Setters

    public void setEscala5(int nuevaEscala5){
        this.escala5 = nuevaEscala5;
    }

    public void setEscala100(int nuevaEscala100){
        this.escala100 = nuevaEscala100;
    }

    public void setCualitativa(String nuevaCualitativa){
        this.cualitativa = nuevaCualitativa;
    }


}
