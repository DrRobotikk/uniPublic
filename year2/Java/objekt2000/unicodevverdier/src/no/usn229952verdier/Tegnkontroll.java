package no.usn229952verdier;

public class Tegnkontroll {

    public String lagVerdier(char start, char slutt){
        //Vi skal bygge opp en String som skal returneres
        //Vi lager en som String:
        String uttekst = "";
        //Konverterer start og slutt til int:
        int startverdi = start; // En char er egentlig en int
        int sluttverdi = slutt;
        int verdi = startverdi;
        //Starter en løkke
        for (int i = startverdi;i<sluttverdi + 1;i++){
            uttekst+= "Tegnet " + start + " har unicode-verdien " + verdi + "\n";
            verdi++;
            start++;
        }//slutt løkke
        return uttekst;
    }
}
