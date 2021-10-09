package empresa;

public class Directivo extends Empleado {
    private String categoria;

    private Empleado[] subordinados;
    private Integer numSubordinados;

    public Directivo(String nombre, Integer edad, Double sueldoBruto, String categoria) {
        super(nombre, edad, sueldoBruto);
        this.categoria = categoria;
        
        subordinados = new Empleado[10];
        numSubordinados = 0;

    }

    @Override
    public String mostrar() {
        // TODO Auto-generated method stub
        return super.mostrar() + "categoria" + categoria;
    }

    public void addSuborbidado(Empleado empleado){
        subordinados[numSubordinados] = empleado;
        empleado.setJefe(this);
        numSubordinados++;

    }
    
    
}
