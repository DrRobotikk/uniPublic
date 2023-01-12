package robin.tangengeneric;

import java.util.ArrayList;

public class GeneriskStack <Type>{
    //Oppretter en ArrayList av type
    private ArrayList<Type> stakk = new ArrayList<>();

    //Metode for å returnere antall objekter i stakk
    public int getSize(){
        return stakk.size();
    }

    //Metode som tester på om stakke er tom:
    public boolean isEmpty(){
        return stakk.isEmpty();
    }

    //Metode for å sette inn et nytt objekt:
    public void push(Type objekt){
        stakk.add(objekt);
    }

    //Meotde for å ta ut et objekt fra "øverst" (sist) i stakken:
    //Metoden skal også returnere objektet:
    public Type pop(){
        //Lager en huskereferanse til det siste objektet i stakken
        Type t = stakk.get(stakk.size()-1);
        //Fjerner objektet ved å bruke en ArrayList-metoden remove:
        stakk.remove(stakk.size()-1);
        return t;
    }

    public Type peep(){
        //skal bare returnere en referanse til objektet:
        return stakk.get(stakk.size()-1);
    }

    //Metode for å returnere innholdet som en array:
    public Object[] getInnhold(){
        return stakk.toArray();
    }
}
