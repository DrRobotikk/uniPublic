package robin.tangenkjortoy;

import java.util.ArrayList;
import java.util.Collections;

public class Kontroll {
    //Vi trenger en arraylist for hver type objekt:

    private ArrayList<Person> personer = new ArrayList<>();
    private ArrayList<Postadresse> postadresser = new ArrayList<>();
    private ArrayList<Kjøretøy> kjøretøy = new ArrayList<>();

    //Metoder for å opperere på datastrukturene

    public void nyPerson(Person person) {
        personer.add(person);
    }

    public void nyttKjøretøy(Kjøretøy k) {
        this.kjøretøy.add(k);
    }

    public void nyPostadresse(int postnr, String poststed) {
        postadresser.add(new Postadresse(postnr, poststed));
    }

    public ArrayList<Person> getPersoner() {
        return personer;
    }

    public ArrayList<Postadresse> getPostadresser() {
        return postadresser;
    }

    public ArrayList<Kjøretøy> getKjøretøy() {
        return kjøretøy;
    }


    public Person finnperson(String navn){
        //bruker binary search
        Collections.sort(personer);
        Person dymmyperson = new Person(navn);
        int index = Collections.binarySearch(personer, dymmyperson);
        if(index >= 0){
            return personer.get(index);
        }
        return null;

    }

    public Kjøretøy finnkjøretøy(String regnr){
        //bruker binary search
        Collections.sort(kjøretøy);
        Kjøretøy dymmykjøretøy = new Kjøretøy(regnr);
        int index = Collections.binarySearch(kjøretøy, dymmykjøretøy);
        if(index >= 0){
            return kjøretøy.get(index);
        }
        return null;

    }

    public Postadresse finnpostadresse(int postnr){
        //bruker binary search
        Collections.sort(postadresser);
        Postadresse dymmypostadresse = new Postadresse(postnr);
        int index = Collections.binarySearch(postadresser, dymmypostadresse);
        if(index >= 0){
            return postadresser.get(index);
        }
        return null;

    }
}
