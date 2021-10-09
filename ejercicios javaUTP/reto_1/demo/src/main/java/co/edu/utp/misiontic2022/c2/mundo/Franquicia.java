package co.edu.utp.misiontic2022.c2.mundo;

public class Franquicia{
// atributos
    private String proyecto;
    private int tiempo;
    private double capital;
    private double interes;
// constructor
    public Franquicia(){
        proyecto = "";
        tiempo = 0;
        capital = 0;
        interes = 0;
    }
//metodos
    public String getNombreProyecto(){
        return proyecto;
    }
       
    public double calcularInteresSimple(){
        double interesSimple = capital * interes * tiempo;
        return interesSimple;
    }

    public double calcularInteresCompuesto(){
        double interesCompuesto = capital * (Math.pow(1 + interes, tiempo)-1);
        return interesCompuesto;   
    }

    public String compararFranquicia(int pTiempo, double pCapital, double pInteres){
        tiempo = pTiempo;
        capital = pCapital;
        interes = pInteres;
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        if(diferencia > 0){
           return "La diferencia en el total de intereses generados para el proyecto, si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de interés Simple, asciende a la cifra de: $" + diferencia ;
        }
        else {
            return "Faltan datos para calcular la diferencia en el total de intereses generados para el proyecto.";

    }
}
}
