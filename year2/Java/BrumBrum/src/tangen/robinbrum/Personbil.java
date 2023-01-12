package tangen.robinbrum;

public class Personbil extends Kjøretøy {
    private int antallseter;

    public Personbil(String regNr, String produsent, String modell, int regår, int antallseter) {
        super(regNr, produsent, modell, regår);
        this.antallseter = antallseter;
    }

    public int getAntallseter() {
        return antallseter;
    }

    public void setAntallseter(int antallseter) {
        this.antallseter = antallseter;
    }

    @Override
    public String toString() {
        return "Personbil{" +
                "antallseter=" + antallseter +
                "} " + super.toString();
    }

}
