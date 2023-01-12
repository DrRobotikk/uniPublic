import javax.swing.*;
import java.sql.Array;

public class verdibytte {
    public static void main(String[] args) {
        String x = JOptionPane.showInputDialog("Oppgi en form for verdi");

        String y = JOptionPane.showInputDialog("Oppgi enda en verdi");

        String z = JOptionPane.showInputDialog("Gidder du og oppgi en verdi til plizz");

        String rest = "";

       System.out.println(x);
       System.out.println(y);
       System.out.println(z);

       boolean ok = true;

       while (ok){

           rest=x;
           x=z;
           z=y;
           y=rest;

           System.out.println(x);
           System.out.println(y);
           System.out.println(z);

           ok = false;



       }





    }
    
}
