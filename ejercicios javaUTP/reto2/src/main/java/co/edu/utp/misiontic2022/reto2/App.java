package co.edu.utp.misiontic2022.reto2;

/**
 * Hello world!
 *
 */
public class App{ 
public static void main(String[] args) {
        
    Carro carro[] = new Carro[5];
        
        carro[0] = new Volqueta(100.0, 10.0);
        carro[1] = new Volqueta(200);
        carro[2] = new CarroNascar(150, 20.0);
        carro[3] = new CarroNascar();
        carro[4] = new Volqueta();

        PrecioTotal solucion = new PrecioTotal(carro);
        
        solucion.mostrarTotales();
    }
}
