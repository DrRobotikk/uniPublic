package no.usn249952stjerner;

public class TegneKontroll {

    public String tegnTrekant(int antall){
        //Lager en tom String:
        String tegning = "";
        int antallStjerner = 1;
        //løkke for å lage trekantens linjer:
        //ytre løkke som tegner linger:
        for (int i = 0;i<antall;i++){
            //Øker antall linjer
            antallStjerner++;
            //indre løkke som skriver stjerner:
            for (int j = 1; j<antallStjerner;j++){
                tegning+='*';
            }// slutt indre
            //Når vi er ferdig med en linje, legger vi til et linjeskift
            tegning+='\n';
        }//slutt ytre
        //returenerer tegningen
        return tegning;
    }

    public String tengPyramide(int antall){
        String tegning ="";
        //Vi må finne ut hvor vi skal begynne å skrive stjerne:
        //Ytre løkke
        for (int i = 1;i<antall*2;i+=2){
            //Midtre løkke bestemmer hvor vi skal begynne å skrive *:
            for (int j = 0;j<(antall - i/2);j+=2){
                //Skriver mellomrom:
                tegning+=" ";
            }//slutt midtre løkke
            //Ny indre løkke for å skrive stjerner:
            for (int k = 0;k< i;k++){
                tegning+='*';
            }
            //leggger til linjeskift
            tegning+='\n';
        }
        return tegning;
    }
}
