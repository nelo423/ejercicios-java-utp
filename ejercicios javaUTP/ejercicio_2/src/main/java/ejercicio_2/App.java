package ejercicio_2;

import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // Mensaje de Bienvenida
        System.out.println("Bienvenido a esta unidad !");
        //Ejercicio No 1
        int x = 0;
        int y = 0;
        int r = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite número_1 : ");
        x = sc.nextInt();
        System.out.println("Digite número_2 : ");
        y = sc.nextInt();
        
        r = x + y;
        System.out.println("La suma de "+ x + " y " + y + " es igual a " + r);
        
        r = x - y;
        System.out.println("La resta de "+ x + " y " + y + " es igual a " + r);        
       
        r = x / y ;
        System.out.println("La division de "+ x + " y " + y + " es igual a " + r);
        
        r  = x * y;
        System.out.println("La multiplicacion de "+ x + " y " + y + " es igual a " + r);
    }
}



