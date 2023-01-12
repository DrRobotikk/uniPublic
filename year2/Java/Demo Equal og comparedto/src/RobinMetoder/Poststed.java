package RobinMetoder;

//Klassen Poststed skal implementere interfacest Comparable
public class Poststed implements Comparable<Poststed> {
    private int postnr;
    private String stedsnavn;

    public Poststed(int post, String stedsnavn) {
        this.postnr = post;
        this.stedsnavn = stedsnavn;
    }

    public int getPostnr() {
        return postnr;
    }

    public void setPostnr(int postnr) {
        this.postnr = postnr;
    }

    public String getStedsnavn() {
        return stedsnavn;
    }

    public void setStedsnavn(String stedsnavn) {
        this.stedsnavn = stedsnavn;
    }
    //Overstyrer metoden equals som er definer i klassen Object
    public boolean equals(Poststed denAndre){
        return this.postnr == denAndre.postnr;
    }

    //Implementerer metoden compareTO fra interfacet Comparable
    public int compareTo(Poststed denAndre){
        //returnerer 0 hvis postnr er like
        if (this.postnr == denAndre.getPostnr()) return 0;

        //Hvis dette objectes postnr er mindre enn detAndre objektet postnr
        //returneres et negativt tall
        else if (this.postnr < denAndre.getPostnr()) return -1;

        //Ellers mp dette postnummret være større ennn det andre
        // og da returneres et positivt tall
        else return 1;
    }

    @Override
    public String toString() {
        return "Poststed{" +
                "postnr=" + postnr +
                ", stedsnavn='" + stedsnavn + '\'' +
                '}';
    }
}
