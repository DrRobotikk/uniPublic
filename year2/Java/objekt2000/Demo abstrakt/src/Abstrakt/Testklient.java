package Abstrakt;

public class Testklient {
    public static void main(String[] args) {
        //Lager tre objekter
        Sirkel sirkel = new Sirkel(10);
        Trekant trekant = new Trekant(5, 6);
        Kvadrat kvadrat = new Kvadrat(4);

        System.out.println("Arealet av sirkelen er "+sirkel.beregnAreal());
        System.out.println("Arealet av trekanten er "+trekant.beregnAreal());
        System.out.println("Arealet av kvadratet er "+kvadrat.beregnAreal());

    }
}
