package moro;

public class Personer {

private String navn;
    private int alder;
    private String adresse;
    private String postnr;
    private String poststed;
    private String telefon;
    private String epost;
    private String kjonn;

    public Personer(String navn, int alder, String adresse, String postnr, String poststed, String telefon, String epost, String kjonn) {
        this.navn = navn;
        this.alder = alder;
        this.adresse = adresse;
        this.postnr = postnr;
        this.poststed = poststed;
        this.telefon = telefon;
        this.epost = epost;
        this.kjonn = kjonn;
    }

    public String getNavn() {
        return navn;
    }

    public void setNavn(String navn) {
        this.navn = navn;
    }

    public int getAlder() {
        return alder;
    }

    public void setAlder(int alder) {
        this.alder = alder;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public String getPostnr() {
        return postnr;
    }

    public void setPostnr(String postnr) {
        this.postnr = postnr;
    }

    public String getPoststed() {
        return poststed;
    }

    public void setPoststed(String poststed) {
        this.poststed = poststed;
    }

    public String getTelefon() {
        return telefon;
    }

    public void setTelefon(String telefon) {
        this.telefon = telefon;
    }

    public String getEpost() {
        return epost;
    }

    public void setEpost(String epost) {
        this.epost = epost;
    }

    public String getKjonn() {
        return kjonn;
    }

    public void setKjonn(String kjonn) {
        this.kjonn = kjonn;
    }

    @Override
    public String toString() {
        return "Personer{" +
                "navn='" + navn + '\'' +
                ", alder=" + alder +
                ", adresse='" + adresse + '\'' +
                ", postnr='" +

}
