package com.gmailtangenrobin;

import java.util.ArrayList;
import java.util.List;

public class DiktKonrtoll {
    //Lager lister for ordene
    MinArray alleord =new MinArray();
    MinArray verb = new MinArray();
    MinArray substantiv = new MinArray();
    MinArray adjektiv = new MinArray();
    MinArray artikkel = new MinArray();







    //Interne lister med noen ferdige ord
    public String[] VERB ={"Kjører","går","vandrer","sover"};
    public String[] SUBSTANTIV = {"kjøleskap","menneske","røver","kanin"};
    public String[] ARTIKKEL = {"En","Ei","Et","den"};

    public String[] ADJEKTIV = {"blåe","grønne","røde","lilla"};


//Metode for å legge listene inn i de nye listene
public void leggTilIListe(){



    for (int i=0;i< VERB.length;i++){
        alleord.nyttObjekt(VERB[i]);
        verb.nyttObjekt(VERB[i]);
    }
    for (int j=0;j< SUBSTANTIV.length;j++){
        alleord.nyttObjekt(SUBSTANTIV[j]);
        substantiv.nyttObjekt(SUBSTANTIV[j]);
    }
    for (int k=0;k<ADJEKTIV.length;k++){
        alleord.nyttObjekt(ADJEKTIV[k]);
        adjektiv.nyttObjekt(ADJEKTIV[k]);
    }
    for (int l=0;l<ARTIKKEL.length;l++){
        artikkel.nyttObjekt(ARTIKKEL[l]);
    }
}


//metode for å lage enkle dikt
public String lagEnkeltDikt(){
    String[] alleordListe=alleord.hentListe();
    String dikt = "";
    for (int i = 0;i < 16;i++){
        int tilfedigOrd = (int) (Math.random()* (alleordListe.length));
        if (alleordListe[tilfedigOrd] == null){
            tilfedigOrd=(int) (Math.random()*alleordListe.length);
        }
        dikt += alleordListe[tilfedigOrd] + " ";
        if (i == 3 || i == 7 || i == 11){
            dikt+="\n";
        }

  ;



    }
    return dikt;
}
//Metode for å lage avanserte dikt
public String lagAvansertDikt(){
    String[] verbListe = verb.hentListe();
    String[] substantivListe = substantiv.hentListe();
    String[] adjektivListe = adjektiv.hentListe();
    String[] artikkelListe = artikkel.hentListe();
    String dikt = "";
    int tilfedigArtikkel = (int)(Math.random()* (artikkelListe.length));



    for (int i = 0; i<4;i++){
        int tilfeldigSubstantiv = (int)(Math.random()* (substantivListe.length));
        int tilfeldigVerb = (int)(Math.random()* (verbListe.length));
        int tilfeldigAdjektiv = (int)(Math.random()* (adjektivListe.length));

        if (artikkelListe[tilfedigArtikkel] == null) tilfedigArtikkel=(int)(Math.random()*3);
        if (adjektivListe[tilfeldigAdjektiv] == null) tilfeldigAdjektiv=(int)(Math.random()*3);
        if (substantivListe[tilfeldigSubstantiv] == null) tilfeldigSubstantiv=(int)(Math.random()*3);
        if (verbListe[tilfeldigVerb] == null) tilfeldigVerb=(int)(Math.random()*3);

        if (i == 3){
            dikt += verbListe[tilfeldigVerb] + " ";
            dikt += artikkelListe[tilfedigArtikkel] + " ";
            dikt += adjektivListe[tilfeldigAdjektiv] + " ";
            dikt += substantivListe[tilfeldigSubstantiv] + "?";
            break;


        }



        dikt += artikkelListe[tilfedigArtikkel] + " ";
        dikt += adjektivListe[tilfeldigAdjektiv] + " ";
        dikt += substantivListe[tilfeldigSubstantiv] + " ";
        dikt += verbListe[tilfeldigVerb] + " " + "\n";


    }



    return dikt;
}
//metoder for å registrere ord
public void  registrertVerb(String element){
    verb.nyttObjekt(element);
    alleord.nyttObjekt(element);

}

public void registrertSubstantiv(String elemnt){
    substantiv.nyttObjekt(elemnt);
    alleord.nyttObjekt(elemnt);
}
public void registrerAdjektiv(String element){
    adjektiv.nyttObjekt(element);
    alleord.nyttObjekt(element);
}
public void registrertArtikkel(String element){
    artikkel.nyttObjekt(element);
    alleord.nyttObjekt(element);
}
}
