package no.usn249952stjerner;

import javax.swing.*;

public class Grensesnitt {
    TegneKontroll kontroll = new TegneKontroll();
    private final String[] ALTERNATIVER ={"Trekant","Pyramide","Avslutt"};

    public int lesValg(){
        //Denne metoden setter opp menyen, leser valget og returnerer dette:
        //Vi bruker JoptionPane-metoden showOptionDialog som returnerer en int:
        int valg = JOptionPane.showOptionDialog(
                null,
                "Gjør et valg:",//Ledetekst
                "Tegneprogramm",//Tittel på menyen
                JOptionPane.DEFAULT_OPTION,// klassekonstant
                JOptionPane.PLAIN_MESSAGE,// klassekonstant
                null,//Lar stå
                ALTERNATIVER,//Valgene
                ALTERNATIVER[0]);//Default valg

        return valg; //Posiosjone i ALTERNATIVER
    }

    public void meny(){
        //Bruker en løkke styrt av en boolean:
        boolean frotsett = true;
        while(frotsett){
            //Setter opp menyen
            int valg = lesValg();
            //Bruker en case-blokk for å behandle valget
            switch (valg){
                case 0: tegnTrekant();
                break;
                case 1: tegnPyramide();
                break;
                default: frotsett=false;

            }
        }

    }

    public void tegnTrekant(){
        //Ber brukeren skrive antall linjer:
        int antall=Integer.parseInt(JOptionPane.showInputDialog("Skriv antall linjer: "));
        //Kaller metoden tegnTrekant i TegneKontroll:
        String tegning = kontroll.tegnTrekant(antall);
        JOptionPane.showMessageDialog(null,tegning);

    }

    public void tegnPyramide(){
        //Ber brukeren skrive antall linjer:
        int antall=Integer.parseInt(JOptionPane.showInputDialog("Skriv antall linjer: "));
        //Kaller metoden tegnTrekant i TegneKontroll:
        String tegning = kontroll.tengPyramide(antall);
        JOptionPane.showMessageDialog(null,tegning);

    }
}
