public class EJ12_sinMultiplo3 {
    public static void main(String[] args) {

        //solucion utilizando FOR
        System.out.println("UTILIZANDO FOR");
        for(int i = 0; i < 100; i++) {
            if (i%3 != 0){
                System.out.println(i);
            }
        }

        var i = 0;
        //solucion utilizando WHILE
        System.out.println("UTILIZANDO WHILE");
        while(i<100){
            if (i%3 != 0){ 
                System.out.println(i);
            }
            i++;
        }

        i = 0;
        //solucion utilizando DO WHILE
        System.out.println("UTILIZANDO DO WHILE");
        do{
            if(i%3 != 0){
                System.out.println(i);
            }
            i++;
        }while(i<100);

        
           
    }
}
