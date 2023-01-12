import javax.swing.*;


public class figur {
    public static void main(String[] args) {
        int linjer = Integer.parseInt(JOptionPane.showInputDialog("Oppgi antall linjer"));

        for(int i = 0; i < linjer+1; i++) {
            String result = new String(new char[i]).replace("\0", "*");
            System.out.println(result);

            System.out.println();
        }
    }
}
