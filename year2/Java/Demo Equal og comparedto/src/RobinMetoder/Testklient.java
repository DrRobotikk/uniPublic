package RobinMetoder;

import java.util.Arrays;

public class Testklient {
    public static void main(String[] args) {
        //Oppretter en array for poststeder:
        Poststed[] poststeder = new Poststed[3];

        poststeder[0] = new Poststed(3518,"Hønefoss");
        poststeder[1] = new Poststed(3000,"Drammen");
        poststeder[2] = new Poststed(3511,"Hønefoss");


        //Skriver ut den usorterte arrayen
        for (int i = 0; i < poststeder.length; i++) {
            System.out.println(poststeder[i].toString());

        }
        //Sorterer poststedene
        Arrays.sort(poststeder);
        System.out.println();
        System.out.println("Sorterte");

        for (int i= 0; i < poststeder.length ; i++) {
            System.out.println(poststeder[i].toString());



        }

        //Vi skal bruke binærsøk
        //Vi søker først etter postnr 3000, som vi vet finnes
        Poststed sokeobjekt =new Poststed(3000,null);
        //binarySerch gir oss indeksen til objektet hvis det finnes
        int indeks = Arrays.binarySearch(poststeder,sokeobjekt);
        System.out.println("Søker etter postnr 3000");
        if (indeks >=0){
            System.out.println("indeks: "+ indeks);
            System.out.println(poststeder[indeks].toString());
        }
        else System.out.println("Postnummeret finnes ikke");
        //Lager et søkeobjekt med et postnummer vi vet ikke finnes
        sokeobjekt = new Poststed(4000,null);
         indeks = Arrays.binarySearch(poststeder,sokeobjekt);
        System.out.println("Søker etter postnr 4000");
        if (indeks >=0){
            System.out.println("indeks: "+ indeks);
            System.out.println(poststeder[indeks].toString());
        }
        else System.out.println("Postnummeret finnes ikke");

    }

}
