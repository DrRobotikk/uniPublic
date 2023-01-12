package TangenOblig2;

import java.util.ArrayList;

public class Hare extends Dyr{
    private String type;
    private String farge;

    private ArrayList<GjenfangstHare> gjenfangst = new ArrayList<>();


    public Hare(String raseid, String kjonn, Float lengde, Float vekt, String sted, String dato, String type, String farge, ArrayList<GjenfangstHare> gjenfangst) {
        super(raseid, kjonn, lengde, vekt, sted, dato);
        this.type = type;
        this.farge = farge;
        this.gjenfangst = gjenfangst;
    }

    public String getType() {
        return type;
    }

    public String getFarge() {
        return farge;
    }

    public ArrayList<GjenfangstHare> getGjenfangst() {
        return gjenfangst;
    }

    @Override
    public String toString() {
        return "Hare{" +
                "type='" + type + '\'' +
                ", farge='" + farge + '\'' +
                ", gjenfangst=" + gjenfangst +
                "} " + super.toString();
    }
}
