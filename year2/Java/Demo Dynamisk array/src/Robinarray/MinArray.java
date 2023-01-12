package Robinarray;

public class MinArray {
    //Angir initiell lengde på arrayen;
    private int lengde =2 ;
    //Lager en array vi kan putte alle slags objekter inn i:
    private Object[] tabell = new Object[lengde];
    //Em variabel som holder rede på antall objekter
    private int antall = 0;

    //Metode for å sette inn nye objekter:
    public void settInn(Object objekt){
        //Sjekker om det er plass i arrayen
        if (antall == tabell.length) utvidTabell();
        tabell[antall] = objekt;
        antall++;
    }//slutt metoden

    //Metoden kan godt være private
    private void utvidTabell(){
        //Lager først en ny tabell med dobbelt så mange plasser
        Object[] nytabell = new Object[lengde*2];
        lengde = lengde*2;
        //Kopierer alle objektene fra gammel til ny array
        for (int i = 0; i < tabell.length; i++) {
            nytabell[i] = tabell[i];

        }
        //Setter tabell til å referere til den nye tabellen:
        tabell=nytabell;

    }
}
