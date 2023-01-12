import javax.swing.*;

public class Person {
    String navn;
    String adresse;

    public Person(String navn,String adresse){
        this.navn=navn;
        this.adresse=adresse;

    }

    public String toString(){
        return "*************" + "\n" +  "Navn: "+navn + "\n" +  "*****************";
    }
}
