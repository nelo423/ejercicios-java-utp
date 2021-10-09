package co.edu.utp.misiontic2022.reto2;

public class Carro {
    //// Constantes
    private static final double PESO = 10.0;
    private static final double TAMANIO = 4.5;
    private static final double PRECIO_BASE = 1000.0;
    //Atributos
    private double peso;
    private double tamanio;
    private double precioBase;
    
    //Constructor
    public Carro(double peso, double tamanio){
        this.peso = peso;
        this.tamanio = tamanio;
        this.precioBase = PRECIO_BASE;
        
    }
    public Carro(double precioBase){
        this.peso = PESO;
        this.tamanio = TAMANIO;
        this.precioBase = precioBase;
    }
    public Carro(){
        this.peso = PESO;
        this.tamanio = TAMANIO;
        this.precioBase = PRECIO_BASE;
    }
    public double getPeso(){
        return peso;
    }

    public double getTamanio(){
        return tamanio;
    }  
    
    public double getPrecioBase(){
        return precioBase;
    }  
    public double calcularPrecio(){
        return 0.0;
    }
    
    }

    
