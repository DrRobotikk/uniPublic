package com.gmailtangenrobin;

import java.util.Arrays;

public class MinArray {
    private int lengde = 30;
    private String[] tabell = new String[lengde];
    private int antall = 0;

    public void nyttObjekt(String element){
        if (antall == tabell.length) utvidTabell();
        tabell[antall]= element;
        antall++;

    }

    private void utvidTabell(){
        String[] nyTabell = new String[lengde*2];
        for (int i=0;i< tabell.length;i++){
            nyTabell[i] = tabell[i];
        }
        tabell = nyTabell;
    }

    public String[] hentListe(){
        return tabell;
    }

    @Override
    public String toString() {
        return "MinArray{" +
                "tabell=" + Arrays.toString(tabell) +
                '}';
    }
}
