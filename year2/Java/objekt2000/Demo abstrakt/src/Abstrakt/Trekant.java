package Abstrakt;

public class Trekant extends Figur {
    private double høyde;
    private double lengde;


    //Konstruktør
    public Trekant(double høyde, double lengde) {
        this.høyde = høyde;
        this.lengde = lengde;
    }


    @Override
    public double beregnAreal() {
        return lengde * høyde / 2;
    }
}
