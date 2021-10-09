import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class App {
    public static void main(String[] args) throws Exception {
        
        Connection connection;
        
        try {
            //Conexión a la base de datos "hr.db"
            connection = DriverManager.getConnection("jdbc:sqlite:hr.db");
            if(connection != null){
                System.out.println("Conexión exitosa");
            }

            //Creación del objeto "statement" para ejecutar las consultas
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(30);  // set time out to 30 sec.

            ResultSet rs = statement.executeQuery("select * from employees");
            while(rs.next())
            {
                // read the result set
                
                System.out.println(("id = " + rs.getInt("employee_id")) + (" apellido = " + rs.getString("last_name"))+ ("id = " + rs.getInt("employee_id")) + (" nombre = " + rs.getString("first_name")))  ;
                System.out.println("___________________________________________________________");
                
                //System.out.println("id = " + rs.getInt("employee_id"));
                //System.out.println("apellido = " + rs.getString("last_name"));
                //System.out.println("nombre = " + rs.getString("first_name"));
            }

            //--------------

            System.out.println("*----------------------------------------------------------*");
            
            statement.executeUpdate("drop table if exists misiontic");
            statement.executeUpdate("create table misiontic (id integer, name string)");
            statement.executeUpdate("insert into misiontic values(1, 'Ciclo1')");
            statement.executeUpdate("insert into misiontic values(2, 'Ciclo2')");

            statement.executeUpdate("DELETE FROM persona WHERE cedula = 2");
            statement.executeUpdate("UPDATE persona SET nombre = 'Julian Cardona' WHERE cedula = 1");
            
            PreparedStatement ps = connection.prepareStatement("insert into misiontic values(?, ?)");
            ps.setInt(1, 3);
            ps.setString(2, "Ciclo3");
            ps.executeUpdate();

            ResultSet consulta = statement.executeQuery("SELECT * FROM misiontic");
            while(consulta.next())

            statement.executeUpdate("select * from misiontic");


            {
                // read the result set
                
                System.out.println(("name = " + consulta.getString("name")) +("id = " + consulta.getInt("id")) );
                //System.out.println("name = " + consulta.getString("name"));
                //System.out.println("id = " + consulta.getInt("id"));
            }




        }
        catch (Exception e) {
                //TODO: handle exception
                System.err.println(e.getClass().getName()+ ":"+e.getMessage());
                System.out.println("Error en la conexión");
            }
    }

}


//var f = new File("sub\\prueba.txt");  preguntasr sobre 'var'