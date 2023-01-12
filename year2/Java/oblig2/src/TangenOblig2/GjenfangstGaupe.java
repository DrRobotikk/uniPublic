package TangenOblig2;

public class GjenfangstGaupe extends Gjenfangst{
    private float nyLengdeorer;

    public GjenfangstGaupe(String nyraseid, String nydato, Float nyvekt, Float nylengde, String nysted, float nyLengdeorer) {
        super(nyraseid, nydato, nyvekt, nylengde, nysted);
        this.nyLengdeorer = nyLengdeorer;
    }

    public float getNyLengdeorer() {
        return nyLengdeorer;
    }



    @Override
    public String toString() {
        return "GjenfangstGaupe{" +
                "nyLengdeorer=" + nyLengdeorer +
                "} " + super.toString();
    }
}
