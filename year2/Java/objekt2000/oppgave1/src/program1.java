import javax.swing.*;

public class program1 {




    public static void main(String[] args) {
        String lesttall = JOptionPane.showInputDialog("Skriv inn et tall");
        int tall1 =  Integer.parseInt(lesttall);
        lesttall=JOptionPane.showInputDialog("skriv inn et nytt tall");
        int tall2 = Integer.parseInt(lesttall);
        int sum = tall1+ tall2;

        JOptionPane.showMessageDialog(null,"svaret er "+sum);

    }
}
