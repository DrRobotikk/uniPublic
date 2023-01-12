import javax.swing.*;

public class gange {
    public static void main(String[] args) {
        int tall1 = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn første delen "));
        int tall2 = Integer.parseInt(JOptionPane.showInputDialog("Oppgi andre delen"));

        for (int teller1=tall1;tall1<tall2+1;teller1++) {
            System.out.println(tall1 +"-gangen");

            for (int i = 1; i < 11; i++) {
                int sum = tall1 * i;
                System.out.println(tall1+"x"+i+"="+sum);

            }
        tall1++;
        }


    }

}
