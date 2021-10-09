package empresa;

public abstract class Persona {
    
    private String nombre;
    private Integer edad;

    public Persona(String nombre, Integer edad){
        this.nombre = nombre;
        this.edad = edad;

    }

    public String mostrar(){
          return String.format("nombre=%s,edad=%d",nombre,edad);

          //"nombre =" "+nombre+ edad=0...";"
          //f"nombre ={nombre} edad = {edad}"; NO EXISTE EN JAVA
          //"nombre = {} edad = {}".format(nombre, edad) NO EXISTE

    }

}
