package TangenOblig2;

public class GjenfangstHare extends Gjenfangst{
    private String farge;

    public GjenfangstHare(String nyraseid, String nydato, Float nyvekt, Float nylengde, String nysted, String farge) {
        super(nyraseid, nydato, nyvekt, nylengde, nysted);
        this.farge = farge;
    }

    public String getFarge() {
        return farge;
    }

    @Override
    public String toString() {
        return "GjenfangstHare" +
                ", nyfarge='" + farge + '\'' +
                " " + super.toString();
    }


}
