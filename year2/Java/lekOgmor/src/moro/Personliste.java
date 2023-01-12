package moro;

import javax.swing.*;
import java.util.ArrayList;

public class Personliste {

    public ArrayList<Personer> personer = new ArrayList<Personer>();

    public void registrerNyPerson( String navn, int alder, String adresse, String postnr, String poststed, String telefon, String epost, String kjonn) {


        Personer person = new Personer(navn, alder, adresse, postnr, poststed, telefon, epost, kjonn);

        personer.add(person);

    }

    public String visAllePersoner(){
        String ut = "";
        for (Personer person : personer){
            ut += person.getNavn() + " " + person.getAlder() + " " + person.getAdresse() + " " + person.getPostnr() + " " + person.getPoststed() + " " + person.getTelefon() + " " + person.getEpost() + " " + person.getKjonn() + "\n";


        }
        return ut;
    }

    public String hentaPerson(String navn){
        String ut = "";
        for (Personer person : personer){
            if (person.getNavn().equals(navn)){
                ut += person.getNavn() + " " + person.getAlder() + " " + person.getAdresse() + " " + person.getPostnr() + " " + person.getPoststed() + " " + person.getTelefon() + " " + person.getEpost() + " " + person.getKjonn() + "\n";

                break;
            }



            else {
                ut = "Personen finnes ikke";
            }
        }
        return ut;
    }

    public String slettPerson(String navn){
        String ut = "";
        for (Personer person : personer){
            if (person.getNavn().equals(navn)){
                personer.remove(person);
                ut = "Personen er slettet";
                break;
            }
            else {
                ut = "Personen finnes ikke";
            }
        }
        return ut;
    }
}
