import javax.swing.*;

public class Vista extends JFrame {
    
    public JLabel etiquetaNum= new JLabel("Valor 1");
    public JTextField txtCampo1 = new JTextField(5);
    public JLabel etiquetaSumar = new JLabel("  +  ");
    public JLabel etiquetaNum2= new JLabel("Valor 2");
    public JTextField txtCampo2 = new JTextField(5);
    public JButton btnSumar = new JButton("Sumar");
    public JLabel etiquetaNum3= new JLabel("Resultado");
    public JTextField txtRespuesta = new JTextField(5);
    
    public Vista(){
        
        JPanel panelCalculadora = new JPanel();
       
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(600,200);

        panelCalculadora.add(etiquetaNum);
        panelCalculadora.add(txtCampo1);
        panelCalculadora.add(etiquetaSumar);
        panelCalculadora.add(etiquetaNum2);
        panelCalculadora.add(txtCampo2);
        panelCalculadora.add(btnSumar);
        panelCalculadora.add(etiquetaNum3);
        panelCalculadora.add(txtRespuesta);

        this.add(panelCalculadora);
    }

    public int getTxtCampo1(){
        return Integer.parseInt(txtCampo1.getText());
    }

    public int getTxtCampo2(){
        return Integer.parseInt(txtCampo2.getText());
    }

    public int getTxtRespuesta(){
        return Integer.parseInt(txtRespuesta.getText());
    }

    public void setTxtRespuesta(int n){
        txtRespuesta.setText(Integer.toString(n));
    }

    public void mensajeError(String msg){
        JOptionPane.showMessageDialog(this, msg);
    }

}