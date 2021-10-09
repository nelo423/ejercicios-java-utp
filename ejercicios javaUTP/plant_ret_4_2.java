//Librerías
import java.util.ArrayList;
import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

//Vista
public class VistaRequerimientosReto4 {

    public static ControladorRequerimientosReto4 controlador = new ControladorRequerimientosReto4();

    public static void requerimiento1() {
        try{
            ArrayList<ProyectoCiudad> rankingProyectosCiudad = controlador.consultarProyectoCiudad();

            System.out.println("-----Proyecto Ciudad-------");
            System.out.println("Constructora Fecha_Inicio Clasificación");
            for(ProyectoCiudad proyectoCiudad: rankingProyectosCiudad){
                System.out.printf("%s %s %s %n", proyectoCiudad.getConstructora(), proyectoCiudad.getFechaInicio(), proyectoCiudad.getClasificacion());
            }
        }catch(SQLException e){
            System.out.println(e);
        }
    }

    public static void requerimiento3() {
        try{
            ArrayList<SumaProveedor> rankingSumaProveedor = controlador.consultarSumaProveedor();

            System.out.println("-----Suma Cantidades-------");
            System.out.println("Suma Cantidades");
            for(SumaProveedor sumaProveedor: rankingSumaProveedor){
                System.out.printf("%s %n" ,sumaProveedor.getCantidad());
            }
        }catch(SQLException e){
            System.out.println(e);
        }

    }

    public static void requerimiento4() {
        try{
            ArrayList<LiderCiudad> rankingLiderCiudad = controlador.consultarLiderCiudad();

            System.out.println("-----Líder Ciudad-------");
            System.out.println("Nombre Líder");
            for(LiderCiudad liderCiudad: rankingLiderCiudad){
                System.out.printf("%s %n", liderCiudad.getNombreLider());
            }
        }catch(SQLException e){
            System.out.println(e);
        }
    }
}
//Controlador
public class ControladorRequerimientosReto4 {

    private ProyectoCiudadDao proyectoCiudadDao;
    private LiderCiudadDao liderCiudadDao;
    private SumaProveedorDao sumaProveedorDao;

    public ControladorRequerimientosReto4(){
        this.proyectoCiudadDao = new ProyectoCiudadDao();
        this.liderCiudadDao = new LiderCiudadDao();
        this.sumaProveedorDao = new SumaProveedorDao();
    }

    public ArrayList<ProyectoCiudad> consultarProyectoCiudad() throws SQLException {
        return this.proyectoCiudadDao.rankingProyectosCiudad();
    }

    public ArrayList<LiderCiudad> consultarLiderCiudad() throws SQLException {
        return this.liderCiudadDao.rankingLiderCiudad();
    }

    public ArrayList<SumaProveedor> consultarSumaProveedor() throws SQLException {
        return this.sumaProveedorDao.rankingSumaProveedor();
    }
}

//DAO´s

public class ProyectoCiudadDao {

    public ArrayList<ProyectoCiudad> rankingProyectosCiudad() throws SQLException {

        ArrayList<ProyectoCiudad> respuesta = new ArrayList<ProyectoCiudad>();
        Connection conexion = JDBCUtilities.getConnection();

        try {
             String consulta = "SELECT Constructora, " 
                             + "Fecha_Inicio, " 
                             + "Clasificacion "
                             + "FROM Proyecto "
                             + "WHERE Ciudad = 'Armenia'";

            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            while(resultSet.next()){
                ProyectoCiudad proyectoCiudad = new ProyectoCiudad();
                proyectoCiudad.setConstructora(resultSet.getString("Constructora"));
                proyectoCiudad.setFechaInicio(resultSet.getString("Fecha_Inicio"));
                proyectoCiudad.setClasificacion(resultSet.getString("Clasificacion"));

                respuesta.add(proyectoCiudad);
            }

            resultSet.close();
            statement.close();

        }catch(SQLException e){
            System.err.println("Error consultando Proyecto Ciudad!!" + e);
            
        }finally{
            if(conexion != null){
                conexion.close();
            }
        }
            return respuesta;
    }
}

public class SumaProveedorDao {

