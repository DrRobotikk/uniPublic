package no.usn229952verdier;

import javax.swing.*;

public class VerdiProgram {
    public static void main(String[] args) {
        //Oppretter et objekt av klassen tegnkontroll

        Tegnkontroll kontroll = new Tegnkontroll();
        //Leser første tegn
        String lestTegn = JOptionPane.showInputDialog("Skriv første tegn: ");
        //I en String ligger teksten som en String[]
        //Vi henter ut det første tegnet i teksten :
        char start = lestTegn.charAt(0);
        //Leser siste tegn:
        lestTegn = JOptionPane.showInputDialog("Skriv siste tegn: ");
        char slutt=lestTegn.charAt(0);
        //Kaller metoden lagVerdier i Tegnkontroll:
        String uttekst = kontroll.lagVerdier(start,slutt);
        JOptionPane.showMessageDialog(null,uttekst);
    }
}
