public class Person {
    String navn;
    String adresse;

    //konstruktør
    public Person(String navn, String adresse){
        this.navn = navn;//attributtnavnet settes til parameter
        this.adresse=adresse;
    }

    public String toString(){
        return navn + ", " + adresse;
    }
}
