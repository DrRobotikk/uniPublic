import javax.swing.*;
import java.util.Formatter;

public class oppgave4 {
    public static void main(String[] args) {
        double kurs =8.89;
        //Leser inn antall $:
        double usd = Double.parseDouble(JOptionPane.showInputDialog("Skriv inn antall $"));
        double nok = usd*kurs;
        // Formaterer til 2 desimaler:
        Formatter f = new Formatter();
        f.format("%.2f",nok);
        JOptionPane.showMessageDialog(null,"nok:"+f.toString());

    }
}
