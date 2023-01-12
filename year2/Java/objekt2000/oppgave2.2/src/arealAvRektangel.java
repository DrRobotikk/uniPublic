import javax.swing.*;

public class arealAvRektangel {
    public static void main(String[] args) {
        //Leser lengde og bredde på et rektangel:
        // Først lengden:
        String lestlengde = JOptionPane.showInputDialog("Skriv lengden");
        //Konverterer til doubble:
        double lengde = Double.parseDouble(lestlengde);
        // Leser bredden på en mer kompakt måte:
        double bredde =Double.parseDouble(JOptionPane.showInputDialog("Skriv bredde"));
        JOptionPane.showMessageDialog(null,"areal: " +lengde*bredde);
    }
}
