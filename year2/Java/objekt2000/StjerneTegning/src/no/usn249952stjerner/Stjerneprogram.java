package no.usn249952stjerner;

public class Stjerneprogram {
    public static void main(String[] args) {
        //Lager et objekt av klassen Grensesnitt:
        Grensesnitt grensesnitt = new Grensesnitt();
        //Overlater programkontrollen til grensesnitt
        grensesnitt.meny();
    }
}