    public ArrayList<SumaProveedor> rankingSumaProveedor() throws SQLException {

        ArrayList<SumaProveedor> respuesta = new ArrayList<SumaProveedor>();
        Connection conexion = JDBCUtilities.getConnection();

        try {
            String consulta = "SELECT SUM(Cantidad) AS Cantidad "
                            + "FROM Compra " 
                            + "WHERE Proveedor ='Cementos El Dorado';";

            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            while(resultSet.next()){
                SumaProveedor sumaProveedor = new SumaProveedor();
                sumaProveedor.setCantidad(resultSet.getString("Cantidad"));

                respuesta.add(sumaProveedor);
            }

            resultSet.close();
            statement.close();
            
        }catch(SQLException e){
            System.err.println("Error en la consulta: " + e);

        }finally{
            if(conexion != null){
                conexion.close();
            }
        }

        return respuesta;
    }

}

public class LiderCiudadDao {

    public ArrayList<LiderCiudad> rankingLiderCiudad() throws SQLException {
    
        ArrayList<LiderCiudad> respuesta = new ArrayList<LiderCiudad>();
        Connection conexion = JDBCUtilities.getConnection();

        try {
            String consulta = "SELECT l.Nombre || ' ' "
                            + " ||l.Primer_Apellido || ' ' "
                            + " ||l.Segundo_Apellido AS 'Nombre Lider' "
                            + "FROM Lider l "
                            + "WHERE l.Ciudad_Residencia = 'Paris'";

            PreparedStatement statement = conexion.prepareStatement(consulta);
            ResultSet resultSet = statement.executeQuery();

            while(resultSet.next()){
                LiderCiudad liderCiudad = new LiderCiudad();
                liderCiudad.setNombreLider(resultSet.getString("Nombre Lider"));

                respuesta.add(liderCiudad);
            }

            resultSet.close();
            statement.close();

        }catch(SQLException e){
            System.err.println("Error consultando Proyecto Ciudad!!" + e);
            
        }finally{
            if(conexion != null){
                conexion.close();
            }
        }
            return respuesta;
    }
}

//VO´s

public class ProyectoCiudad {

    private String constructora;
    private String fechaInicio;    
    private String clasificacion;

    public ProyectoCiudad(String constructora, String fechaInicio, String clasificacion) {
        this.constructora = constructora;
        this.fechaInicio = fechaInicio;
        this.clasificacion = clasificacion;
    }

    public ProyectoCiudad(){
    }

    public String getConstructora() {
        return constructora;
    }
    
    public void setConstructora(String constructora) {
        this.constructora = constructora;
    }
    
    public String getFechaInicio() {
        return fechaInicio;
    }
    
    public void setFechaInicio(String fechaInicial) {
        this.fechaInicio = fechaInicial;
    }
    
    public String getClasificacion() {
        return clasificacion;
    }
    
    public void setClasificacion(String clasificacion) {
        this.clasificacion = clasificacion;
    }
}


public class SumaProveedor {

    private String cantidad;

    public SumaProveedor(){
    }

    public SumaProveedor(String cantidad) {
        this.cantidad = cantidad;
    }

    public String getCantidad() {
        return cantidad;
    }

    public void setCantidad(String cantidad) {
        this.cantidad = cantidad;
    }

   
}


public class LiderCiudad {

    private String nombreLider;

    public LiderCiudad() {
    }

    public LiderCiudad(String nombreLider) {
        this.nombreLider = nombreLider;
    }

    public String getNombreLider() {
        return nombreLider;
    }

    public void setNombreLider(String nombreLider) {
        this.nombreLider = nombreLider;
    }

}

//Utilities

public class JDBCUtilities {

    // Atributos de clase para gestión de conexión con la base de datos
    private static final String UBICACION_BD = "ProyectosConstruccion.db";
    
    public static Connection getConnection() throws SQLException {
        String url = "jdbc:sqlite:" + UBICACION_BD;
        return DriverManager.getConnection(url);
    }

    public static boolean estaVacia() {
        File archivo = new File(JDBCUtilities.UBICACION_BD);
        return archivo.length() == 0;
    }

}

