package Abstrakt;

public class Sirkel extends Figur {
    //Vi må vite radien
    //Enheten Pi henter vi fra klassen Math
    private double radius;

    //Konstruktør
    public Sirkel(double radius) {
        this.radius = radius;
    }

    @Override
    public double beregnAreal() {
        return Math.PI * radius * radius;
    }
}

