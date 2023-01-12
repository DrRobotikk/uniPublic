package robin.tangenkjortoy;

public class Postadresse implements Comparable<Postadresse>{
    private int postnummer;
    private String poststed;

    public Postadresse(int postnummer, String poststed) {
        this.postnummer = postnummer;
        this.poststed = poststed;
    }

    public Postadresse(int postnummer) {
        this.postnummer = postnummer;
    }

    public int getPostnummer() {
        return postnummer;
    }

    public void setPostnummer(int postnummer) {
        this.postnummer = postnummer;
    }

    public String getPoststed() {
        return poststed;
    }

    public void setPoststed(String poststed) {
        this.poststed = poststed;
    }

    @Override
    public String toString() {
        return "Postadresse{" +
                "postnummer=" + postnummer +
                ", poststed='" + poststed + '\'' +
                '}';
    }


    public int compareTo(Postadresse postadresse) {
        //Postnr er deklarert som en integer:
        if (this.postnummer == postadresse.getPostnummer()) {
            return 0;
        } else if (this.postnummer < postadresse.getPostnummer()) {
            return -1;//Dette postnummeret kommer foran
        } else {
            return 1;
        }
    }

    public boolean equals(Postadresse postadresse) {
        if (this.postnummer == postadresse.getPostnummer()) {
            return true;
        } else {
            return false;
        }
    }
}
