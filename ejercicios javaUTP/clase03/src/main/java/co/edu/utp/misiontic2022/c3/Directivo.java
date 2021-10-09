package co.edu.utp.misiontic2022.c3;

public class Directivo {

    private String categoria;
    private Empleado empleado;

    public Directivo(String categoria , Empleado empleado){
        this.categoria = categoria;
        this.empleado = empleado;
    }
    
    public String toString(){
        return "Rango: " + categoria + " Empleado: " + empleado.toString();
    }

    public String rangoDirectivo(Empleado empleado){
        return empleado.getSueldoBruto();
    }
}
