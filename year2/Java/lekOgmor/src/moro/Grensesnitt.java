package moro;

import javax.swing.*;

public class Grensesnitt {

    Personliste personliste = new Personliste();

    String[] HOVEDMENY = {"1. Registrer ny person", "2. Søk etter person", "3. Slett person", "4. Endre person", "5. Vis alle personer", "6. Avslutt"};


    public int lesvalg(){
        int valg = JOptionPane.showOptionDialog(null, "Hva ønsker du å gjøre?", "Hovedmeny", JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, HOVEDMENY, HOVEDMENY[0]);
        return valg;
    }

    public void hovedmeny(){
        boolean fortsett = true;
        while (fortsett){
            int valg = lesvalg();
            switch (valg){
                case 0:
                    registrerNyPerson();
                    break;
                case 1: hentaPerson();
                    break;
                case 2:System.out.println("Slett person");
                    break;
                case 3:System.out.println("Endre person");
                    break;
                case 4: visAllePersoner();
                    break;
                default:
                    fortsett = false;
                    break;
            }




    }








    }

    public void registrerNyPerson(){
        String navn = JOptionPane.showInputDialog("Skriv inn navn");
        int alder = Integer.parseInt(JOptionPane.showInputDialog("Skriv inn alder"));
        String adresse = JOptionPane.showInputDialog("Skriv inn adresse");
        String postnr = JOptionPane.showInputDialog("Skriv inn postnummer");
        String poststed = JOptionPane.showInputDialog("Skriv inn poststed");
        String telefon = JOptionPane.showInputDialog("Skriv inn telefonnummer");
        String epost = JOptionPane.showInputDialog("Skriv inn epost");
        String kjonn = JOptionPane.showInputDialog("Skriv inn kjønn");

        personliste.registrerNyPerson(navn, alder, adresse, postnr, poststed, telefon, epost, kjonn);
    }
    public void visAllePersoner(){
        String ut = personliste.visAllePersoner();
        JOptionPane.showMessageDialog(null, ut);
    }

    public void hentaPerson(){
        String navn = JOptionPane.showInputDialog("Skriv inn navn");
        String ut = personliste.hentaPerson(navn);
        JOptionPane.showMessageDialog(null, ut);
    }


}
