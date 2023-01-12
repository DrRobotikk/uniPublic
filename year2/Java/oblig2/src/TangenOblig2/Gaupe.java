package TangenOblig2;

import java.util.ArrayList;

public class Gaupe extends Dyr{
    private float lengdeorer;

    private ArrayList<GjenfangstGaupe> gjenfangst = new ArrayList<>();

    public Gaupe(String raseid, String kjonn, Float lengde, Float vekt, String sted, String dato, float lengdeorer, ArrayList<GjenfangstGaupe> gjenfangst) {
        super(raseid, kjonn, lengde, vekt, sted, dato);
        this.lengdeorer = lengdeorer;
        this.gjenfangst = gjenfangst;
    }

    public float getLengdeorer() {
        return lengdeorer;
    }

    public ArrayList<GjenfangstGaupe> getGjenfangst() {
        return gjenfangst;
    }

    @Override
    public String toString() {
        return "Gaupe{" +
                "lengdeorer=" + lengdeorer +
                ", gjenfangst=" + gjenfangst +
                "} " + super.toString();
    }
}
