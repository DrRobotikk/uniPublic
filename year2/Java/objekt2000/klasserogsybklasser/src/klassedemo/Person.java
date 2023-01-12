package klassedemo;

public class Person {
    private String navn;
    private String adresse;
    private int fodselsaar;

    public Person(String navn, String adresse, int fodselsaar) {
        super();
        this.navn = navn;
        this.adresse = adresse;
        this.fodselsaar = fodselsaar;
    }

    public String getNavn() {
        return navn;
    }

    public String getAdresse() {
        return adresse;
    }

    public int getFodselsaar() {
        return fodselsaar;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public void setFodselsaar(int fodselsaar) {
        this.fodselsaar = fodselsaar;
    }

    @Override
    public String toString() {
        return "Person{" +
                "navn='" + navn + '\'' +
                ", adresse='" + adresse + '\'' +
                ", fodselsaar=" + fodselsaar +
                '}';
    }
}

