package TangenOblig2;

import java.util.ArrayList;
import java.util.Date;

public class Dyr implements Comparable<Dyr> {
    private String raseid;
    private String kjonn;
    private Float lengde;
    private Float vekt;
    private String sted;
    private String dato;



    public Dyr(String raseid, String kjonn, Float lengde, Float vekt, String sted, String dato) {
        this.raseid = raseid;
        this.kjonn = kjonn;
        this.lengde = lengde;
        this.vekt = vekt;
        this.sted = sted;
        this.dato = dato;
    }

    public String getRaseid() {
        return raseid;
    }

    public String getKjonn() {
        return kjonn;
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
        return "{" +
                "raseid='" + raseid + '\'' +
                ", kjonn='" + kjonn + '\'' +
                ", lengde=" + lengde +
                ", vekt=" + vekt +
                ", sted='" + sted + '\'' +
                ", dato='" + dato + '\'' +
                '}';
    }

    @Override
    public int compareTo(Dyr o) {return this.raseid.compareTo(o.getRaseid());}

    public boolean equals(Dyr denAndre) {return this.raseid.equals(denAndre.getRaseid());}
}
