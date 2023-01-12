package tangen.robinbrum;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class kontroll {
    //En kontrollklasse skal inneholde de nødvendige datastrukturene
    //Objketer av subklassen til kjøretøy er også kjøretøy:
    private ArrayList<Kjøretøy> kjøretøyliste = new ArrayList<>();

    //Forutsetter at objekt av riktig subklasse oppretttes av grensesnittet
    public void nyttKjøretøy(Kjøretøy Kjøretøy){
        kjøretøyliste.add(Kjøretøy);
    }

    public Kjøretøy finnKjøretøy(String regNr){
        //Vi må være sikre på at kjøretøyliste er sortert
        Collections.sort(kjøretøyliste);
        //For å kunne bruke binærsøk lager vi et dummy-objekt
        //med det regNr vi søker etter
        //Kjøretøy dummy = new Kjøretøy(regNr, null, null, 0);
        //Bruker i stedet den ekstra konstruktøren
        Kjøretøy dummy = new Kjøretøy(regNr);
        //Bruker binærsøk,som returnerer indeksen til objektet i kjøretøyliste:
        //Hvis den ikke finner objektet returneres negativ verdi
        int indeks = Collections.binarySearch(kjøretøyliste, dummy);
        if (indeks > -1) {
            return kjøretøyliste.get(indeks);
        } else {
            return null;
        }

    }
    public ArrayList<Kjøretøy> getKjøretøyliste() {
        return kjøretøyliste;
    }
}
