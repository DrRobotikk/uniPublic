package tangen.robinbrum;

public class Kjøretøy implements Comparable<Kjøretøy>{
    private String regNr;// Tjener som unik identifikator
    private String produsent;
    private String modell;
    private int regår;

    public Kjøretøy(String regNr, String produsent, String modell, int regår) {
        this.regNr = regNr;
        this.produsent = produsent;
        this.modell = modell;
        this.regår = regår;
    }
    //Ekstra konstruktør for å lage dummy-objekt
    public Kjøretøy(String regNr){
        this.regNr = regNr;
    }


    public String getRegNr() {
        return regNr;
    }

    public void setRegNr(String regNr) {
        this.regNr = regNr; 
    }

    public String getProdusent() {
        return produsent;
    }

    public void setProdusent(String produsent) {
        this.produsent = produsent;
    }

    public String getModell() {
        return modell;
    }

    public void setModell(String modell) {
        this.modell = modell;
    }

    public int getRegår() {
        return regår;
    }

    public void setRegår(int regår) {
        this.regår = regår;
    }

    @Override
    public String toString() {
        return "Kjøretøy{" +
                "regNr='" + regNr + '\'' +
                ", produsent='" + produsent + '\'' +
                ", modell='" + modell + '\'' +
                ", regår=" + regår +
                '}';
    }


    public int compareTo(Kjøretøy denandre) {
        return this.regNr.compareTo(denandre.getRegNr());
    }


    public boolean equals(Kjøretøy denandre) {
        return this.regNr.equals(denandre.getRegNr());
    }
}
