package ejercicio_1;

/**
 * Hello world!
 *
 */
import java.util.Scanner;
public class App 
{
    public static void main( String[] args )throws Exception {
        //Mensaje de Bienvenida
        System.out.println("Bienvenido a esta unidad !");
        //Ejercicio No 2
        double x = sc.nextDouble();
        double y = sc.nextDouble();
        double z = sc.nextDouble();
        String num = sc.nextString();
        Scanner sc = new Scanner(System.in);
        //invocando el metodo promNum
        System.out.print("Ingrese su nombre :");
        System.out.print("Digite evaluacion_1 : ");
        System.out.print("Digite evaluacion_2 : ");
        System.out.print("Digite evaluacion_3 : ");
        System.out.println(promNum(num));
        }
    public String promNum( String num){
        String r = "";
        if ((x+y+z)/3)>= 3 {
            r = num +"Aprobado";
        } else{
            r = num + "Reprobado";
        }
              
    }
}

