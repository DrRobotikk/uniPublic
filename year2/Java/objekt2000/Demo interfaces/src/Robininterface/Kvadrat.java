package Robininterface;

public class Kvadrat implements Figur {
    private double side;

    public Kvadrat(double side) {
        this.side = side;
    }

    public double beregnAreal() {
        return side * side;
    }


}

