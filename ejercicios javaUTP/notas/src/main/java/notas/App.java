package notas;

import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
    float acum = 1;    
    float notas = 0;
    Scanner r = new Scanner(System.in);
    System.out.println("Ingrese Nombre :");
    String nombre = r.nextLine();
    System.out.println("Ingrese la cantidad de notas a promediar :");
    float cn = r.nextFloat();
    while (acum <= cn ){
        System.out.println("Ingrese la nota No : " + acum);
        float n = r.nextFloat();
        notas += n;
        acum ++; 
    }
    float promedio = notas /cn;
    System.out.println("El promedio es : " + promedio);
    if (promedio >= 3){
        System.out.println(nombre + " Aprobó ");
        }
        else {
            System.out.println(nombre + " Reprobó ");
        }
    }
}
