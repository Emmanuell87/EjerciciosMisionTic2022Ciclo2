package co.edu.utp.misiontic2022.c2;

//Import Primera forma
import org.apache.commons.math3.util.Precision;

//Import segunda forma
import java.math.BigDecimal;
import java.math.RoundingMode;


public class RedondearDecimales {

    public static void main(String[] args){
      //Primera forma
      System.out.println("***PRIMERA FORMA***");
      double input = 9476.2351;
      double roundedDbl = Precision.round(input,3);  
      System.out.println("Rounded Double value: "+roundedDbl); 
      
      
      // Segunda forma
      System.out.println("***SEGUNDA FORMA***");
      double val1 = 1.666666666666666;
      System.out.println("Double value: "+val1);
    
      BigDecimal bd = new BigDecimal(val1).setScale(2, RoundingMode.HALF_UP);
      double val2 = bd.doubleValue();
      System.out.println("Rounded Double value: "+val2);
    }
}
