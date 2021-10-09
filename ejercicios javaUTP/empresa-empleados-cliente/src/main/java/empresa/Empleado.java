package empresa;

public class Empleado extends Persona {
    private Double sueldoBruto;

    private Directivo jefe;

    public Empleado(String nombre, Integer edad, Double sueldoBruto) {
        super(nombre, edad);
        this.sueldoBruto = sueldoBruto;
    }

    @Override
    public String mostrar() {
        // TODO Auto-generated method stub
        return super.mostrar() + "sueldo = " + sueldoBruto;
    }

    public void setJefe(Directivo jefe) {
        this.jefe = jefe;
    }
    
}
