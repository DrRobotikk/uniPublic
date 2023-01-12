package robin.tangenkjortoy;

import java.util.ArrayList;

public class Person implements Comparable<Person>{
    private String navn; //Vi later som at navn er unikt og kan brukes som identifikator
    private String adresse;
    //Refereanse til postaddressen
    Postadresse postadresse;

    //Alle kjøretøyene personen eier
    private ArrayList<Kjøretøy> kjøretøyliste = new ArrayList<>();

    public Person(String navn, String adresse, Postadresse postadresse) {
        this.navn = navn;
        this.adresse = adresse;
        this.postadresse = postadresse;
    }

    public Person(String navn) {
        this.navn = navn;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public Postadresse getPostadresse() {
        return postadresse;
    }

    public void setPostadresse(Postadresse postadresse) {
        this.postadresse = postadresse;
    }

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", postadresse=" + postadresse.toString() +
                '}';
    }

    //CompareTo and equals skal nå brukes til og samenligne Strenger
    public int compareTo(Person person) {
        //Navn er deklarert som en String:
        return this.navn.compareTo(person.getNavn());
    }

    public boolean equals(Person person) {
        return this.navn.equals(person.getNavn());
    }
}
