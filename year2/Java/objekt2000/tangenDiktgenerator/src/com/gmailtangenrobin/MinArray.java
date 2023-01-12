package com.gmailtangenrobin;

import java.util.Arrays;


//Lager en klasse som heter MinArray
public class MinArray {


    public int lengde = 4;
    private String[] tabell = new String[lengde];
    private int antall = 0;

    //Lager en metode som heter nyttObjekt
    public void nyttObjekt(String element){
        if (antall == tabell.length) utvidTabell();
        tabell[antall]= element;
        antall++;

    }

    private void utvidTabell(){
        String[] nyTabell = new String[lengde+1];
        lengde= nyTabell.length;
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
