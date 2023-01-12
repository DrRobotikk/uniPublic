package Abstrakt;

public class Kvadrat extends Figur {
    //I et kvadrat er alle sidene ike lange
    //Derfor trenger vi bare å vite om en av dem:
    private double side;

    //Konstruktør
    public Kvadrat(double side) {
        this.side = side;
    }

    @Override
    public double beregnAreal() {
        return side * side;
    }
}

