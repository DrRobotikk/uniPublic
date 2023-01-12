package TangenOblig2;

public class Gjenfangst implements Comparable<Gjenfangst>{
    private String raseid;
    private Float lengde;
    private Float vekt;
    private String sted;
    private String dato;

    public Gjenfangst(String nyraseid,String nydato,Float nyvekt,  Float nylengde,  String nysted ) {
        this.raseid = nyraseid;
        this.lengde = nylengde;
        this.vekt = nyvekt;
        this.sted = nysted;
        this.dato = nydato;
    }

    public String getRaseid() {
        return raseid;
    }



    public Float getLengde() {
        return lengde;
    }

    public Float getVekt() {
        return vekt;
    }

    public String getSted() {
        return sted;
    }

    public String getDato() {
        return dato;
    }

    @Override
    public String toString() {
        return "Gjenfangst" +
                ", nylengde=" + lengde +
                ", nyvekt=" + vekt +
                ", nysted='" + sted + '\'' +
                ", nydato='" + dato + '\'';
    }

    @Override
    public int compareTo(Gjenfangst o) {return this.raseid.compareTo(o.getRaseid());}

  public boolean equals(Gjenfangst denAndre) {return this.raseid.equals(denAndre.getRaseid());}

}
