import javax.swing.*;
import java.util.Formatter;

public class arealAvSirkel {
    public static void main(String[] args) {
        //Leser radius for en sirkel:
        String lestRadius = JOptionPane.showInputDialog("Skriv sirkelens radius");
        double radius = Double.parseDouble(lestRadius);
        //Arealet av en sirkel er pi*radius'radius:
        double areal = Math.PI*radius*radius;
        //Formaterer arealet til å ha 1 desimal:
        Formatter f = new Formatter();
        f.format("%.0f",areal);

        JOptionPane.showMessageDialog(null, "arealet er: "+ f.toString());
    }
}
