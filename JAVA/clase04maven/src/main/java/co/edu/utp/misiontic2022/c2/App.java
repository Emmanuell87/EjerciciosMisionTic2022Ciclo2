package co.edu.utp.misiontic2022.c2;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {

        //Interactuamos con nuestra clase materia -> creamos una nueva materia
        Materia materia = new Materia(35, 85, 40, 60, 70);

        //Utilizamos los metodos creados, (comportamientos)
        materia.calcularPromedioAjustado();
        materia.calcularPromedio();

        //Como quedan las materias
        materia.mostrarMateria();


       
        // Nota notaVacia = new Nota();
        // /*
        // System.out.println("----------------------------------------------------------");
        // System.out.println("Nota vacia");
        // System.out.println("Valor escala 5 -> " + notaVacia.getEscala5());
        // System.out.println("Valor escala 100 -> " + notaVacia.getEscala100());
        // System.out.println("Valor escala Cualitativa -> " + notaVacia.getCualitativa());
        // */

        // notaVacia.mostrarNotasConsola();

        // Nota notaEscala5 = new Nota(4.0);
        // /*
        // System.out.println("----------------------------------------------------------");
        // System.out.println("NotaEscala 5 ");
        // System.out.println("Valor escala 5 -> " + notaEscala5.getEscala5());
        // System.out.println("Valor escala 100 -> " + notaEscala5.getEscala100());
        // System.out.println("Valor escala Cualitativa -> " + notaEscala5.getCualitativa());
        // */
        // notaEscala5.mostrarNotasConsola();

        // Nota notaEscala100 = new Nota(60);
        // /*
        // System.out.println("----------------------------------------------------------");
        // System.out.println("NotaEscala 100 ");
        // System.out.println("Valor escala 5 -> " + notaEscala100.getEscala5());
        // System.out.println("Valor escala 100 -> " + notaEscala100.getEscala100());
        // System.out.println("Valor escala Cualitativa -> " + notaEscala100.getCualitativa());
        // */
        // notaEscala100.mostrarNotasConsola();

        // Nota notaTodos = new Nota(5, 100, "Aprobado");
        // /*
        // System.out.println("----------------------------------------------------------");
        // System.out.println("Nota TODOS ");
        // System.out.println("Valor escala 5 -> " + notaEscala100.getEscala5());
        // System.out.println("Valor escala 100 -> " + notaEscala100.getEscala100());
        // System.out.println("Valor escala Cualitativa -> " + notaEscala100.getCualitativa());
        // */
        // notaTodos.mostrarNotasConsola();

        
    }
}
