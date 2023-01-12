package robin.tangenkjortoy;

public class Kjøretøy implements Comparable<Kjøretøy>{
    private String regnr;
    private String modell;
    private Person eier;

    public Kjøretøy(String regnr, String modell, Person eier) {
        this.regnr = regnr;
        this.modell = modell;
        this.eier = eier;
    }

    public Kjøretøy(String regnr) {
        this.regnr = regnr;
    }

    public String getRegnr() {
        return regnr;
    }

    public void setRegnr(String regnr) {
        this.regnr = regnr;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public Person getEier() {
        return eier;
    }

    public void setEier(Person eier) {
        this.eier = eier;
    }

    @Override
    public String toString() {
        return "Kjøretøy{" +
                "regnr='" + regnr + '\'' +
                ", modell='" + modell + '\'' +
                ", eier=" + eier +
                '}';
    }

    public int compareTo(Kjøretøy kjøretøy) {
        //Regnr er deklarert som en String:
        return this.regnr.compareTo(kjøretøy.getRegnr());
    }

    public boolean equals(Kjøretøy kjøretøy) {
        return this.regnr.equals(kjøretøy.getRegnr());
    }
}
