package com.gmailtangenrobin;

import javax.swing.*;

public class Grensesnitt {
    DiktKonrtoll kontroll = new DiktKonrtoll();

    private final String[] HOVEDMENY = {"Enkelt dikt","avansert dikt","Legg til ord","Avslutt"};
    private final String[] ENKELTMENY = {"Enkelt dikt","tilbake"};
    private final String[] AVANSERTMENY = {"Avansert dikt","tilbake"};
    private final String[] REGISTRERMENY = {"Artikkel","Verb","Substantiv","Adjektiv","Tilbake"};



    public int lesValgHoved(){
        int valg = JOptionPane.showOptionDialog(
                null,
                "Ta et valg",//Ledetekst
                "Diktgenerator",//Tittel på vinduet
                JOptionPane.DEFAULT_OPTION,//Klassekonstant
                JOptionPane.PLAIN_MESSAGE,//Klassekonstant
                null,
                HOVEDMENY,//Valgene
                HOVEDMENY[0]);//Default option
        return valg;

    }
    public int lesValgEnekltMeny(){
        int valg = JOptionPane.showOptionDialog(
                null,
                "Ta et valg",//Ledetekst
                "Diktgenerator",//Tittel på vinduet
                JOptionPane.DEFAULT_OPTION,//Klassekonstant
                JOptionPane.PLAIN_MESSAGE,//Klassekonstant
                null,
                ENKELTMENY,//Valgene
                ENKELTMENY[0]);//Default option
        return valg;

    }
    public int lesValgAvansertMeny(){
        int valg = JOptionPane.showOptionDialog(
                null,
                "Ta et valg",//Ledetekst
                "Diktgenerator",//Tittel på vinduet
                JOptionPane.DEFAULT_OPTION,//Klassekonstant
                JOptionPane.PLAIN_MESSAGE,//Klassekonstant
                null,
                AVANSERTMENY,//Valgene
                AVANSERTMENY[0]);//Default option
        return valg;

    }

    public int lesValgRegistrer(){
        int valg = JOptionPane.showOptionDialog(
                null,
                "Ta et valg",//Ledetekst
                "Diktgenerator",//Tittel på vinduet
                JOptionPane.DEFAULT_OPTION,//Klassekonstant
                JOptionPane.PLAIN_MESSAGE,//Klassekonstant
                null,
                REGISTRERMENY,//Valgene
                REGISTRERMENY[0]);//Default option
        return valg;

    }


    public void meny (){
        kontroll.leggTilIListe();
        boolean fortsette=true;
        while (fortsette){
            int valg=lesValgHoved();

            switch (valg){
                case 0: enkeltMeny();
                break;
                case 1: avansertMeny();
                break;
                case 2: registrereMeny();
                break;
                default: fortsette = false;

            }

        }



    }

    public void enkeltMeny (){
        boolean fortsette=true;
        while (fortsette){
            int valg=lesValgEnekltMeny();

            switch (valg){
                case 0: lagEnkeltDikt();
                    break;
                default: fortsette = false;

            }

        }



    }
    public void avansertMeny (){
        boolean fortsette=true;
        while (fortsette){
            int valg=lesValgAvansertMeny();

            switch (valg){
                case 0: lagAvansertDikt();
                    break;
                default: fortsette = false;

            }

        }



    }

    public void registrereMeny (){
        boolean fortsette=true;
        while (fortsette){
            int valg=lesValgRegistrer();

            switch (valg){
                case 0: registrerArtikkel();
                    break;
                case 1: registrerVerb();
                    break;
                case 2: registrerSubstantiv();
                    break;
                case 3: registrerAdjektiv();
                    break;
                default: fortsette = false;

            }

        }



    }




    public void lagEnkeltDikt(){
        String dikt = kontroll.lagEnkeltDikt();
        JOptionPane.showMessageDialog(null,dikt);

    }

    public void lagAvansertDikt(){
        String dikt = kontroll.lagAvansertDikt();
        JOptionPane.showMessageDialog(null,dikt);
    }

    public void registrerVerb(){
        String nyttVerb = JOptionPane.showInputDialog("Skriv et verb");
        kontroll.registrertVerb(nyttVerb);


    }

    public void registrerAdjektiv(){
        String nyttAdjektiv = JOptionPane.showInputDialog("Skriv et adjektiv");
        kontroll.registrerAdjektiv(nyttAdjektiv);

    }

    public void registrerSubstantiv(){
        String nyttSubstantiv = JOptionPane.showInputDialog("Skriv et substantiv");
        kontroll.registrertSubstantiv(nyttSubstantiv);

    }

    public void registrerArtikkel(){
        String nyArtikkel = JOptionPane.showInputDialog("Skriv inn en artikkel");
        kontroll.registrertArtikkel(nyArtikkel);

    }


}
